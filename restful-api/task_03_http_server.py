#!/usr/bin/python3

import http.server
import socketserver
import json

PORT = 8000

class Server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            # encoding is neccesary because .wfile.write expect bytes object, not String object
            json_data = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == '/info':
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            # encoding is neccesary because .wfile.write expect bytes object, not String object
            json_data = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == '/status':
            self.send_response(200)
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), Server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
