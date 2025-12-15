from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1550x800")

        self.bg = PhotoImage(file=r"D:/0df675008d1b42f693786ddcd4e2fe22.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"D:\Downloads\contact-image-icon-11.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
#label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
         

        Password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        Password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        #===============ICOn image======================
        img2=Image.open(r"D:\Downloads\contact-image-icon-11.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        
        img3=Image.open(r"D:\Downloads\icons8-password-48.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
 


# loginButton

        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerButton
        registerbtn=Button(frame,text="New User Register",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="red")
        registerbtn.place(x=20,y=350,width=160)


        #forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="red")
        registerbtn.place(x=20,y=350,width=160)



if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root) 
    root.mainloop()