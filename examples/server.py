# web application
import socket
sock = socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("request information:", data)

    conn.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello world")
    conn.close()
