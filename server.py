import socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        print(f'{self.address_string()} - {format % args}')


class ThreadedServer(socketserver.ThreadingMixIn, HTTPServer):
    daemon_threads = True


if __name__ == '__main__':
    server = ThreadedServer(('', 8888), CORSHandler)
    print('Servidor rodando em http://localhost:8888')
    server.serve_forever()
