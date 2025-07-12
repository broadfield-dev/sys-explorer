import os
import io
import argparse  # <-- ADDED: To handle command-line arguments
from flask import Flask, render_template, request, redirect, url_for, flash
from repo_to_md import create_markdown_document

app = Flask(__name__)
app.secret_key = os.urandom(24) 

BASE_DIR = os.path.realpath('/')

def get_directory_contents(path):
    dirs = []
    files = []
    try:
        for item in sorted(os.listdir(path), key=str.lower):
            full_path = os.path.join(path, item)
            if not os.access(full_path, os.R_OK):
                continue
            if os.path.isdir(full_path):
                dirs.append({'name': item, 'path': full_path})
            else:
                files.append({'name': item, 'path': full_path})
    except (FileNotFoundError, PermissionError) as e:
        flash(f"Error accessing path: {e}", "error")
        return [], []
    return dirs, files

def prepare_files_for_repo_to_md(selected_paths):
    file_objects = []
    for path in selected_paths:
        safe_path = os.path.realpath(path)
        # Security check remains important
        if not safe_path.startswith(BASE_DIR):
            print(f"Skipping insecure path: {path}")
            continue

        if os.path.isfile(safe_path):
            try:
                with open(safe_path, 'rb') as f:
                    content = f.read()
                    file_data = io.BytesIO(content)
                    file_data.filename = os.path.relpath(safe_path, BASE_DIR)
                    file_objects.append(file_data)
            except Exception as e:
                print(f"Could not read file {safe_path}: {e}")

        elif os.path.isdir(safe_path):
            for root, _, filenames in os.walk(safe_path):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    try:
                        with open(file_path, 'rb') as f:
                            content = f.read()
                            file_data = io.BytesIO(content)
                            file_data.filename = os.path.relpath(file_path, BASE_DIR)
                            file_objects.append(file_data)
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
    return file_objects

@app.route('/', methods=['GET', 'POST'])
def explorer():
    markdown_result = None
    if request.method == 'POST':
        selected_items = request.form.getlist('selected_items')
        if not selected_items:
            flash("No files or folders were selected.", "error")
        else:
            file_objects = prepare_files_for_repo_to_md(selected_items)
            if not file_objects:
                flash("No readable files were found in the selection.", "error")
            else:
                markdown_result = create_markdown_document(files=file_objects)

    req_path = request.args.get('path', BASE_DIR)
    
    safe_path = os.path.realpath(req_path)
    if not safe_path.startswith(BASE_DIR):
        flash(f"Access denied: You cannot navigate outside the base directory.", "error")
        return redirect(url_for('explorer', path=BASE_DIR))
    
    if not os.path.exists(safe_path) or not os.path.isdir(safe_path):
        flash(f"Path not found or is not a directory: {safe_path}", "error")
        return redirect(url_for('explorer', path=BASE_DIR))

    dirs, files = get_directory_contents(safe_path)
    
    parent_path = None
    if safe_path != BASE_DIR:
        parent_path = os.path.dirname(safe_path)

    return render_template('index.html', 
                           current_path=safe_path, 
                           parent_path=parent_path,
                           dirs=dirs, 
                           files=files,
                           markdown_result=markdown_result)

def main():
    """
    This is the entry point function for the command-line tool.
    """
    parser = argparse.ArgumentParser(description="Run the Sys-Explorer web app.")
    parser.add_argument('--host', default='127.0.0.1', help='The host to bind to.')
    parser.add_argument('--port', type=int, default=5000, help='The port to listen on.')
    parser.add_argument('--debug', action='store_true', help='Enable Flask debug mode.')
    args = parser.parse_args()

    print(f" * Starting Sys-Explorer server at http://{args.host}:{args.port}")
    print(" * Navigate your file system, select files/folders, and generate markdown.")
    print(" * Press CTRL+C to quit.")
    
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == '__main__':
    main()
