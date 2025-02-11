# extlookup: Advanced File Extension Lookup Tool

## Overview

`extlookup` is an advanced Python-based utility designed for retrieving detailed metadata about file extensions using information from [file-extension.info](https://www.file-extension.info). It leverages web scraping techniques to extract relevant data and presents the results in a structured, colorized format for improved readability.

## Features

- Efficient retrieval of file extension metadata
- Displays structured information including title, name, developer, and description
- Utilizes `requests` for HTTP communication and `BeautifulSoup` for parsing HTML content
- Enhanced console output with `colorama` for better visual presentation
- Robust error handling to manage connectivity and parsing issues

## Prerequisites

Ensure that the following dependencies are installed before running the script:

```bash
pip install requests beautifulsoup4 colorama
```

## Installation

To install and set up `extlookup`, follow these steps:

```bash
git clone https://github.com/yourusername/extlookup.git
cd extlookup
```

## Usage

To perform a file extension lookup, execute the script with the desired file extension:

```bash
python extlookup.py txt
```

### Example Output

```bash
[i] Title:       File Extension TXT
[i] Name:        Text File
[i] Dev:         Microsoft Corporation
[i] Description: Standard text document format
```

## Error Handling

The script includes robust error handling mechanisms:

- If the website is unreachable, it outputs:
  ```
  [!]: Couldn't reach the site!
  ```
- If an unexpected error occurs, it displays:
  ```
  [!]: Something went wrong
  L->    <error message>
  ```

## License

This project is distributed under the **GNU General Public License v3.0**. Refer to the `LICENSE` file for full terms and conditions.

## Author

**rax** – Black/Slash 2025
