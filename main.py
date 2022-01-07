from tkinter import*
import Create

root = Tk()

#Variables
t = False
times = 12
s = False
n = False
low = False
upp = False
password = ""

def Gen_Password():
    print("Gen Started...")
    password = Create.create(times,t,s,n,low,upp)
    Password_Entry.insert(END, password)

# Set Title
root.title("Chars Password Generator")

# Label Widget
My_Label = Label(root, text="Password: ")

#Button
Generate_Button = Button(root, text="Generate",bg="LightGreen",width=26,command=Gen_Password)

# Entry Widget
Password_Entry = Entry(root, bd=4)


# Add to Screen
Generate_Button.pack(side=TOP)
My_Label.pack(side=LEFT)
Password_Entry.pack(side=RIGHT)


root.mainloop()
