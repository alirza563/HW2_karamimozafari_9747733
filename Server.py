import socket
import os

HOST = '127.0.0.1'
PORT = 65432


files = os.listdir('serverFile')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct:
    sct.bind((HOST, PORT))
    sct.listen()
    conn, addr = sct.accept()

    with conn:
        print('Connected by', addr)
        isFileFound = False
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            for file in files:
                if data + ".html" == file:
                    conn.sendall("200 ok".encode())
                    isFileFound = True

                    filePath = "serverFile/" + data + ".html"
                    fileFound = open(filePath, 'rb')
                    result = fileFound.read(1024)
                    while (result):
                        conn.send(result)
                        result = fileFound.read(1024)
                    fileFound.close()
                    break


            if not isFileFound:
                conn.sendall("404 Not Found".encode())

