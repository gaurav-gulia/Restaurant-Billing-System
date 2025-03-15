from tkinter import *
from tkinter import ttk
import random
from tokenize import String
from datetime import datetime
from tkinter import messagebox
import sys


#Creating a Tk() window,Instantiates the LoginPage class.,Calls mainloop() to run the application.
def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()

#initializing the login page
class LoginPage:
    def __init__(self,win):
        self.win=win                                                                              #Setting Up the Window
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label=Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)   #Title Label
        self.title_label.pack(side=TOP,fill=X)
        self.main_frame=Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)                    #Creating the Main Frame that holds all the login widgets
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans-serif',25,'bold'))    #Displaying a Login label
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame=LabelFrame(self.main_frame,text="Enter details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))   #This LabelFrame contains input fields
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl=Label(self.entry_frame,text="Enter Username: ",bg="lightgrey",font=('sans-serif',15))               #Username & Password Fields
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)

        #===========================Variables=========================================================================================================

        username=StringVar()
        password=StringVar()

        #=============================================================================================================================================
        self.entus_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.entpass_lbl = Label(self.entry_frame, text="Enter Password: ", bg="lightgrey", font=('sans-serif', 15))
        self.entpass_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.entpass_ent = Entry(self.entry_frame, font=('sans-serif', 15),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1, column=1, padx=2, pady=2)
        #======================Functions=================================================

        def check_login():                                             #this function will check logic
            if username.get()=="gaurav" and password.get()=="1234":
                self.billing_btn.config(state="normal")
            else:
                pass    #--> message box
        def reset():
            username.set("")
            password.set("")

        def billing_sect():                                           #Billing Section
            self.newWindow=Toplevel(self.win)
            self.app=Window2(self.newWindow)

        #======================Buttons===============================================================================================================

        #Login, Billing & Reset Buttons

        self.button_frame=LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn=Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame, text="Billing", font=('Arial', 15), bd=5, width=15,command=billing_sect)
        self.billing_btn.grid(row=0, column=1, padx=20, pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame, text="Reset", font=('Arial', 15), bd=5, width=15,command=reset)
        self.reset_btn.grid(row=0, column=2, padx=20, pady=2)

        #=============================================================================================================================================

class Window2:                                    #Window2 Class (Billing System),Creates a new Tkinter window for billing
    def __init__(self,win):
        self.win=win
        self.win.geometry("1300x750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label = Label(self.win, text="Restaurant Management System", font=('Arial', 35, 'bold'),bg="lightgrey", bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        self.win.resizable(0,0)

        #==================Varibles=================================================================================================================

        bill_no=random.randint(100,9999)                  #Random Bill Number
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)

        calc_var=StringVar()

        #Entry Fields for Billing,Stores user input related to the bill.
        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()
        date_pr.set(datetime.now())

        total_list=[]
        self.grd_total=0
        #==================================================================================================================================================


        #=====================================ENTRY========================================================================================================

        # Create a LabelFrame widget to contain the entry fields for the bill details
        self.entry_frame=LabelFrame(self.win,text="Enter details",background="lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        # Label and entry field for Bill Number
        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number ",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent=Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,font=('Arial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        # Label and entry field for Customer Name
        self.cust_nm_lbl=Label(self.entry_frame,text="Customer Name ",font=('Arial',15),bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent=Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)


        self.cust_cot_lbl=Label(self.entry_frame,text="Customer Contact ",font=('Arial',15),bg="lightgrey")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent=Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Arial',15))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl=Label(self.entry_frame,text="Date ",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl=Label(self.entry_frame,text="Item Purchased ",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent=Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl=Label(self.entry_frame,text="Item Quantity ",font=('Arial',15),bg="lightgrey")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent=Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame, text="Cost of one ", font=('Arial', 15), bg="lightgrey")
        self.cost_one_lbl.grid(row=6, column=0, padx=2, pady=2)

        self.cost_one_ent = Entry(self.entry_frame, bd=5, textvariable=cone, font=('Arial', 15))
        self.cost_one_ent.grid(row=6, column=1, padx=2, pady=2)

        #==========================Functions===============================================================================================================

        # Inserts default header for the bill (Restaurant Name, Address, Contact Info)
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tGaurav Restaurant")
            self.bill_txt.insert(END,"\n\t\t\t7 Street, Near Railway Lines, Badaun")
            self.bill_txt.insert(END,"\n\t\t\t    Contact - +919845228457")
            self.bill_txt.insert(END,"\n============================================================================")
            self.bill_txt.insert(END,f"\nBill Number {bill_no_tk.get()}")

        def genbill():
            # Checks if customer details are entered properly
            if cust_nm.get()=="" or (cust_cot.get()=="" or len(cust_cot.get())!=10):
                messagebox.showerror("Error!","Please enter all the fields correctly.")
            else:
                #Inserts customer details and bill header into the bill text area
                self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END,"\n============================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t        Quantity        \t\tPer Cost\t\t        Total")
                self.bill_txt.insert(END,"\n============================================================================")

                self.add_btn.config(state="normal")              ## Enables buttons for adding items and calculating total
                self.total_btn.config(state="normal")

        def clear_func():                             # Clears all input fields to reset the form
            cust_nm.set("")                            #Clear customer name
            cust_cot.set("")                           #Clear customer contact
            item_pur.set("")                           #Clear product name
            item_qty.set("")                           #Clear quantity
            cone.set("")                               #Clear product price

        def reset_func():                                    # Resets everything, clearing the bill content and disabling buttons
            total_list.clear()                                    # Clears the list of total item costs
            self.grd_total=0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)               # Clears the bill text area
            default_bill()                                # Calls the default_bill function to display default header

        def add_func():
            # Adds a product item to the bill
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error!", "Please enter all the fields correctly.",parent=self.win)
            else:
                qty= int(item_qty.get())
                cones= int(cone.get())           # Converts entered per item cost to integer
                total=qty*cones                  # Calculates total cost for the item
                total_list.append(total)         # Adds the total cost to the total list
                self.bill_txt.insert(END,f"\t\t{item_pur.get()}\t\t        {item_qty.get()}\t\t          Rs. {cone.get()}\t\t          Rs. {total}")

        def total_func():
            # Calculates the grand total for all items and inserts it into the bill
            for item in total_list:
                self.grd_total=self.grd_total+item                   # Adds each item total to the grand total
            self.bill_txt.insert(END,f"\n============================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\tGrand Total : Rs. {self.grd_total}")
            self.bill_txt.insert(END,f"\n============================================================================")
            self.save_btn.config(state='normal')                     # Enables the "Save Bill" button

        def save_func():
            # Saves the bill content to a text file
            user_choice=messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no_tk.get()}",parent=self.win)
            if user_choice>0:
                self.bill_content=self.bill_txt.get("1.0",END)               # Retrieves the bill content from the text area
                try:
                    con=open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")          # Opens a new text file with bill number as filename
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}",parent=self.win)
                con.write(self.bill_content)                                                      # Writes the bill content to the file
                con.close()
                messagebox.showinfo("Success!",f"Bill {bill_no_tk.get()} has been successfully!",parent=self.win)
            else:
                return
        #================================================================================================================================================

        #=============================Button=============================================================================================================

        # Creating a frame inside entry_frame to hold different action buttons
        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="Options",bg="lightgrey",font=('Arial',15))
        self.button_frame.place(x=20,y=280,width=392,height=300)

        # "Add" Button - Calls add_func() when clicked
        self.add_btn=Button(self.button_frame,bd=3,text="Add",font=('Arial',12),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        # "Generate" Button - Calls genbill() when clicked
        self.generate_btn = Button(self.button_frame, bd=3, text="Generate", font=('Arial', 12), width=12, height=3,command=genbill)
        self.generate_btn.grid(row=0, column=1, padx=4, pady=2)

        # "Clear" Button - Calls clear_func() when clicked
        self.clear_btn = Button(self.button_frame, bd=3, text="Clear", font=('Arial', 12), width=12, height=3,command=clear_func)
        self.clear_btn.grid(row=0, column=2, padx=4, pady=2)

        # "Total" Button - Calls total_func() when clicked
        self.total_btn = Button(self.button_frame, bd=3, text="Total", font=('Arial', 12), width=12, height=3,command=total_func)
        self.total_btn.grid(row=1, column=0, padx=4, pady=2)

        # "Reset" Button - Calls reset_func() when clicked
        self.reset_btn = Button(self.button_frame, bd=3, text="Reset", font=('Arial', 12), width=12, height=3,command=reset_func)
        self.reset_btn.grid(row=1, column=1, padx=4, pady=2)

        # "Save" Button - Calls save_func() when clicked
        self.save_btn = Button(self.button_frame, bd=3, text="Save", font=('Arial', 12), width=12, height=3,command=save_func)
        self.save_btn.grid(row=1, column=2, padx=4, pady=2)

        #self._btn = Button(self.button_frame, bd=2, text="Add", font=('Arial', 12), width=15, height=3)
        #self.add_btn.grid(row=0, column=0, padx=4, pady=2)

        ## Disabling some buttons initially (they will be enabled later based on conditions)
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        #==================================================================================================================================================


        #===================Calculator frame===============================================================================================================
        #Calculator in Billing
        self.calc_frame=Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=585,y=110,width=650,height=295)

        self.num_ent=Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Arial',15),width=54,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):                                              #Button Click Function
            text=event.widget.cget("text")
            if text== "=":
                if calc_var.get().isdigit():
                    value=int(calc_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text=="C":
                pass
            else:
                calc_var.set(calc_var.get()+text)
                self.num_ent.update()

        ## Creating a calculator inside the billing window

        # Button for Number 7
        self.btn7=Button(self.calc_frame,bg="lightgrey",text="7",bd=8,width=12,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8 = Button(self.calc_frame, bg="lightgrey", text="8", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn8.grid(row=1, column=1, padx=2, pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9 = Button(self.calc_frame, bg="lightgrey", text="9", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn9.grid(row=1, column=2, padx=2, pady=2)
        self.btn9.bind("<Button-1>",press_btn)

        self.btnadd = Button(self.calc_frame, bg="lightgrey", text="+", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnadd.grid(row=1, column=3, padx=2, pady=2)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4 = Button(self.calc_frame, bg="lightgrey", text="4", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn4.grid(row=2, column=0, padx=2, pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5 = Button(self.calc_frame, bg="lightgrey", text="5", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn5.grid(row=2, column=1, padx=2, pady=2)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6 = Button(self.calc_frame, bg="lightgrey", text="6", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn6.grid(row=2, column=2, padx=2, pady=2)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsubs = Button(self.calc_frame, bg="lightgrey", text="-", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnsubs.grid(row=2, column=3, padx=2, pady=2)
        self.btnsubs.bind("<Button-1>",press_btn)

        self.btn1 = Button(self.calc_frame, bg="lightgrey", text="1", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn1.grid(row=3, column=0, padx=2, pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2 = Button(self.calc_frame, bg="lightgrey", text="2", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn2.grid(row=3, column=1, padx=2, pady=2)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3 = Button(self.calc_frame, bg="lightgrey", text="3", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn3.grid(row=3, column=2, padx=2, pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmult = Button(self.calc_frame, bg="lightgrey", text="*", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnmult.grid(row=3, column=3, padx=2, pady=2)
        self.btnmult.bind("<Button-1>",press_btn)

        self.btn0 = Button(self.calc_frame, bg="lightgrey", text="0", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn0.grid(row=4, column=0, padx=2, pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint = Button(self.calc_frame, bg="lightgrey", text=".", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnpoint.grid(row=4, column=1, padx=2, pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btn_clear = Button(self.calc_frame, bg="lightgrey", text="=", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn_clear.grid(row=4, column=2, padx=2, pady=2)
        self.btn_clear.bind("<Button-1>",press_btn)

        self.btndiv = Button(self.calc_frame, bg="lightgrey", text="/", bd=8, width=12, height=1, font=('Arial', 15))
        self.btndiv.grid(row=4, column=3, padx=2, pady=2)
        self.btndiv.bind("<Button-1>",press_btn)
        #=============================================================================================================================================


        #=========================BILL FRAME==========================================================================================================

        # Creating a section for the bill display
        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=("Arial",18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=650,height=320)

        ## Scrollbar for Bill Display
        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()

        #===============================================================================
if __name__=="__main__":
    main()


