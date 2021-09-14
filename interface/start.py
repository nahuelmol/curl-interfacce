import tkinter as tk
import os
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.final_string = ""
        self.error = ""

    def create_widgets(self):

        self.data_label = tk.Label(self, text="Data").pack()
        self.data   = tk.Entry(self)
        self.data.pack(side="top")        

        self.method_label = tk.Label(self, text="Method").pack()
        self.method = tk.Entry(self)
        self.method.pack(side="top")

        self.url_label = tk.Label(self, text="Url").pack()
        self.url    = tk.Entry(self)
        self.url.pack(side="top")

        self.send = tk.Button(self)
        self.send["text"] = "send"
        self.send["command"] = self.execute_command
        self.send.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def getdata(self):
            if self.data.get():
                data    = ' -d '+ self.data.get()
                return data

    def execute_command(self):

        url     = ' '+self.url.get()+' '
        method  = ' -X '+ self.method.get()+' '
        data    = self.getdata()

        if self.method.get() == 'POST':
            if self.data.get():
                self.final_string = 'curl '+ data +method+url
                result = os.system(self.final_string)

                tk.Label(self, 
                    text="sended",
                    bg='#fff', fg='green').pack()

                return print(result)

            else:
                return tk.Label(self, 
                    text="You have to insert data, due this is a POST method",
                    bg='#fff', fg='#f00').pack()



if __name__ == "__main__":
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == "interface.start":

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()