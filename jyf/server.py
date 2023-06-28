import http.server
import socketserver
import os
import json
import psutil
import chardet
from urllib.parse import urlparse, parse_qs, unquote
from http.server import SimpleHTTPRequestHandler
from urllib.parse import unquote_plus
from http import HTTPStatus

# Define server port
PORT = 8090

# Define the list of saved files
saved_files = []

# Define the file formats to be saved
file_formats = ['.pdf', '.docx', '.txt']

def get_folders_recursive(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return folders


def save_files_recursive(path):
    files = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] in file_formats:
                files.append(os.path.join(root, filename))
    return files

def search_files(keyword):
    search_result = {}
    for file in saved_files:
        try:
            with open(file, 'rb') as f:
                data = f.read()
                encoding = chardet.detect(data)['encoding']
                if encoding is None:
                    encoding = 'utf-8'
            with open(file, 'r', encoding=encoding, errors='ignore') as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, start=1):
                    if keyword.lower() in line.lower():
                        result = {'line': line_num, 'content': line.strip()}
                        if file in search_result:
                            search_result[file].append(result)
                        else:
                            search_result[file] = [result]

        except:
            pass
    return search_result

def get_drives():
    drives = []
    for drive in psutil.disk_partitions():
        if 'cdrom' in drive.opts or drive.fstype == '':
            continue
        drives.append(drive.device)
    return drives

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global saved_files
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        if path == '/drives':
            drives = get_drives()
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(drives).encode('utf-8'))
        elif path == '/folders':
            drive_path = unquote(query_params['path'][0])
            folders = get_folders_recursive(drive_path)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(folders).encode('utf-8'))
        elif path == '/save':
            folder_path = unquote(query_params['path'][0])
            saved_files = save_files_recursive(folder_path)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write('Files saved successfully.'.encode('utf-8'))
        elif path == '/search':
            keyword = unquote(query_params['keyword'][0])
            search_result = search_files(keyword)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(search_result, ensure_ascii=False).encode('utf-8'))
        else:
            super().do_GET()

    def end_headers(self):
        self.send_my_headers()
        super().end_headers()

    def send_my_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.NO_CONTENT)
        self.send_my_headers()
        self.end_headers()

# Create an HTTP server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server running on port", PORT)
    httpd.serve_forever()
