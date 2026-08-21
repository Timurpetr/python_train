class Server:
    count = 0

    def __init__(self):
        Server.count += 1
        self.ip = Server.count
        self.buffer = []
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        server.router = self
        self.servers[server.get_ip()] = server

    def unlink(self, server):
        if server.get_ip() in self.servers:
            self.servers.pop(server.get_ip())
            server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer = []


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv1 = Server()
sv2 = Server()

router.link(sv1)
router.link(sv2)

print(sv1.router is router)  # True
print(sv2.router is router)  # True
