import http.server
import socketserver
import mimetypes

mimetypes.add_type("model/vnd.usdz+zip", ".usdz")

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

