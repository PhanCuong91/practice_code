import socket
from threading import Thread

HEADER_SIZE = 10
global host
global port
host = socket.gethostname()
port = 1234
arr_conn = []


def create_socket():
    """
    create a socket for server
    :return: None
    """
    try:
        global server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Socket creation with {host} is successful")
    except socket.error as msg:
        print(f"Socket creation error: {msg}")


def bind_socket():
    """
    Binding socket for server
    :return:
    """
    try:
        server.bind((host, port))
        print(f"Socket binding port {port} is successful")
        server.listen(5)
    except socket.error as msg:
        print(f"Socket binding error: {msg}")


def accept_socket():
    """
    accept new client
    broadcast new user name to chat room
    run receive message function
    :return:
    """
    conn, add = server.accept()
    # add new connection to array which use for broadcasting
    arr_conn.append(conn)
    # get user name and broadcast to other user name who was in chat room
    mess_len = get_mess_len(conn)
    username = conn.recv(mess_len).decode('utf-8')
    print(f"connection: {username} joined chat room")
    broadcast(conn, f"connection: {username} joined chat room")
    # run receive_mess thread
    Thread(target=receive_mess, args=(conn, username)).start()


def broadcast(except_client, mess):
    """
    broadcast message to other clients except itself
    :param except_client: itself client
    :param mess: message
    :return: None
    """
    mess = f"{len(mess):<{HEADER_SIZE}}" + mess
    for client in arr_conn:
        # if client is not excepted client
        # then send message
        if except_client != client:
            try:
                send_mess(client, mess)
            except Exception as e:
                print(f"Broadcast exception is {e}")


def receive_mess(conn, username):
    """
    get message from client and broadcast to other client
    :param conn: connection of client
    :param username: user name of client
    :return: None
    """
    while True:
        try:
            mess_len = get_mess_len(conn)
            mess = conn.recv(mess_len).decode('utf-8')
            print(f"{username} >> {mess}")
            # if server receives quit message
            # broadcast respective user left chat room and close connection
            if mess == 'quit()':
                # then server send "Close connect" mess to respective client,
                mess = f"Close connect"
                mess = encode_with_header(mess)
                send_mess(conn, mess)
                # broadcast respective user left chat room
                broadcast(conn, f"{username} left chat room")
                # close connection and remove connection from connection array
                conn.close()
                arr_conn.remove(conn)
                print(f"Disconnection: {username} quited chat room")
                break
            # broadcast message with respect to user name
            mess = f"{username} >> {mess}"
            broadcast(conn, mess)
        except Exception as e:
            print(f"[Receive message] Exception is {e}")


def send_mess(conn, mess):
    """
    send mess
    :param conn:  connection
    :param mess: message
    :return: None
    """
    conn.send(bytes(mess, "utf-8"))


def encode_with_header(mess):
    return f"{len(mess):<{HEADER_SIZE}}" + mess


def get_mess_len(conn):
    mess_header_size = conn.recv(HEADER_SIZE)
    return int(mess_header_size.decode('utf-8'))


if __name__ == "__main__":
    create_socket()
    bind_socket()
    while True:
        accept_socket()
