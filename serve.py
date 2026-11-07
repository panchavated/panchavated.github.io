import http.server
import socketserver
import webbrowser
import threading
import sys
import os

PORT = 8000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent browser caching so local edits appear immediately
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    webbrowser.open(f'http://localhost:{PORT}/test.html')

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("=" * 60)
    print("  🌐 LOCAL PORTFOLIO PREVIEW SERVER")
    print("=" * 60)
    print(f"  • Test Page:        http://localhost:{PORT}/test.html")
    print(f"  • Production View:  http://localhost:{PORT}/index.html")
    print(f"  • Single-file Test: http://localhost:{PORT}/test-standalone.html")
    print("-" * 60)
    print("  Opening test page in your browser...")
    print("  Press Ctrl + C in this terminal window to stop the server.")
    print("=" * 60)

    # Open browser automatically after 1 second
    threading.Timer(1.2, open_browser).start()

    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down preview server. Goodbye!")
            sys.exit(0)

if __name__ == '__main__':
    main()
