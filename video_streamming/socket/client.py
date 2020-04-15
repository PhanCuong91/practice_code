import socket
import sys
import errno
from threading import Thread


class Client:

    def __init__(self, debug_log=False):
        try:
            self.debug_log = debug_log
            self.rec_bool = False
            self.Client__quit = False
            self.quit = False
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((socket.gethostname(), 1234))
            self.client.setblocking(False)
            self.mess = ''

        except Exception as e:
            print(f"connection to server has issue: {e}")
        self.HEADER_SIZE = 10

    def send_mess(self, arg_client, arg_user_name, mess):
        """
        send mess to chat room
        :param arg_client: client connection
        :param arg_user_name: user name
        :return:
        """
        # while loop for testing purpose
        # while True:
        try:
            # print(f"{arg_user_name} >>")
            # mess = input(f'')
            arg_client.send(bytes(self.encode_with_header(mess), "utf-8"))
        except Exception as e:
            print(f"Client class, send mess function: {e}")

    def receive_mess(self, quit):
        """
        receive mess from server
        :param soc: client connection
        :return: None
        """
        # while loop for testing purpose
        # while True:
        try:
            mess_header_size = self.client.recv(self.HEADER_SIZE)
            mess_len = int(mess_header_size.decode('utf-8'))
            self.mess = self.client.recv(mess_len).decode('utf-8')
            self.rec_bool = True
            # receive mess from server before server close the connection
            if self.debug_log:
                print(f"Debug log: receive message is {self.mess}")
                print(f"Debug log: receive bool is {self.rec_bool}")
            if quit is True or self.mess == 'Close connect':
                self.disconnect_server()
                # break

        except IOError as e:
            # This is normal on non blocking connections -
            # when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected,
            # means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
            # We just did not receive anything
            # continue

    def encode_with_header(self, mess):
        return f"{len(mess):<{self.HEADER_SIZE}}" + mess

    def get_mess_len(self, conn):
        mess_header_size = conn.recv(self.HEADER_SIZE)
        return int(mess_header_size.decode('utf-8'))

    def disconnect_server(self):
        self.client.close()


if __name__ == "__main__":
    client = Client()
    print("your username is:")
    user_name = input("")
    messa = f"{user_name}"
    mess_header = f"{len(messa):<{client.HEADER_SIZE}}"
    client.client.send(bytes(mess_header + messa, "utf-8"))
    Thread(target=client.send_mess, args=(client.client, user_name)).start()
    Thread(target=client.receive_mess, args=(client.client,)).start()

