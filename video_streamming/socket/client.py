import socket
import sys
import errno
from threading import Thread
from gui import ChatRoomGui
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 1234))
    client.setblocking(False)
except Exception as e:
    print(f"connection to server has issue: {e}")
HEADER_SIZE = 10


def send_mess(client, user_name):
    """
    send mess to chat room
    :param client: client connection
    :param user_name: user name
    :return:
    """
    while True:
        try:
            print(f"{user_name} >>")
            mess = input(f'')
            client.send(bytes(encode_with_header(mess), "utf-8"))
            # send quit mess , then break while loop
            if mess == 'quit()':
                break
        except Exception as e:
            print(e)


def receive_mess(soc):
    """
    receive mess from server
    :param soc: client connection
    :return: None
    """
    while True:
        try:
            mess_header_size = soc.recv(HEADER_SIZE)
            mess_len = int(mess_header_size.decode('utf-8'))
            mess = soc.recv(mess_len).decode('utf-8')
            # receive mess from server before server close the connection
            print(f"{mess}")
            if mess == 'Close connect':
                break
        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected,
            # means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
            # We just did not receive anything
            continue


def encode_with_header(mess):
    return f"{len(mess):<{HEADER_SIZE}}" + mess


def get_mess_len(conn):
    mess_header_size = conn.recv(HEADER_SIZE)
    return int(mess_header_size.decode('utf-8'))


if __name__ == "__main__":

    print("your username is:")
    user_name = input("")
    mess = f"{user_name}"
    mess_header = f"{len(mess):<{HEADER_SIZE}}"
    client.send(bytes(mess_header + mess, "utf-8"))
    Thread(target=send_mess, args=(client, user_name)).start()
    Thread(target=receive_mess, args=(client,)).start()

