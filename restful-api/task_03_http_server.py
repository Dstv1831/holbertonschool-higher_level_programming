#!/usr/bin/python3

import http.server
import socketserver
import json

PORT = 8000

API_DATA = {
    "data": {"name": "John", "age": 30, "city": "New York"},
    "info": {"version": "1.0", "description": "A simple API built with http.server"}
}

class Server(http.server.SimpleHTTPRequestHandler):

    def __init__(self, api_data = None):
        "Initialize with external data"
        super.__init__()
        self.api_data = api_data

    def json_response(self, data, status = 200):
        "From Dict to Json to web-server"
         # encoding is neccesary because .wfile.write expect bytes object, not String object
        json_data = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_data)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.json_response(self.api_data.get("data", {}) )

        elif self.path == '/info':
            self.json_response(self.api_data.get("info", {}) )

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), Server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
