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

You can install this tool directly from the GitHub repository using `pip`. This will also install all necessary dependencies, including `Flask` and `repo-to-md`.

```bash
pip install git+https://github.com/your-username/sys-explorer.git
```
*Replace `your-username/sys-explorer` with your actual GitHub repository URL.*

---

## How to Run the Application

There are two ways to run the application, depending on your goal.

### 1. For Regular Use (After Installation)

This is the simplest method and is recommended for most users.

After following the installation steps above, the `sysexplorer` command will be available in your terminal.

**Step 1: Start the server**

```bash
sysexplorer
```

**Step 2: Open your browser**

Navigate to **http://127.0.0.1:5000**.

**Command-Line Options**

You can also specify the host and port.

To run on a different port:
```bash
sysexplorer --port 8080
```

To make it accessible on your local network (use with caution):
```bash
sysexplorer --host 0.0.0.0
```

### 2. For Development (Running from Source)

If you want to modify the code or contribute to the project, you should run it directly from the source code.

**Step 1: Clone the repository**

```bash
git clone https://github.com/your-username/sys-explorer.git
cd sys-explorer
```

**Step 2: Create and activate a virtual environment** (Recommended)

This isolates the project's dependencies from your system's Python.

For **macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

For **Windows**:
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Step 3: Install the dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the application**

```bash
python -m sysexplore.app
```
The server will start, and you can access it at **http://127.0.0.1:5000**.

---

## Security Warning

This application is intended for **local use only**. Do not expose it to the public internet without implementing proper authentication and further security hardening. By default, it is restricted to your user's home directory.

## License

This project is licensed under the MIT License.
