from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x900+0+0")

        # Create a canvas for the background image
        self.bg = ImageTk.PhotoImage(file="D:\\Downloads\\pexels-thisisengineering-3861969.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #===============left image=============
        self.left = ImageTk.PhotoImage(file="D:\\Downloads\\artificial-intelligence-brain-circuitry.jpg")
        left_lbl = Label(self.root, image=self.left)
        left_lbl.place(x=50, y=100, width=470, height=500)

        #====================== main Frame===========
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=500)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        #===================label and entry==============
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=20, y=70)

        self.txt_fname = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_fname.place(x=20, y=100, width=250)

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()