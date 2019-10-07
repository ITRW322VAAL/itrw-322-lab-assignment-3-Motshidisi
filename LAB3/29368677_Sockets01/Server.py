import socket 

HOST = '127.0.0.1'
PORT = 9999

with socket.socket(socket.AF.INET, socket.SOCK_STREAM) as s:
s.blind ((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:

 print ('Server is connected with address', addr)
 while True:
  data = conn.recv(2048)
  if not data:
   break
   conn.sendall(data)