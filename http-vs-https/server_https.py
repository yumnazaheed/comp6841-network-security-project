#server-ubuntu — TLS-wrapped version
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('login.html', 'rb') as f:
            self.wfile.write(f.read())

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        print("Received login attempt:", post_data.decode())
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h2>Login received (demo only)</h2></body></html>")

server = HTTPServer(('0.0.0.0', 8443), Handler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
server.socket = context.wrap_socket(server.socket, server_side=True)
print("Serving HTTPS on port 8443...")
server.serve_forever()
