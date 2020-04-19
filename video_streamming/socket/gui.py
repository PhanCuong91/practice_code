import tkinter as tk
from client import Client
from threading import Thread


class ChatRoomGui(Client):

    def __init__(self, debug_log=False):
        # super().__init__(debug_log)
        self.Gui__quit = False
        self.max_len_txt_box = 40
        self.len_txt_box = 60
        self.gui = tk.Tk()
        self.gui.title('hello')
        self.gui.geometry("500x500")
        # self.chat_room_frame()

        self.label_usr_name = tk.Label(self.gui, text="user name")
        self.label_usr_name.place(x=10, y=10, height=20, width=100)
        self.entry_usr_name = tk.Entry(self.gui)
        self.entry_usr_name.place(x=110, y=10, height=20, width=200)
        self.btn_usr_name = tk.Button(self.gui, text='apply', command=(lambda entry_user=self.entry_usr_name:
                                                                       self.apply_usr_name(entry_user)))
        self.btn_usr_name.place(x=350, y=10, height=20, width=100)

        self.btn_quit = tk.Button(self.gui, text='quit', command=self.close_gui)
        self.btn_quit.place(x=450, y=10, height=20, width=50)

        self.txt_send = tk.Text(self.gui)
        self.txt_send.place(x=0, y=450, height=50, width=500)

        self.txt_rec = tk.Text(self.gui)
        self.txt_rec.place(x=0, y=350, height=100, width=500)

        scroll_1 = tk.Scrollbar(self.txt_send, command=self.txt_send.yview)
        self.txt_send.config(yscrollcommand=scroll_1.set)
        scroll_1.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_2 = tk.Scrollbar(self.txt_rec, command=self.txt_rec.yview)
        self.txt_rec.config(yscrollcommand=scroll_2.set)
        scroll_2.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_rec["state"] = tk.DISABLED

        self.txt_send.bind("<Return>", lambda event, text_send=self.txt_send, text_rec=self.txt_rec:
                                                            self.extract_text(text_send, text_rec))
        self.user_name = ''
        self.video()

    def video(self):

        self.btn_setup = tk.Button(self.gui, text='set up', command=self.setup_func)
        self.btn_setup.place(x=0, y=30, height=20, width=50)

        self.btn_play = tk.Button(self.gui, text='play', command=self.play_func)
        self.btn_play.place(x=100, y=30, height=20, width=50)

        self.btn_pause = tk.Button(self.gui, text='pause', command=self.pause_func)
        self.btn_pause.place(x=200, y=30, height=20, width=50)

        self.btn_stop = tk.Button(self.gui, text='stop', command=self.stop_func)
        self.btn_stop.place(x=300, y=30, height=20, width=50)

        self.text_img = tk.Text(self.gui)
        self.text_img.place(x=0, y=50, height=300, width=500)
        self.img = tk.PhotoImage(file="./tracks.png")
        self.text_img.image_create(tk.END, image=self.img)

    def setup_func(self):
        mess = self.encode_with_header('SETUP')
        self.client.send(bytes(mess), "utf-8")
        pass

    def play_func(self):
        mess = self.encode_with_header('PLAY')
        self.client.send(bytes(mess), "utf-8")
        pass

    def pause_func(self):
        mess = self.encode_with_header('PAUSE')
        self.client.send(bytes(mess), "utf-8")
        pass

    def stop_func(self):
        mess = self.encode_with_header('STOP')
        self.client.send(bytes(mess), "utf-8")
        pass

    def close_gui(self):
        self.Gui__quit = True
        self.gui.quit()

        # @staticmethod
    def apply_usr_name(self, entry_user):
        usr_name = entry_user.get()
        if usr_name != '':
            print(usr_name)
            self.user_name = usr_name
            entry_user["state"] = tk.DISABLED
            mess_header = f"{len(usr_name):<{self.HEADER_SIZE}}"
            self.client.send(bytes(mess_header + usr_name, "utf-8"))

    def extract_text(self, text_send, text_rec):
        try:
            text = text_send.get("1.0", "end")
            if self.debug_log:
                print(f"Debug log: input text is {text}")
            if text[0] == '\n':
                text = text[1:len(text)]
            if text[len(text)-1] == '\n':
                text = text[0:len(text)-1]
            text_send.delete("1.0", "end")
            self.insert_text(text_rec, text, self.user_name)
            self.send_mess(self.client, self.user_name, text)
        except Exception as e:
            print(f"Gui class, extract_text: exception is {e}")

    @staticmethod
    def add_space( num_space, text):
        mes = ''
        for i in range(num_space):
            mes += ' '
        mes += text
        return mes

    def analyze_text(self, text):
        try:
            arr_txt = []
            f = e = 0
            if len(text) > self.max_len_txt_box:
                # if len of text is more than max len of text box, then dive text to small texts and append to arr
                i = self.max_len_txt_box
                while i < len(text)-1:
                    # if the text has space at max len of text box
                    if text[i] == ' ':
                        e = i
                    else:
                        # find the space whose index is less then max len of text box
                        # space's index should be not equal first index
                        while text[i] != ' ' and i != f:
                            i -= 1
                    # cannot find space
                    if i == f:
                        # set end's index to first's index plus max len of text box
                        e = f + self.max_len_txt_box
                        # save text to array
                        arr_txt.append(text[f+1:e] if text[f] == ' ' else text[f:e])
                        # assign first to end, because next index is not space
                        f = e
                    else:
                        # find space, then set end's index to current index
                        e = i
                        # save text to array
                        arr_txt.append(text[f+1:e] if text[f] == ' ' else text[f:e])
                        # assign first to end + 1, because next index is space
                        f = e + 1
                    # increase current index
                    i = f + self.max_len_txt_box
                arr_txt.append(text[f:len(text)])
            else:
                # if len of text is less than max len of text box, then append text to arr
                arr_txt.append(text)
            return arr_txt
        except Exception as e:
            print(f"analyze_text exception is {e}")

    def insert_text(self, text_rec, text, user):
        try:
            # divide text to small texts and contain to array of text
            arr_text = self.analyze_text(text)
            # if len of arr text is 1, it mean that len of mess is less than max len of text box
            if len(arr_text) == 1:
                if self.debug_log:
                    print(f"Debug log: array text is {arr_text}")
                # add space to set mess always in right side
                # num_space = int(len_txt_box-len(arr_text[0]))
                if user == self.user_name:
                    # enable text to insert
                    self.txt_rec["state"] = tk.NORMAL
                    text_rec.insert(tk.END, ChatRoomGui.add_space(int(self.len_txt_box-len(arr_text[0])), arr_text[0]))
                    text_rec.insert(tk.END, '\n')
                    # disable text because showing text instead of getting
                    self.txt_rec["state"] = tk.DISABLED
                else:
                    self.txt_rec["state"] = tk.NORMAL
                    text_rec.insert(tk.END, arr_text[0])
                    text_rec.insert(tk.END, '\n')
                    self.txt_rec["state"] = tk.DISABLED
            # if len of arr text is more than 1, it mean that len of mess is more than max len of text box
            else:
                if self.debug_log:
                    print(f"Debug log: array text is {arr_text}")
                for txt in arr_text:
                    # add space to set mess always in right side
                    # num_space = int(len_txt_box-max_len_txt_box)
                    if user == self.user_name:
                        # enable text to insert
                        self.txt_rec["state"] = tk.NORMAL
                        text_rec.insert(tk.END, ChatRoomGui.add_space(int(self.len_txt_box-self.max_len_txt_box), txt))
                        text_rec.insert(tk.END, '\n')
                        # disable text because showing text instead of getting
                        self.txt_rec["state"] = tk.DISABLED
                    else:
                        self.txt_rec["state"] = tk.NORMAL
                        self.text_rec.insert(tk.END, txt)
                        text_rec.insert(tk.END, '\n')
                        self.txt_rec["state"] = tk.DISABLED
        except Exception as e:
            print(f"insert_text exception is {e}")

    def get_mess_from_server(self):
        while False:
            self.receive_mess(self.Gui__quit)
            if self.rec_bool is True:
                if self.debug_log:
                    print(f"\nDebug log: get_mess_from_server runs")
                    print(f"\nDebug log: mess is {self.mess}")
                self.rec_bool = False
                self.insert_text(self.txt_rec, self.mess, '')
            if self.Gui__quit:
                print(f"\nDebug log: gui quit is {self.Gui__quit}")
                self.Gui__quit = False
                break


if __name__ == "__main__":
    gui = ChatRoomGui(False)
    get_mess = Thread(target=gui.get_mess_from_server)
    get_mess.start()
    gui.gui.mainloop()
    get_mess.join()

global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print
            board[i][j],
        print


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this colum col  then return false
    return False


# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one  of the
# feasible solutions.
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if solveNQUtil(board, 0) == False:
        print
        "Solution does not exist"
        return False

    printSolution(board)
    return True


# driver program to test above function
solveNQ()

# This code is contributed by Divyanshu Mehta