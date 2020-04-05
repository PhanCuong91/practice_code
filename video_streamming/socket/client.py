import socket
import os
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    mess = input("")
    print(mess)
    mess_header = f"{len(mess):<{HEADERSIZE}}"
    s.send(bytes(mess_header+mess, "utf-8"))
# while True:
# full_msg = ''
# new_mess = True
# while True:
#     mess = s.recv(16)
#     if new_mess:
#         # print(f"length of mess is {mess[:HEADERSIZE]}")
#         # print(mess[:HEADERSIZE])
#         mess_len = int(mess[:HEADERSIZE])
#         new_mess = False
#     # print(mess[HEADERSIZE:])
#     full_msg += mess.decode("utf-8")
#     # print(full_msg)
#     if len(full_msg) - HEADERSIZE == mess_len:
#         print(full_msg[HEADERSIZE:])
#         new_mess = True
#         full_msg = ''
#         break

