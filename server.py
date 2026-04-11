import http.server
import socketserver
import os

PORT = 8080

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Remove query parameters from path if any
        path = self.path.split('?')[0]
        
        # Translate the URL path to a local file system path
        translated_path = self.translate_path(path)
        
        # If the requested path is not a file and doesn't end with a slash
        # check if appending .html matches a file
        if not os.path.exists(translated_path) and not path.endswith('/'):
            html_path = translated_path + '.html'
            if os.path.exists(html_path):
                self.path = path + '.html'
                
        return super().do_GET()

# To allow reusing the port quickly if restarted
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Servidor de teste rodando em http://localhost:{PORT}")
    print("Suporte a URLs limpas (sem .html) ATIVADO!")
    httpd.serve_forever()
