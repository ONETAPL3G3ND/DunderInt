class Server:
    def __init__(self):
        self.ConnectedUsers = 0

    def ConnectNewUser(self):
        self.ConnectedUsers += 1

    def DisconnectUser(self):
        if self.ConnectedUsers > 0:
            self.ConnectedUsers -= 1
            return
        raise Exception

    def GetCountUser(self):
        return int(self)

    def __int__(self):
        return self.ConnectedUsers



if __name__ == "__main__":
    server = Server()
    server.ConnectNewUser()
    server.ConnectNewUser()

    print(server.GetCountUser())

    server.DisconnectUser()

    print(server.GetCountUser())


