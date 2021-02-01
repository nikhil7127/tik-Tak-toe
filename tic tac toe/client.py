import socket
import pickle as p 
import threading
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
    
    def receive(self):
        while(1):
            try:
                msg = p.loads(self.client.recv(64))
                if(msg):
                    msg = p.loads(self.client.recv(int(msg)))
                    if(msg=="exit"):
                        break
                    else:
                        print((msg))

            except:
                pass

copy = Client()
def sendMsg():
    while(1):
        inp = input()
        copy.sendMessage(inp)
        if(inp == "exit"):
            break

recving = threading.Thread(target=copy.receive)
recving.start()
send = threading.Thread(target=sendMsg)
send.start()
