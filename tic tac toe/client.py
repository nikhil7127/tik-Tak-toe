import socket
import pickle as p 

class Client:
    client = socket.socket()
    ip = socket.gethostbyname(socket.gethostname())
    port = 8000
    client.connect((ip,port))

    def sendMessage(self,msg):
        message = p.dumps(msg)
        temp = len(message)
        temp = p.dumps(str(temp)) + b" " * (64 - temp)
        self.client.send(temp)
        self.client.send(message)

copy = Client()
while(1):
    inp = input()
    copy.sendMessage(inp)
    if(inp == "exit"):
        break