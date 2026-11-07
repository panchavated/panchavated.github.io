import http.server
import socketserver
import webbrowser
import threading
import socket
import sys
import os

PREFERRED_PORTS = [8080, 5500, 3000, 8001, 8081, 8000]

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent browser caching so local edits appear immediately
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def find_available_port(ports):
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    # Fallback to an OS-assigned ephemeral free port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

def open_browser(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Could not auto-open browser: {e}")

def main():
    # Ensure current directory is the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    port = find_available_port(PREFERRED_PORTS)
    url_test = f"http://127.0.0.1:{port}/test.html"
    url_prod = f"http://127.0.0.1:{port}/index.html"

    print("=" * 64)
    print("  🌐 LOCAL PORTFOLIO PREVIEW SERVER")
    print("=" * 64)
    print(f"  👉 Test Page:       {url_test}")
    print(f"  👉 Production View: {url_prod}")
    print("-" * 64)
    print("  Opening browser automatically...")
    print("  Press Ctrl + C in this window to stop the server.")
    print("=" * 64)

    # Open browser in a separate thread
    threading.Timer(1.0, open_browser, args=[url_test]).start()

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", port), NoCacheHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server. Goodbye!")
    except Exception as err:
        print(f"\n❌ Error starting server: {err}")
        input("\nPress Enter to close...")

if __name__ == '__main__':
    main()
