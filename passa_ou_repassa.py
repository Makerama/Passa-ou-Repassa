from tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.str_placar = StringVar()

        self.makerama = Label(frame, text="Makerama\nPassa ou Repassa", anchor=CENTER, fg = "blue", justify=CENTER, font=("Helvetica", 60))
        self.makerama.configure(background='white')
        self.makerama.pack()

        self.placar = Label(frame, textvariable=self.str_placar, anchor=CENTER, fg = "blue", justify=CENTER, font=("Helvetica", 350))
        self.placar.pack()

        self.add_left = Button(frame, text = "+", command = lambda: self.add_point('left'))
        self.add_left.pack(side = LEFT)

        self.remove_left = Button(frame, text = "-", command = lambda: self.remove_point('left'))
        self.remove_left.pack(side = LEFT)

        self.add_right = Button(frame, text = "+", command = lambda: self.add_point('right'))
        self.add_right.pack(side = LEFT)

        self.remove_right = Button(frame, text = "-", command = lambda: self.remove_point('right'))
        self.remove_right.pack(side = LEFT)

        self.button = Button(frame, text = "Sair", fg = "red", command = frame.quit)
        self.button.pack(side = RIGHT)

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

#fullscrean
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

#set focus
root.focus_set() # <-- move focus to this widget

#Esc to exit
root.bind("<Escape>", lambda e: e.widget.quit())

app = App(root)

root.mainloop()
root.destroy()
