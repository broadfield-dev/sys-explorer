# Sys-Explorer

A simple but powerful web-based tool to explore your local file system, select files and folders, and generate a single, comprehensive markdown document from their contents. Ideal for creating context for LLMs, generating project summaries, or creating documentation.

This tool is built with Flask and `repo-to-md`.

## Features

-   **Web-Based UI**: Easy-to-use interface accessible from your browser.
-   **File & Folder Selection**: Select individual files or entire directories.
-   **Recursive Directory Traversal**: Automatically includes all files within selected folders.
-   **Instant Markdown Generation**: See the combined markdown output in real-time.
-   **Copy to Clipboard**: Easily copy the entire output.
-   **Download as Text**: Save the output as a `.md.txt` file.
-   **Security**: Confined to your user's home directory to prevent access to system-critical files.

## Installation

You can install this tool directly from your GitHub repository using `pip`.

```bash
pip install git+https://github.com/broadfield-dev/sys-explorer.git
