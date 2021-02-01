import socket 
import threading
import pickle as p 
class Server:
    port = 8000
    IP = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,port))

    def connect(self,conn,addr):
        connection = True
        print(f"[CONNECTED] {addr}")
        while connection:
            try:
                let = p.loads(conn.recv(64))
                if let:
                    message = p.loads(conn.recv(int(let)))
                    if(message=="exit"):
                        connection = False
                    else: 
                        print(message)
            except:
                pass
        print(f"[DISCONNECTED] {addr}")

    def start(self):
        self.server.listen()
        while 1:
            conn,addr = self.server.accept()
            thread = threading.Thread(target=self.connect,args=(conn,addr))
            thread.start()

copy = Server()
copy.start()