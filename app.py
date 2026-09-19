import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 10000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # अगर templates फोल्डर में index.html या base.html है
            if os.path.exists('templates/index.html'):
                self.path = 'templates/index.html'
            elif os.path.exists('templates/base.html'):
                self.path = 'templates/base.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
