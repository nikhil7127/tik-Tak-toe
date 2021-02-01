import socket 
import threading
import pickle as p 
class Server:
    port = 8000
    IP = socket.gethostbyname(socket.gethostname())
    server = socket.socket()
    server.bind((IP,port))
    connectionList = []

    def sendBack(self,msg):
        msg = p.dumps(msg)
        length = len(msg)
        temp = p.dumps(str(length)) + b' '*(64-length)
        for connect,_ in self.connectionList:
            connect.send(temp)
            connect.send(msg)

    def connect(self,conn,addr):
        connection = True
        print(f"[CONNECTED] {addr}")
        self.connectionList.append([conn,addr])
        while connection:
            try:
                let = p.loads(conn.recv(64))
                if let:
                    message = p.loads(conn.recv(int(let)))
                    if(message=="exit"):
                        self.sendBack(message)
                        connection = False
                    else: 
                        print(message)
                        self.sendBack(message)
            except:
                pass
        self.connectionList.remove([conn,addr])
        print(f"[DISCONNECTED] {addr}")

    def start(self):
        self.server.listen()
        while 1:
            conn,addr = self.server.accept()
            thread = threading.Thread(target=self.connect,args=(conn,addr))
            thread.start()

copy = Server()
copy.start()
