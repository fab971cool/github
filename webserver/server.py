import http.server as hsv
import socketserver

PORT = 8080
Handler = hsv.SimpleHTTPRequestHandler


with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# @param test
# ! do not use 

