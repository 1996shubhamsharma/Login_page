# username = shubham, password =1996shubu
#username = sakshi , password = 1996sakshi
from tkinter import *
from PIL import ImageTk,Image
import pdbc as p
from tkinter import messagebox
window = Tk()#Making window 
class Login_System:
	def __init__(self,window):#accepting the window object
		self.window=window#creating object of window
		self.window.title("Login System")#title of window
		self.window.geometry("1008x1722+0+0")#pixel of window or size of window and x,y coordinates 
		self.usnname=StringVar() #you need to pass it to the entry field of username
		self.passwrd = StringVar()#you need to pass it to the entry field of password
		
		#creating lables

		self.bg_image = ImageTk.PhotoImage(file="backgrnd.png")
		self.icon = ImageTk.PhotoImage(file="icon.png")
		#open the image using Image 
		open_usn = Image.open("usn.png")
		#resize the image using Image and use ANTIALIAS to avoid rugged corners
		resize_usn = open_usn.resize((20,20),Image.ANTIALIAS)
		#read the image using PIL
		self.usn= ImageTk.PhotoImage(resize_usn)

		#open password image
		pswd_open = Image.open("lock.png")
		#resize the ia pswd image
		resize_pswd = pswd_open.resize((20,20),Image.ANTIALIAS)
		#read the image usinh PIL
		self.password = ImageTk.PhotoImage(resize_pswd)
		
				#creating lable for bg image and packing it
		bg_image=Label(self.window,image =self.bg_image)
		bg_image.pack()

		#creating lable for title and placing it
		title=Label(self.window,text="Login System",font=("times new roman",40,"bold"),bg="yellow",bd=10,relief=GROOVE)
		title.place(x=0,y=0,relwidth=1)

		#creating a frame and providing by giving window object and background color
		Login_Frame = Frame(self.window,bg="white")
		Login_Frame.place(x=290,y=100)
		
		#using Frame creating icon and providing its pace using grid, here pady=0 means no extended area around icon.
		icon= Label(Login_Frame,image=self.icon)
		icon.grid(columnspan=2,row=0,pady=20,padx=20)#columnspan = 2 will keep icon between clm=0 and clm=2

		#using frame creating usn 
		usn = Label(Login_Frame,image=self.usn,text="Username",compound=LEFT,font=("times new roman",20,"bold"),bg="white")
		usn.grid(column=0,row=2,pady=20,padx=20)

		#using frame create password 
		pswrd = Label(Login_Frame,image=self.password,text="password",font=("times new roman",20,"bold"),compound=LEFT,bg="white")
		pswrd.grid(column=0,row=3,pady=20,padx=20)
		
		#creating input field
		txtusn = Entry(Login_Frame,bd=5,font=("times new roman",20),textvariable=self.usnname.get)#pass self.ussname to get input
		txtusn.grid(column=1,row=2,pady=20,padx=30)

		#create entry for password
		txtpswrd = Entry(Login_Frame,bd=5,font=("times new roman",20),textvariable=self.passwrd)#pass self.passwrd to get input
		txtpswrd.grid(column=1,row=3,padx=30,pady=20)

		p.read_record()#you need to call it prior to the validation function and submit button otherwise youll get empty password_lst

		# creating submit button
		submit = Button(Login_Frame,font=("times new roman",20),text="Submit",bd=5,command=self.validate)
		submit.grid(column=0,row=5,pady=30)

		
		

	def validate(self): 
			if(self.passwrd.get() in p.password_lst):
				messagebox.showinfo("login","you are logged In")
			else:
				messagebox.showerror("Error","Invalid Password or Username")
					



if __name__ =="__main__":
	login = Login_System(window)#passing window object to the constructor of class 
	window.mainloop()#making infinite loop to run window 
	
	
	

