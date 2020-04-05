import socket
import time
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
    # for i in range(len(arr_con)):
        # arr_con[i].close()
    # arr_address = []
    # arr_con = []
    # while True:
    conn, add = soc.accept()
    # arr_con.append(conn)
    # arr_address.append(add)
    # send_command(conn)
    while True:
        mess_header_size = conn.recv(HEADERSIZE)
        mess_len = int(mess_header_size.decode('utf-8'))
        mess = conn.recv(mess_len).decode('utf-8')
        print(f"{mess}")


def receive_mess(conn):
    mess_header_size = conn.recv(HEADERSIZE)
    mess_len = int(mess_header_size.decode('utf-8'))
    mess = conn.recv(mess_len).decode('utf-8')
    print(f"{mess}")
    conn.close()


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
