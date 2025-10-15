from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Simple Web Server</title>
</head>
<body>
<h1 align="center">19AI414-Fundamentals of Web Application Development</h1>
<h2>Execrise 1: Simple Web Server</h2>
<pre>Status: Completed Successfully!!!!</pre>
</body>
</html>
"""
class SimpleWebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8005)
httpd = HTTPServer(server_address,SimpleWebServer)
print("my webserver is running...")
httpd.serve_forever()
