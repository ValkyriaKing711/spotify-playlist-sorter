import socket


class Server:

    def __init__(self):
        self.code = ''

    async def create_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 80))
        self.server.listen(1)
        while self.code == '':
            (conn, _) = self.server.accept()
            data = str(conn.recv(1024))
            self.code = data.split(
                'GET /?code=')[1].split(' HTTP/1.1')[0] or ''
            conn.send("You can close this page now".encode())
            conn.close()

    async def close_server(self):
        self.server.close()  # self.server.shutdown well doesn't work
