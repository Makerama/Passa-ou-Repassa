from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.str_placar = StringVar()

        self.makerama = Label(frame, text="Makerama\nPassa ou Repassa", anchor=CENTER, fg = "blue", justify=CENTER, font=("Helvetica", 60))
        self.makerama.configure(background='white')
        self.makerama.pack()

        self.placar = Label(frame, textvariable=self.str_placar, anchor=CENTER, fg = "blue", justify=CENTER, font=("Helvetica", 150))
        self.placar.pack()

        self.str_placar.set('0x0')

    def add_point(self, side):
        self.str_placar.set('Add ' + side)
        print('Add ' + side)
        
    def remove_point(self, side):
        self.str_placar.set('Remove ' + side)
        print('Remove ' + side)
        
root = Tk()
root.title = "Makerama"
root.configure(background='white')

root.focus_set() # <-- move focus to this widget

app = App(root)

root.mainloop()
root.destroy()
