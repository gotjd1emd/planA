#!usr/bin/env python

def my_app(environ, start_response):

  status = "200 OK"
  headers = [('Content-Type', 'test/plain')]
  start_response(status, headers)

  return ["This is a sample WSGI Application."]

try:
    from wsgiref.simple_server import make_server

    print "Started WSGI Server on port 8888..."
    server = make_server('172.30.1.13', 8888, my_app)
    server.serve_forever()

except KeyboardInterrupt:
    print "^C received, shutting down the web server"
    server.server_close()
