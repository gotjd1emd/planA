#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write("Hello World")
try:
    server = HTTPServer(('172.30.1.48', 8888), MyHandler)
    print "Started WebServer on port 8888..."
    print "Press ^C to quit WebServer"
    print __name__
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
