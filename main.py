import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Транслитератор')
        self.FONT = 'Helvetica 10 bold'
        self.geometry('1200x700')
        self.frames()

    def frames(self):
        self.labels_frame()
        self.btns_frame()
        self.frame_editor()
        self.result_frame()

    def labels_frame(self):
        frame = tk.Frame(self, height=30, width=1000, bg='#A9A9A9')
        frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        l_btn = tk.Label(master=frame, text='Кнопочки', bg='#A9A9A9', font=self.FONT)
        l_btn.place(relx=0.08, rely=0.2)
        l_editor = tk.Label(master=frame, text='Редактор-Транслитатор-Экстерминатор', bg='#A9A9A9', font=self.FONT)
        l_editor.place(relx=0.6, rely=0.2)

    def btns_frame(self):
        frame = tk.Frame(self, height=670, width=300, bg='#C0C0C0')
        frame.place(relx=0, rely=0.05, relwidth=0.2, relheight=1)
        btn1 = tk.Button(master=frame, text='Кнопочка1',
                            bg='#FF69B4', fg='#00FF00', activebackground='#00BFFF', font=self.FONT,
                            activeforeground='#FF0000')
        btn1.place(relx=0.3, rely=0.6)
        btn2 = tk.Button(master=frame, text='Кнопочка2',
                           bg='#00FF00', fg='#C71585', activebackground='#FFFF00', font=self.FONT,
                           activeforeground='#FF0000')
        btn2.place(relx=0.5, rely=0.4)

    def frame_editor(self):
        frame = tk.Frame(self, height=240, width=700)
        frame.place(relx=0.2, rely=0.05, relwidth=0.8, relheight=0.45)
        query = tk.Text(master=frame)
        query.place(relx=0, rely=0, relwidth=1)

    def result_frame(self):
        frame = tk.Frame(self, height=240, width=700)
        frame.place(relx=0.2, rely=0.5, relwidth=0.8, relheight=0.5)
        query = tk.Text(master=frame)
        query.place(relx=0, rely=0, relwidth=1)


window = Window()
window.mainloop()
