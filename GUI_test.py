from tkinter import *
import tkinter.messagebox as tm
from time import sleep

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.text_label = Label(self, text="Enter your Facebook Login information")
        self.label_username = Label(self, text="Email")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.text_label.grid(row=0, column=1)
        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.logbtn = Button(self, text="Go", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()
        # print(username, password)

        if username != "" and password != "":
            sleep(0)
            #tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Learn to type fgt")

        root.destroy()
        
root = Tk()
lf = LoginFrame(root)
root.mainloop()
