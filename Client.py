import socket
import os

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    name = input("name : ")
    fileAddress = input("fileAdress : ")
    savePath = fileAddress + name + ".html"

    s.sendall(name.encode())
    response = s.recv(1024).decode()
    print(response)

    if response == "200 ok":
        with open(savePath, 'wb') as sf:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                sf.write(data)
            print(name + " saved in " + savePath)