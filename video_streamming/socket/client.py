import socket
import os, sys, errno
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
s.setblocking(False)
HEADERSIZE = 10


def send_mess(soc):

    while True:
        try:
            mess = input(f'{user_name} > ')
            mess = f"{user_name} >> {mess}"
            mess_header = f"{len(mess):<{HEADERSIZE}}"
            soc.send(bytes(mess_header+mess, "utf-8"))
        except Exception as e:
            print(e)


def receive_mess(soc):

    while True:
        try:
            mess_header_size = soc.recv(HEADERSIZE)
            mess_len = int(mess_header_size.decode('utf-8'))
            mess = soc.recv(mess_len).decode('utf-8')
            print(f"{mess}")
        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
            # We just did not receive anything
            continue


if __name__ == "__main__":
    user_name = input("user name is ")
    Thread(target=send_mess, args=(s,)).start()
    Thread(target=receive_mess, args=(s,)).start()

