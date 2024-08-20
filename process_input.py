import os
import requests
import json

# API settings
API_KEY = ""
API_URL = "https://api.anthropic.com/v1/messages"

# Configuration
input_file = "changelog.txt"
output_dir = "changelog_chunk_processed"
max_chunk_size = 400  # max characters per request - 8000 should work but wasnt tested



def chunk_text(text, max_chunk_size):
    """Split text into smaller chunks."""
    chunks = []
    while len(text) > max_chunk_size:
        split_index = text.rfind("\n", 0, max_chunk_size)
        if split_index == -1:
            split_index = max_chunk_size
        chunks.append(text[:split_index])
        text = text[split_index:]
    chunks.append(text)
    return chunks

def escape_special_characters(text):
    """Escape characters that might cause issues in JSON or API interpretation."""
    return json.dumps(text)

def call_anthropic_api(diff_content):
    """Send a request to the Anthropic API to summarize a git diff for a commit message."""
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",  # Required version header
              # Beta header for extended tokens
    }
    # Construct the prompt with specific instructions for summarizing a git diff
    prompt = f"Summarize the following git diff content into a concise commit message:\n\n{diff_content}"
    
    data = {
        "model": "claude-3-5-sonnet-20240620",  # Use the correct model
        "messages": [
            {"role": "user", "content": escape_special_characters(prompt)}
        ],
        "max_tokens": 8192,  # Request up to 8192 tokens in the response
    }
    response = requests.post(API_URL, headers=headers, json=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Response content:", response.content.decode())  # Print detailed error response
        raise
    return response.json()

    
def process_file(input_file, output_dir):
    """Process the file, split it into parts, and send to the Anthropic API."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = chunk_text(text, max_chunk_size)
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1} of {len(chunks)}")
        try:
            response_text = call_anthropic_api(chunk)
        except Exception as e:
            print(f"Failed to process chunk {i + 1}: {e}")
            continue

        output_file = os.path.join(output_dir, f"output_{i + 1}.txt")
        with open(output_file, "w", encoding="utf-8") as output:
            output.write(json.dumps(response_text, indent=2))  # Serialize dict to JSON string
        print(f"Result saved to: {output_file}")

if __name__ == "__main__":
    process_file(input_file, output_dir)