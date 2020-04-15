import tkinter as tk
from client import Client
from threading import Thread


class ChatRoomGui(Client):

    def __init__(self):
        super().__init__()
        self.max_len_txt_box = 40
        self.len_txt_box = 60
        self.gui = tk.Tk()
        self.gui.title('hello')
        self.gui.geometry("500x500")

        self.label_usr_name = tk.Label(self.gui, text="user name")
        self.label_usr_name.place(x=10, y=10, height=20, width=100)
        self.entry_usr_name = tk.Entry(self.gui)
        self.entry_usr_name.place(x=110, y=10, height=20, width=200)
        self.btn_usr_name = tk.Button(self.gui, text='apply', command=(lambda entry_user=self.entry_usr_name:
                                                                       self.apply_usr_name(entry_user)))
        self.btn_usr_name.place(x=350, y=10, height=20, width=100)

        self.txt_send = tk.Text(self.gui)
        self.txt_send.place(x=0, y=400, height=50, width=500)

        self.txt_rec = tk.Text(self.gui)
        self.txt_rec.place(x=0, y=100, height=300, width=500)

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

        menubar = tk.Menu(self.gui)
        file = tk.Menu(menubar, tearoff=0)
        file.add_command(label="Exit", command=self.gui.quit)
        self.gui.config(menu=menubar)

        # @staticmethod
    def apply_usr_name(self, entry_user):
        usr_name = entry_user.get()
        print(f"press button")
        if usr_name != '':
            print(usr_name)
            self.user_name = usr_name
            entry_user["state"] = tk.DISABLED
            mess_header = f"{len(usr_name):<{self.HEADER_SIZE}}"
            self.client.send(bytes(mess_header + usr_name, "utf-8"))

    def extract_text(self, text_send, text_rec):
        try:
            text = text_send.get("1.0", "end")
            print(f"input text is {text}")
            if text[0] == '\n':
                text = text[1:len(text)]
            if text[len(text)-1] == '\n':
                text = text[0:len(text)-1]
            print(f"remove new line in text")
            text_send.delete("1.0", "end")
            self.insert_text(text_rec, text, self.user_name)
            self.send_mess(self.client, self.user_name, text)
        except Exception as e:
            print(f"extract_text exception is : {e}")

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
                print(f"array text is {arr_text}")
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
        while True:
            if self.rec_bool is True:
                print(f"\n get_mess_from_server runs")
                self.rec_bool = False
                self.insert_text(self.txt_rec, self.mess, '')
                print(f"mess is {self.mess}")


if __name__ == "__main__":
    gui = ChatRoomGui()
    Thread(target=gui.receive_mess, args=(gui.client,)).start()
    Thread(target=gui.get_mess_from_server).start()
    gui.gui.mainloop()
    # gui.mainloop()
