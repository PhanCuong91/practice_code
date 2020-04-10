import tkinter as tk


def extract_text(text_send, text_rec):
    text = text_send.get("1.0", "end-1c")
    text_rec.insert(tk.END, text)
    text_send.delete("1.0", tk.END)
    text_send.mark_set("insert", "insert-1c")
    print(text_send.index(tk.CURRENT))
    # text_send.insert(tk.END,'')

gui = tk.Tk()
gui.title('hello')
gui.geometry("500x500")

txt_1 = tk.Text(gui)
txt_1.place(x=0, y=400, height=50, width=150)
txt_2 = tk.Text(gui)
txt_2.place(x=0, y=0, height=100, width=500)
scroll_1 = tk.Scrollbar(txt_1, command=txt_1.yview)
txt_1.config(yscrollcommand=scroll_1.set)
scroll_1.pack(side=tk.RIGHT, fill=tk.Y)
scroll_2 = tk.Scrollbar(txt_2, command=txt_2.yview)
txt_2.config(yscrollcommand=scroll_2.set)
scroll_2.pack(side=tk.RIGHT, fill=tk.Y)
txt_1.bind("<Return>", lambda event, text_send=txt_1, text_rec=txt_2: extract_text(text_send, text_rec))

gui.mainloop()