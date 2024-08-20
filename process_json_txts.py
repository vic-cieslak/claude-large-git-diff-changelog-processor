import os
import json

# Directory containing the output files
directory = '/home/vic/Projects/changelog_processor/changelog_chunk_processed/'

# Output file to save extracted text
output_file = 'extracted_texts.txt'

# Function to extract text from the JSON data
def extract_text_from_json(data):
    try:
        # Extract the text from the 'content' field
        text = data['content'][0]['text']
        return text
    except (KeyError, IndexError):
        return None

# Process each file in the directory
with open(output_file, 'w') as output:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                try:
                    json_data = json.load(file)
                    text = extract_text_from_json(json_data)
                    if text:
                        output.write(text + "\n\n")  # Write the extracted text to the output file
                except json.JSONDecodeError:
                    print(f"Could not decode JSON in file: {filename}")

print(f"Extraction complete. Extracted texts saved to {output_file}")
