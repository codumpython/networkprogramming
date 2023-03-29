import socket

s = socket.socket()
host = socket.gethostname()
port = 9992

s.bind((host,port))
s.listen(5)

while True:
    conn,addr = s.accept()
    print("Bağlatı Kuruldu ",addr)
    conn.send("")
    conn.close()