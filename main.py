import time
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
    try:
        Dis()
        Generate_Button.update()
        print("Gen Started...")
        Password_Entry.delete(0,"end")
        password = Create.create(times,t,s,n,low,upp)
        Password_Entry.insert(END, password)
    except:
        Password_Entry.insert(END, "Failed to generate")
    finally:
        time.sleep(2)
        Dis()
        print("Gen_Password Finished")

def Dis():
    if Generate_Button["state"] == NORMAL:
        Generate_Button["state"] = DISABLED
        Generate_Button["text"] = "Generating"
        Generate_Button["bg"] = "Pink"
    else:
        Generate_Button["state"] = NORMAL
        Generate_Button["text"] = "Generate"
        Generate_Button["bg"] = "LightGreen"
# Set Title
root.title("CL's Password Generator")

# Label Widget
My_Label = Label(root, text="Password: ")

#Button
Generate_Button = Button(root, text="Generate",bg="LightGreen",width=26,command=(lambda: Gen_Password()))

# Entry Widget
Password_Entry = Entry(root, bd=4)


# Add to Screen
Generate_Button.pack(side=TOP)
My_Label.pack(side=LEFT)
Password_Entry.pack(side=RIGHT)


root.mainloop()
