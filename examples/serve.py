# Web server in python, why?

from http.server import BaseHTTPRequestHandler, HTTPServer

# Listening on Port 80 for requests
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("Hello World!", "utf8"))
        return

# Server Configuration
port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()