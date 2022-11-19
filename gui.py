import secrets
import string
from tkinter import *
from tkinter import ttk
import tkinter as tk
import runner as runner

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Python Tkinter")
        self.minsize(500,400)
 

 
 
root = Root()

   
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

tk.Label(tab1, text = "Store Credentials", font=("Arial", 25)).place(x = 40, y = 30)
# the label for user_name
Label(tab1,
                  text = "Username").place(x = 40,
                                           y = 80) 
   
# the label for user_password 
Label(tab1, text="Password").place(x=40, y=100)
Label(tab1, text="Domain").place(x=40, y=120)

user_text = Entry(tab1,name="user_text",  width=20)
user_text.unbind('<Return>')
user_text.place(x=120, y=80)
pass_text =Entry(tab1,name="pass_text", width=20)
pass_text.unbind('<Return>')
pass_text.place(x=120, y=100)
host_text = Entry(tab1,name="host_text",  width=20)
host_text.place(x=120, y=120)


store_submit_button = Button(tab1,
                             text = "Submit",
                             command=lambda:
                             runner.store_credentials(user_text.get(), pass_text.get(), host_text.get()))

store_submit_button.place(x=40, y=150)
   


######## GET #############
printText = tk.StringVar()
printInfo = Entry(tab1, width=50, textvariable=printText, name="info", state=DISABLED)
printInfo.place(x=90, y=240)


def output():
    printText.set(runner.get_credentials(domain_text.get()))


get_cred_label = Label(tab1, text = "Get Credentials", font=("Arial", 25))
get_cred_label.place(x = 40, y = 180)

nameToGet = Label(tab1,
                  text = "Host")
nameToGet.place(x = 40, y = 220)

domain_text = Entry(tab1,name="domain_text", width=20)
domain_text.place(x=120, y= 220)

get_submit_button = Button(tab1, text = "Submit", command=output)
get_submit_button.place(x = 40, y = 240)



specialCharFlag = False

#name_entry = Entry(root,textvariable = hostname_var, font=('calibre',10,'normal'))

hostname_var=StringVar()
#passw_var=tk.StringVar()
#Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

Label(tab2, text="Host Name :").place(x=40, y=100)
hostName = Entry(tab2, name="host_name", font=('calibre', 10, 'normal'))
hostName.place(x=120, y=100)

Label(tab2, text="Username  :").place(x=40, y=120)
username_var = ""
userName = Entry(tab2, name = "user_text", font=('calibre', 10, 'normal'))
userName.place(x=120, y=120)

c1 = Checkbutton(tab2, text="Special Characters",variable=specialCharFlag, onvalue=1, offvalue=0)


def generate_password(username, hostname):
    if specialCharFlag:
        generated_password = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits) for i in range(7)))
    else:
        generated_password = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(7)))

    if len(hostname) > 0:
        runner.store_credentials(username, generated_password, hostname)
        Label(tab2, text=("Password: " + generated_password), font=("Arial", 25)).place(x=40, y=160)


generatePasswordButton = Button(tab2, text="Generate", command=lambda: generate_password(str(userName.get()), str(hostName.get())))
generatePasswordButton.place(x=40, y=140)

root.mainloop()
