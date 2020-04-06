import socket
import time
from threading import Thread
HEADERSIZE = 10
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(1)
global host
global port
host = socket.gethostname()
port = 1234

arr_conn = []
arr_add = []


def create_socket():
    try:
        global soc
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Socket creation with {host} is successful")
    except socket.error as msg:
        print(f"Socket creation error: {msg}")


def bind_socket():
    try:
        soc.bind((host, port))
        print(f"Socket binding port {port} is successful")
        soc.listen(5)
    except socket.error as msg:
        print(f"Socket binding error: {msg}")


def accept_socket(arr_con, arr_address):
    conn, add = soc.accept()
    arr_conn.append(conn)
    print(f"connection to is accepted with {conn} and {add}")
    Thread(target=receive_mess, args=(conn,)).start()


def broadcast(except_client, mess):
    for client in arr_conn:
        if except_client != client:
            try:
                mess = f"{len(mess):<{HEADERSIZE}}" + mess
                client.send(bytes(mess, "utf-8"))
            except Exception as e:
                print(f"Broadcast exception is {e}")


def receive_mess(conn):
    while True:
        try:
            mess_header_size = conn.recv(HEADERSIZE)
            mess_len = int(mess_header_size.decode('utf-8'))
            mess = conn.recv(mess_len).decode('utf-8')
            print(f"{mess}")
            if mess == 'Use quit() or Ctrl-Z plus Return to exit':
                conn.close()
                arr_conn.remove(conn)
                print(f"Disconnection")
                break
            broadcast(conn, mess)
        except Exception as e:
            print(f"[Receive message] Exception is {e}")
    # conn.close()


def send_command(conn):
    print(f"Connection from {conn} has been establish!")
    mess = f"welcome to socket and time is "
    mess = f"{len(mess):<{HEADERSIZE}}" + mess
    conn.send(bytes(mess, "utf-8"))
    conn.close()


if __name__ == "__main__":
    create_socket()
    bind_socket()
    while True:
        accept_socket(arr_conn, arr_add)
        # send_command()
