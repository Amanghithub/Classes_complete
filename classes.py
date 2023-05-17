from tkinter import *
from tkinter import messagebox

from tkinter import ttk

root = Tk()
root.title("Classes")
root.geometry("400x400")

lbl_name = Label(root,text="Enter Name:  ")
lbl_name.place(relx=0.2,rely=0.2,anchor=CENTER)

name_entry = Entry(root)
name_entry.place(relx=0.5,rely=0.2,anchor=CENTER)

lbl_age = Label(root,text="Enter Age:  ")
lbl_age.place(relx=0.2,rely=0.4,anchor=CENTER)

age_entry = Entry(root)
age_entry.place(relx=0.5,rely=0.4,anchor=CENTER)

lbl_height = Label(root,text="Enter Height:  ")
lbl_height.place(relx=0.2,rely=0.6,anchor=CENTER)

height_entry = Entry(root)
height_entry.place(relx=0.5,rely=0.6,anchor=CENTER)

lbl_gender = Label(root,text="Enter Gender:  ")
lbl_gender.place(relx=0.2,rely=0.8,anchor=CENTER)

gender = ["Male","Female","Other"]

gender_entry = ttk.Combobox(root,state="readonly",values=gender)
gender_entry.place(relx=0.5,rely=0.8,anchor=CENTER)


name_get = ""
age_get = ""
height_get = ""
gender_get = ""

class citizen:
    def __init__(self,name,age,height,gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
    
    def addCitizen(self):
        
        global name_get
        global age_get
        global height_get
        global gender_get
        
        name_get = name_entry.get()
        age_get = age_entry.get()
        height_get = height_entry.get()
        gender_get = gender_entry.get()
        
        #lbl_name[text]="Name: "+self.name
        print("Name: "+name_get)
        print("Age: "+str(age_get))
        print("Height: "+str(height_get))
        print("Gender: "+gender_get)
        
        messagebox.showinfo("Info","Citizen Added")
        

citizen1 = citizen(name_get,age_get,height_get,gender_get)
#citizen1.addCitizen()

btn = Button(root,text="Add",command=citizen1.addCitizen)

btn.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()