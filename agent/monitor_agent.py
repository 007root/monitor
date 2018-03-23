from BaseHTTPServer import BaseHTTPRequestHandler
import json
from http import HttpGet

get = HttpGet()


class TodoHandler(BaseHTTPRequestHandler):

    def respond(self, ret):
        if ret:
                self.send_response(500)
                message = json.dumps(ret)
        else:
            self.send_response(200)
            message = None
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if message:
            self.wfile.write(message)

    def do_GET(self):
        # return all todos
        if self.path == '/nc':
            ret = get.nc()
            self.respond(ret)
        else:
            self.send_error(404, "File not found.")
            return


if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', 8888), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
