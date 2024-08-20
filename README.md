
# Large Git Diff Changelog Processor (Antrophic/Claude - claude-3-5-sonnet-20240620)
### Working as of Aug 20 2024

This project provides tools to process and summarize large git diff changelog files by interacting with the Anthropic API. The repository contains two Python scripts:

## Example input

[![Watch the video](https://img.youtube.com/vi/_4bHSJDp1wY/0.jpg)](https://www.youtube.com/watch?v=_4bHSJDp1wY)

## Markdown formatted example output (using gpt4 and some prompts)

[![Watch the video](https://img.youtube.com/vi/lASfNaNEYTg/0.jpg)](https://www.youtube.com/watch?v=lASfNaNEYTg)


1. **`process_input.py`**: This script processes a large git diff changelog file, splits it into smaller chunks, and sends these chunks to the Anthropic API to generate concise summaries or commit messages.
2. **`process_json_text.py`**: After the summaries are generated, this script extracts the relevant text from the API responses and compiles them into a single output file.

## Features

- **Chunk Processing**: Handles large git diff changelog files by splitting them into manageable chunks.
- **API Integration**: Interacts with the Anthropic API to generate summaries of each chunk.
- **Error Handling**: Includes robust error handling to manage API failures.
- **JSON Parsing**: Extracts and compiles text data from JSON responses.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `os`
  - `json`

You can install the necessary packages using:

```bash
pip install requests
```

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/vic-cieslak/claude-large-git-diff-changelog-processor.git
    cd claude-large-git-diff-changelog-processor
    ```

2. Set your Anthropic API key in the `process_input.py` file:

    ```python
    API_KEY = "your_api_key_here"
    ```

3. Place your `changelog.txt` file containing the git diff content in the project directory.

### Usage

#### Step 1: Process the Git Diff Changelog File

Run the `process_input.py` script to process the `changelog.txt` file and generate summarized chunks:

```bash
python process_input.py
```

This will create an `output_dir` folder where the summarized chunks are saved as JSON files.

#### Step 2: Extract Text from JSON Responses

After processing, run the `process_json_text.py` script to extract the summarized text from the JSON files:

```bash
python process_json_text.py
```

The extracted text will be saved in `extracted_texts.txt`.

## Example

Here's an example of how the output files are organized:

- **Input**: A large `changelog.txt` file containing git diff content.
- **Output**: Multiple JSON files in the `changelog_chunk_processed` directory, each containing a summary of a chunk of the original git diff content.
- **Final Output**: An `extracted_texts.txt` file containing all the summarized texts compiled together.

## Troubleshooting

- **API Errors**: If you encounter HTTP errors during API requests, the script will print the error details for debugging.
- **JSON Parsing Errors**: If the script fails to decode a JSON file, it will skip the file and notify you.


## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.


### Issues and improvements

Script was created ad hoc, prompt for generating git commit message could likely be improved. 
Chunking logic could be improved to not split in certain places of changelog.  

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

### Contact

For any questions or support, please open an issue on the GitHub repository.

---

