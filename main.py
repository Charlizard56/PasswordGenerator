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
        Password_Entry.insert(END, "Size MUST be a integer")
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


##Label Widget###############################


My_Label = Label(root, text="Password: ")

##Button#####################################


Generate_Button = Button(root, text="Generate", bg="LightGreen", width=25, command=(lambda: gen_password()))

##Entry Widget##############################


Password_Entry = Entry(root, bd=4, width=30)
Size_Entry = Entry(root, bd=5, width=2)


###Draw to Screen############################
############################################

##Buttons###################################


Generate_Button.grid(column=1,row=0)

##Labels###################################


My_Label.grid(column=0,row=1)


##Entries#################################


Password_Entry.grid(column=1,row=1)
Size_Entry.grid(column=0,row=0)


##MainLoop###############################

root.mainloop()
