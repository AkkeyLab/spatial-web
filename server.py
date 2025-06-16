import http.server
import socketserver
import mimetypes
import signal
import sys
import threading

PORT = 8000
mimetypes.add_type("model/vnd.usdz+zip", ".usdz")

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

def run_server():
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

def shutdown_server(sig, frame):
    print("\nShutting down server gracefully...")
    httpd.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_server)

server_thread = threading.Thread(target=run_server)
server_thread.start()
