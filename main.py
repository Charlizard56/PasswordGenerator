from tkinter import*
import Create

root = Tk()

# Variables
t = False
s = False
n = False
low = False
upp = False
password = "Insert Length of characters above ^"

##Methods############################
#####################################

def gen_password():
    try:
        # Get Entry
        size = Size_Entry.get()
        # Set Entry to int
        s = int(size)
        if(s > 7 and s < 25):
            try:
                # Set Gen Button to Disabled
                dis()
                # Update Gen Button
                Generate_Button.update()
                print("Gen Started...")
                # Delete Entry Bar
                Password_Entry.delete(0, "end")
                password = Create.create(s, t, s, n, low, upp)
                # Insert new password string
                Password_Entry.insert(END, password)
                # Copy to clipboard
                try:
                    root.clipboard_clear()
                    root.clipboard_append(password)
                    Show_Copied.place(x=56, y=56)
                except:
                    print("Failed to copy to clipboard")
            except:
                Password_Entry.delete(0, "end")
                Password_Entry.insert(END, "Failed to generate")
                dis()
            finally:
                dis()
                print("Gen_Password Finished")
        else:
            print("Size not correct")
            Password_Entry.delete(0, "end")
            Password_Entry.insert(END, "Size MUST be 8-24 characters")
    except:
        print("Size not correct")
        Password_Entry.delete(0, "end")
        Password_Entry.insert(END, "Size MUST be a Integer")
    finally:
        print("End")


def dis():
    if Generate_Button["state"] == NORMAL:
        Generate_Button["state"] = DISABLED
        Generate_Button["text"] = "Generating"
        Generate_Button["bg"] = "Pink"
    else:
        Generate_Button["state"] = NORMAL
        Generate_Button["text"] = "Generate"
        Generate_Button["bg"] = "LightGreen"

##SET#########################################
##############################################


##Title#######################################


root.title("CL's Password Generator")

##Window######################################

root.geometry('338x80+700+200')

##Label Widget################################


My_Label = Label(root, text="Password: ")
Size_Label = Label(root, text="Size: ")
Size_Instructions = Label(root, text="<== Character length: 8-24")
Show_Copied = Label(root, text="Copied to Clipboard",fg="Green")

##Button#####################################


Generate_Button = Button(root, text="Generate", bg="LightGreen", width=10,height=4,bd=4, command=(lambda: gen_password()))

##Entry Widget###############################


Password_Entry = Entry(root, bd=4, width=30)
Size_Entry = Entry(root, bd=5, width=2)


###Draw to Screen############################
#############################################

##Buttons####################################


Generate_Button.place(x=250,y=2)

##Labels####################################


My_Label.place(x=0,y=32)
Size_Label.place(x=0,y=2)
Size_Instructions.place(x=70,y=2)
Show_Copied.place_forget()

##Entries##################################


Password_Entry.place(x=60,y=30)
Size_Entry.place(x=40,y=2)


##MainLoop################################

root.mainloop()
