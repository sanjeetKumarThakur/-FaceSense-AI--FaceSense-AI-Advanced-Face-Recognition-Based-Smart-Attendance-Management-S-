from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x900+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file="D:\\Downloads\\pexels-thisisengineering-3861969.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left image
        self.left = ImageTk.PhotoImage(file="D:\\Downloads\\artificial-intelligence-brain-circuitry.jpg")
        left_lbl = Label(self.root, image=self.left)
        left_lbl.place(x=50, y=100, width=470, height=500)

        # Main Frame
        frame= Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=500)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=20, y=70)
        self.txt_fname = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_fname.place(x=20, y=100, width=250)

        # Last Name
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname.place(x=400, y=70)
        self.txt_lname = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_lname.place(x=400, y=100, width=250)

        # Contact No
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=20, y=150)
        self.txt_contact = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_contact.place(x=20, y=180, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=400, y=150)
        self.txt_email = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_email.place(x=400, y=180, width=250)

        # Security Question
        security_q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_q.place(x=20, y=230)
        self.combo_security_q = ttk.Combobox(frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_q["values"] = ("Select", "Your Birth Place", "Your Best Friend", "Your Pet Name")
        self.combo_security_q.current(0)
        self.combo_security_q.place(x=20, y=260, width=250)

        # Security Answer
        security_a = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_a.place(x=400, y=230)
        self.txt_security_a = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        self.txt_security_a.place(x=400, y=260, width=250)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=20, y=310)
        self.txt_password = Entry(frame, font=("times new roman", 15, "bold"), bg="white", show="*")
        self.txt_password.place(x=20, y=340, width=250)

        # Confirm Password
        cpassword = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        cpassword.place(x=400, y=310)
        self.txt_cpassword = Entry(frame, font=("times new roman", 15, "bold"), bg="white", show="*")
        self.txt_cpassword.place(x=400, y=340, width=250)

        #=========================checkbutton==============
        checkbtn=Checkbutton(frame, text="I Agree The Terms & Conditions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        checkbtn.place(x=50, y=380)

        #==================== buttons===============
        img=Image.open(r"image/artificial-intelligence-brain-circuitry.jpg")
        img=img.resize((100, 50), Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=10, y=420, width=200)


         #==================== login button===============
        img1=Image.open(r"image/reset-password-icon-29.jpg")
        img1=img1.resize((200, 40), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=10, y=420, width=300)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()