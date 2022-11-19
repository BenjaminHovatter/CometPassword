from tkinter import *
from tkinter import ttk
import runner

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

store_cred_label = Label(tab1, text = "Store Credentials", font=("Arial", 25)).place(x = 40, y = 30) 
# the label for user_name
user_name = Label(tab1,
                  text = "Username").place(x = 40,
                                           y = 80) 
   
# the label for user_password 
user_password = Label(tab1,
                      text = "Password").place(x = 40,
                                               y = 100) 
   
store_submit_button = Button(tab1,
                       text = "Submit").place(x = 40,
                                              y = 130)
   


######## GET #############
get_cred_label = Label(tab1, text = "Get Credentials", font=("Arial", 25)).place(x = 40, y = 160) 
# the label for user_name
nameToGet = Label(tab1,
                  text = "Host").place(x = 40, y = 200)

get_submit_button = Button(tab1, text = "Submit").place(x = 40, y = 220)

specialCharFlag = False

#name_entry = Entry(root,textvariable = hostname_var, font=('calibre',10,'normal'))

hostname_var=StringVar()
#passw_var=tk.StringVar()
#Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
hostName = Entry(tab2,textvariable = hostname_var, font=('calibre',10,'normal')).place(x = 40, y = 100)
genUsernameBox = Text(tab2, height = 5, width =  52).place(x = 40, y = 120)

c1 = Checkbutton(tab2, text="Special Characters",variable=specialCharFlag, onvalue=1, offvalue=0)
c1.pack()

generatedPassword = ""
def generatePassword():
    genHostSite = hostName.get("1.0", END)  # For line 1, col 0 to end.


    if(specialCharFlag == True):
        generatedPassword = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits) for i in range(7)))
    else:
        generatedPassword = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(7)))

    
    if(genHostSite != ""):

#        print(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7)))

        runner.store_credentials(genUser_Name, generatedPassword, genHostSite)

        genPassLabel = Label(tab2, text = ("Password: " + generatedPassword), font=("Arial", 25)).place(x = 40, y = 160) 


generatePasswordButton = Button(tab2, text = "Generate", command=generatePassword).place(x = 50, y = 80)

root.mainloop()