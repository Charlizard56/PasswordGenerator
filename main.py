from tkinter import*
import Create

root = Tk()

# Variables
t = False
s = False
n = False
low = False
upp = False
password = ""

##Methods############################


def gen_password():
    try:
        # Get Entry
        size = Size_Entry.get()
        # Set Entry to int
        s = int(size)

        dis()
        Generate_Button.update()
        print("Gen Started...")
        Password_Entry.delete(0, "end")
        password = Create.create(s, t, s, n, low, upp)
        Password_Entry.insert(END, password)
    except:
        Password_Entry.delete(0, "end")
        Password_Entry.insert(END, "Failed to generate")
        dis()
    finally:
        dis()
        print("Gen_Password Finished")


def dis():
    if Generate_Button["state"] == NORMAL:
        Generate_Button["state"] = DISABLED
        Generate_Button["text"] = "Generating"
        Generate_Button["bg"] = "Pink"
    else:
        Generate_Button["state"] = NORMAL
        Generate_Button["text"] = "Generate"
        Generate_Button["bg"] = "LightGreen"

##Set Title###################################


root.title("CL's Password Generator")


# Label Widget


My_Label = Label(root, text="Password: ")

# Button


Generate_Button = Button(root, text="Generate", bg="LightGreen", width=25, command=(lambda: gen_password()))

# Entry Widget


Password_Entry = Entry(root, bd=4, width=30)
Size_Entry = Entry(root, bd=5, width=2)

###Add to Screen###########################
# Buttons


Generate_Button.grid(column=1,row=0)

# Labels


My_Label.grid(column=0,row=1)

# Entries
Password_Entry.grid(column=1,row=1)
Size_Entry.grid(column=0,row=0)

root.mainloop()
