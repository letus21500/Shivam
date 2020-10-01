#.............Header Files........................................................................
import sqlite3
import tkinter 
import tkinter.ttk
import tkinter.messagebox
from tkinter import Toplevel, Button, Tk, Menu  

#..................DATABASE........................................................................
class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("database1.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS project_info (project_id PRIMARYKEY text, project_name text, project_domain text,project_type text,project_cost text,project_members text,project_duration text,Date text,project_status text,human_resource text,technical_resource text,other_resource text,client_name text,client_phone text,client_email text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, project_id, project_name,project_domain,project_type,project_cost,project_members,project_duration,Date, project_status,human_resource,technical_resource,other_resource,client_name,client_phone,client_email):
        self.dbCursor.execute("INSERT INTO project_info VALUES (?,?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?)", (project_id, project_name,project_domain,project_type,project_cost,project_members,project_duration,Date, project_status,human_resource,technical_resource,other_resource,client_name,client_phone,client_email))
        self.dbConnection.commit()
        
    def Update(self,project_name,project_domain,project_type,project_cost,project_members,project_duration,Date, project_status,human_resource,technical_resource,other_resource,client_name,client_phone,client_email,project_id):
        self.dbCursor.execute("UPDATE project_info SET project_name = ?, project_domain = ?,project_type = ?, project_cost = ? , project_members = ? ,project_duration = ? ,Date =? , project_status = ?,human_resource = ?,technical_resource = ? ,other_resource = ? ,client_name = ? ,client_phone = ? ,client_email = ? WHERE project_id = ?", (project_name,project_domain,project_type,project_cost,project_members,project_duration,Date, project_status,human_resource,technical_resource,other_resource,client_name,client_phone,client_email,project_id))
        self.dbConnection.commit()
        
    def Search(self, project_id):
        self.dbCursor.execute("SELECT * FROM project_info WHERE project_id = ?", (project_id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
        
    def Delete(self, project_id):
        self.dbCursor.execute("DELETE FROM project_info WHERE project_id = ?", (project_id, ))
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM project_info")
        records = self.dbCursor.fetchall()
        return records

#.................................................................................................

# value class to check if project id and name are entered
class Values:
    C = ["In-active", "Active", "Completed"]
    def Validate(self, project_id, project_name,Completion_List,project_domain,project_members,client_phone,client_email):
        if not (project_id.isnumeric() and (len(project_id) == 3)):
            return "project id"
        elif not (project_name.isalpha()):
            return "project name"
        elif not (Completion_List.isalpha()):
            return "project status"
        elif not (project_domain.isalpha()):
            return "Project Domain"
        elif not (project_members.isdigit() and project_members >= '1'):
            return "Project Members"
        elif not (client_phone.isdigit() and (len(client_phone) == 10)):
            return "Client Phone"
        elif not (client_email.count("@") == 1 and client_email.count(".") > 0):
            return "Client Email"
        else:
            return "SUCCESS"

#................INSERT WINDOW..............................................................................
class InsertWindow:

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("INSERT WINDOW")
        self.window.wm_geometry("900x400")
        
        #...Variables...
        
        self.project_id = tkinter.IntVar()
        self.project_name = tkinter.StringVar()
        self.project_domain=tkinter.StringVar()
        self.Type_List = ["Social", "Environmental", "Corporate","Other"]
        self.project_cost = tkinter.StringVar()
        self.project_members = tkinter.IntVar()
        self.project_duration = tkinter.IntVar()
        self.start_date=tkinter.StringVar()
        self.Completion_List = ["In-active", "Active", "Completed"]
        self.human_resource = tkinter.StringVar()
        self.technical_resource = tkinter.StringVar()
        self.other_resource = tkinter.StringVar()
        self.client_name = tkinter.StringVar()
        self.client_phone = tkinter.StringVar()
        self.client_email = tkinter.StringVar()
        
        #...Labels...
        
        tkinter.Label(self.window, text = "Project ID ( 3 digits only ):",  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "Project Name :",  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = "Project Domain :",  width = 25).grid(pady = 5, column = 4, row = 2)
        tkinter.Label(self.window, text = "Project Type :",  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = "Estimated Cost:",  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = "Members :",  width = 25).grid(pady = 5, column = 4, row = 4)
        tkinter.Label(self.window, text = "Project Duration :",  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = "Commencement Date :",  width = 25).grid(pady = 5, column = 4, row = 5)
        tkinter.Label(self.window, text = "Project Status :",  width = 25).grid(pady = 5, column = 3, row = 7)
        tkinter.Label(self.window, text = "Resources :",  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text ="Human Resource", width = 20).grid(pady = 5, column = 3, row = 8)
        tkinter.Label(self.window, text ="Technical Resource", width = 20).grid(pady = 5, column = 4, row = 8)
        tkinter.Label(self.window, text ="Others", width = 20).grid(pady = 5, column = 5, row = 8)
        tkinter.Label(self.window, text = "Client Name :",  width = 25).grid(pady = 5, column = 2, row = 10)
        tkinter.Label(self.window, text = "Client Contact Number :",  width = 25).grid(pady = 5, column = 2, row = 11)
        tkinter.Label(self.window, text = "Client Email Id :",  width = 25).grid(pady = 5, column = 2, row = 12)
        
        #...Entry Fields & Comboboxes...
        
        #1-->project id
        self.project_id_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_id)
        self.project_id_Entry.delete(0, tkinter.END)
        self.project_id_Entry.grid(pady = 5, column = 4, row = 1)
        #2-->project name
        self.project_name_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_name)
        self.project_name_Entry.grid(pady = 5, column = 3, row = 2)
        #3-->project domain
        self.project_domain_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_domain)
        self.project_domain_Entry.grid(pady = 5, column = 5, row = 2)
        #4-->project type
        self.Type_List_Box = tkinter.ttk.Combobox(self.window, values = self.Type_List, width = 20)
        self.Type_List_Box.grid(pady = 5, column = 3, row = 3)
        #5-->cost
        self.cost_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_cost)
        self.cost_Entry.grid(pady = 5, column = 3, row = 4)
        #6-->members
        self.member_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_members)
        self.member_Entry.grid(pady = 5, column = 5, row = 4)
        self.member_Entry.delete(0, tkinter.END)
        #7-->project duration
        self.project_duration_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_duration)
        self.project_duration_Entry.grid(pady = 5, column = 3, row = 5)
        self.project_duration_Entry.delete(0, tkinter.END)
        #8-->start date
        self.start_date_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.start_date)
        self.start_date_Entry.grid(pady = 5, column = 5, row = 5)
        #9-->status
        self.Completion_List_Box = tkinter.ttk.Combobox(self.window, values = self.Completion_List, width = 20)
        self.Completion_List_Box.grid(pady = 5, column = 4, row = 7)
        #10-->resources
        self.human_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.human_resource)
        self.human_resource_Entry.grid(pady = 5, column = 3, row = 9)
        self.technical_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.technical_resource)
        self.technical_resource_Entry.grid(pady = 5, column = 4, row = 9)
        self.other_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.other_resource)
        self.other_resource_Entry.grid(pady = 5, column = 5, row = 9)
        #11-->Client name
        self.client_name_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_name)
        self.client_name_Entry.grid(pady = 5, column = 3, row = 10)
        #12-->Client phone
        self.client_phone_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_phone)
        self.client_phone_Entry.grid(pady = 5, column = 3, row = 11)
        #13-->Client email
        self.client_email_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_email)
        self.client_email_Entry.grid(pady = 5, column = 3, row = 12)
        
        #...Button...
        
        #..Submit Button..
        tkinter.Button(self.window, width = 40, height = 2, text = "Submit", command = self.Insert).grid(pady = 5, column = 4, row = 13)

        #..Menu Bar..
        top=self.window
        menubar = Menu(top)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="Reset",command=self.Reset)  
        file.add_separator()
        file.add_command(label="Exit", command=top.destroy)  
        menubar.add_cascade(label="Menu", menu=file)
        top.config(menu=menubar)  
        top.mainloop() 
        
        self.window.mainloop()

# Insert function
    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.project_id_Entry.get(), self.project_name_Entry.get(), self.Completion_List_Box.get(),self.project_domain_Entry.get(),self.member_Entry.get(),self.client_phone_Entry.get(),self.client_email_Entry.get())
        if (self.test == "SUCCESS"):
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
            self.database.Insert(self.project_id_Entry.get(), self.project_name_Entry.get(),self.project_domain_Entry.get(),self.Type_List_Box.get(),self.cost_Entry.get(),self.member_Entry.get(),self.project_duration_Entry.get(),self.start_date_Entry.get(), self.Completion_List_Box.get(),self.human_resource_Entry.get(),self.technical_resource_Entry.get(),self.other_resource_Entry.get(),self.client_name_Entry.get(),self.client_phone_Entry.get(),self.client_email_Entry.get())
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test 
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)
        self.window.destroy()
# Reset function
    def Reset(self):
        self.window.destroy()
        homePage = InsertWindow()

#....UPDATE WINDOW...........................................................................................
class UpdateWindow:

    def __init__(self,project_id):
        self.window = Tk()
        self.window.wm_title("UPDATE WINDOW")

        #...Variables...
        
        self.project_id = project_id
        self.project_name = tkinter.StringVar()
        self.project_domain=tkinter.StringVar()
        self.Type_List = ["Social", "Environmental", "Corporate","Other"]
        self.project_cost = tkinter.StringVar()
        self.project_members = tkinter.IntVar()
        self.project_duration = tkinter.IntVar()
        self.start_date=tkinter.StringVar()
        self.Completion_List = ["In-active", "Active", "Completed"]
        self.human_resource = tkinter.StringVar()
        self.technical_resource = tkinter.StringVar()
        self.other_resource = tkinter.StringVar()
        self.client_name = tkinter.StringVar()
        self.client_phone = tkinter.StringVar()
        self.client_email = tkinter.StringVar()

        #...Labels...
        
        tkinter.Label(self.window, text = "Project ID ( 3 digits only ):",  width = 25).grid(pady = 5, column = 2, row = 1)
        tkinter.Label(self.window, text = project_id,  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "Project Name :",  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = "Project Domain :",  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = "Project Type :",  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = "Estimated Cost:",  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = "Members :",  width = 25).grid(pady = 5, column = 2, row = 6)
        tkinter.Label(self.window, text = "Project Duration :",  width = 25).grid(pady = 5, column = 2, row = 7)
        tkinter.Label(self.window, text = "Commencement Date :",  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text = "Project Status :",  width = 25).grid(pady = 5, column = 2, row = 9)
        #tkinter.Label(self.window, text = "Resources :",  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text ="Human Resource", width = 20).grid(pady = 5, column = 2, row = 10)
        tkinter.Label(self.window, text ="Technical Resource", width = 20).grid(pady = 5, column = 2, row = 11)
        tkinter.Label(self.window, text ="Others", width = 20).grid(pady = 5, column = 2, row = 12)
        tkinter.Label(self.window, text = "Client Name :",  width = 25).grid(pady = 5, column = 2, row = 13)
        tkinter.Label(self.window, text = "Client Contact Number :",  width = 25).grid(pady = 5, column = 2, row = 14)
        tkinter.Label(self.window, text = "Client Email Id :",  width = 25).grid(pady = 5, column = 2, row = 15)

        self.database = Database()
        self.searchResults = self.database.Search(project_id)

        tkinter.Label(self.window, text = self.searchResults[0][1],  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = self.searchResults[0][2],  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = self.searchResults[0][3],  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = self.searchResults[0][4],  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = self.searchResults[0][5],  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = self.searchResults[0][6],  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = self.searchResults[0][7],  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = self.searchResults[0][8],  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = self.searchResults[0][9],  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = self.searchResults[0][10],  width = 25).grid(pady = 5, column = 1, row = 11)
        tkinter.Label(self.window, text = self.searchResults[0][11],  width = 25).grid(pady = 5, column = 1, row = 12)
        tkinter.Label(self.window, text = self.searchResults[0][12],  width = 25).grid(pady = 5, column = 1, row = 13)
        tkinter.Label(self.window, text = self.searchResults[0][13],  width = 25).grid(pady = 5, column = 1, row = 14)
        tkinter.Label(self.window, text = self.searchResults[0][14],  width = 25).grid(pady = 5, column = 1, row = 15)

        #...Entry Fields & Comboboxes...
        
        #1-->project name
        self.project_name_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_name)
        self.project_name_Entry.grid(pady = 5, column = 3, row = 2)
        #2-->project domain
        self.project_domain_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_domain)
        self.project_domain_Entry.grid(pady = 5, column = 3, row = 3)
        #3-->project type
        self.Type_List_Box = tkinter.ttk.Combobox(self.window, values = self.Type_List, width = 20)
        self.Type_List_Box.grid(pady = 5, column = 3, row = 4)
        #4-->cost
        self.cost_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_cost)
        self.cost_Entry.grid(pady = 5, column = 3, row = 5)
        #5-->members
        self.member_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_members)
        self.member_Entry.grid(pady = 5, column = 3, row = 6)
        self.member_Entry.delete(0, tkinter.END)
        #6-->project duration
        self.project_duration_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.project_duration)
        self.project_duration_Entry.grid(pady = 5, column = 3, row = 7)
        self.project_duration_Entry.delete(0, tkinter.END)
        #7-->start date
        self.start_date_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.start_date)
        self.start_date_Entry.grid(pady = 5, column = 3, row = 8)
        #8-->status
        self.Completion_List_Box = tkinter.ttk.Combobox(self.window, values = self.Completion_List, width = 20)
        self.Completion_List_Box.grid(pady = 5, column = 3, row = 9)
        #9-->resources
        self.human_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.human_resource)
        self.human_resource_Entry.grid(pady = 5, column = 3, row = 10)
        self.technical_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.technical_resource)
        self.technical_resource_Entry.grid(pady = 5, column = 3, row = 11)
        self.other_resource_Entry = tkinter.Entry(self.window,  width = 25,textvariable = self.other_resource)
        self.other_resource_Entry.grid(pady = 5, column = 3, row = 12)
        #10-->Client name
        self.client_name_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_name)
        self.client_name_Entry.grid(pady = 5, column = 3, row = 13)
        #11-->Client phone
        self.client_phone_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_phone)
        self.client_phone_Entry.grid(pady = 5, column = 3, row = 14)
        #12-->Client email
        self.client_email_Entry = tkinter.Entry(self.window,  width = 25, textvariable = self.client_email)
        self.client_email_Entry.grid(pady = 5, column = 3, row = 15)
        
        #...Button...
        
        #..Submit Button..
        tkinter.Button(self.window, width = 40, height = 2, text = "Submit", command = self.Update).grid(pady = 5, column = 4, row = 16)

        #..Menu Bar..
        top=self.window
        menubar = Menu(top)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="Reset",command=self.Reset)  
        file.add_separator()
        file.add_command(label="Exit", command=top.destroy)  
        menubar.add_cascade(label="Menu", menu=file)
        top.config(menu=menubar)  
        top.mainloop() 
        
        self.window.mainloop()

# Update function
    def Update(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.project_id, self.project_name_Entry.get(), self.Completion_List_Box.get(),self.project_domain_Entry.get(),self.member_Entry.get(),self.client_phone_Entry.get(),self.client_email_Entry.get())
        if (self.test == "SUCCESS"):
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
            self.database.Update(self.project_name_Entry.get(),self.project_domain_Entry.get(),self.Type_List_Box.get(),self.cost_Entry.get(),self.member_Entry.get(),self.project_duration_Entry.get(),self.start_date_Entry.get(), self.Completion_List_Box.get(),self.human_resource_Entry.get(),self.technical_resource_Entry.get(),self.other_resource_Entry.get(),self.client_name_Entry.get(),self.client_phone_Entry.get(),self.client_email_Entry.get(),self.project_id)
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test 
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)
        self.window.destroy()
# Reset function
    def Reset(self):
        self.window.destroy()
        homePage = UpdateWindow()

#....SEARCH & DELETE WINDOW...........................................................................................
class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.project_id = tkinter.StringVar()
        self.project_name = tkinter.StringVar()
        self.project_domain = tkinter.StringVar()
        self.heading = "Please enter Project ID to " + task

        # Labels
        tkinter.Label(window, text = self.heading, width = 50).grid(pady = 20, row = 1)
        tkinter.Label(window, text = "Project ID", width = 10).grid(pady = 5, row = 2)

        # Entry widgets
        self.project_id_Entry= tkinter.Entry(window, width = 5, textvariable = self.project_id)

        self.project_id_Entry.grid(pady = 5, row = 3)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width = 20, text = task, command = self.Search).grid(pady = 15, padx = 5, column = 1, row = 14)
        elif (task == "Delete"):
            tkinter.Button(window, width = 20, text = task, command = self.Delete).grid(pady = 15, padx = 5, column = 1, row = 14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.project_id_Entry.get())
        self.databaseView = DatabaseView(self.data)
    
    def Delete(self):
        self.database = Database()
        self.database.Delete(self.project_id_Entry.get())
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)
        

#....DISPLAY WINDOW..........................................................................................
class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label wproject_idgets
        tkinter.Label(self.databaseViewWindow, text = "Database View Window",  width = 25).grid(pady = 5, column = 1, row = 1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady = 5, column = 1, row = 2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("project_id", "project_name","project_domain","project_type","project_cost","project_members","project_duration","Date", "project_status","human_resource","technical_resource","other_resource","client_name","client_phone","client_email")

        # Treeview column headings
        
        self.databaseView.heading("project_id", text = "Project ID")
        self.databaseView.heading("project_name", text = "Project Name")
        self.databaseView.heading("project_domain", text = "Project Domain")
        self.databaseView.heading("project_type", text = "Project Type")
        self.databaseView.heading("project_cost", text = "Project Cost")
        self.databaseView.heading("project_members", text = "Project Members")
        self.databaseView.heading("project_duration", text = "Project Duration")
        self.databaseView.heading("Date", text = "Date")
        self.databaseView.heading("project_status", text = "Project Status")
        self.databaseView.heading("human_resource", text = "Human Resource")
        self.databaseView.heading("technical_resource", text = "Technical Resource")
        self.databaseView.heading("other_resource", text = "Other Resource")
        self.databaseView.heading("client_name", text = "Client Name")
        self.databaseView.heading("client_phone", text = "Client Phone")
        self.databaseView.heading("client_email", text = "Client Email")


        # Treeview columns
        
        self.databaseView.column("project_id", width=100)
        self.databaseView.column("project_name", width=100)
        self.databaseView.column("project_domain", width=100)
        self.databaseView.column("project_type", width=100)
        self.databaseView.column("project_cost", width=100)
        self.databaseView.column("project_members", width=100)
        self.databaseView.column("project_duration", width=100)
        self.databaseView.column("Date", width=100)
        self.databaseView.column("project_status", width=100)
        self.databaseView.column("human_resource", width=100)
        self.databaseView.column("technical_resource", width=100)
        self.databaseView.column("other_resource", width=100)
        self.databaseView.column("client_name", width=100)
        self.databaseView.column("client_phone", width=100)
        self.databaseView.column("client_email", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()

#....HOME PAGE...............................................................................................
class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Project Information System")

        tkinter.Label(self.homePageWindow, text = "Home Page",  width = 100).grid(pady = 20, column = 1, row = 1)

        tkinter.Button(self.homePageWindow, width = 20, text = "Insert", command = self.Insert).grid(pady = 15, column = 1, row = 2)
        tkinter.Button(self.homePageWindow, width = 20, text = "Update", command = self.Update).grid(pady = 15, column = 1, row = 3)
        tkinter.Button(self.homePageWindow, width = 20, text = "Search", command = self.Search).grid(pady = 15, column = 1, row = 4)
        tkinter.Button(self.homePageWindow, width = 20, text = "Delete", command = self.Delete).grid(pady = 15, column = 1, row = 5)
        tkinter.Button(self.homePageWindow, width = 20, text = "Display", command = self.Display).grid(pady = 15, column = 1, row = 6)
        tkinter.Button(self.homePageWindow, width = 20, text = "Exit", command = self.homePageWindow.destroy).grid(pady = 15, column = 1, row = 7)

        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()

    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.project_id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text = "Enter the ID to update", width = 50).grid(pady = 20, row = 1)

        # Entry widgets
        self.project_id_Entry = tkinter.Entry(self.updateIDWindow, width = 5, textvariable = self.project_id)
        self.project_id_Entry.grid(pady = 10, row = 2)
        
        # Button widgets
        tkinter.Button(self.updateIDWindow, width = 20, text = "Update", command = self.updateID).grid(pady = 10, row = 3)
        
        self.updateIDWindow.mainloop()
        

    def updateID(self):
        updateWindow = UpdateWindow(self.project_id_Entry.get())
        #self.updateIDWindow.destroy()
    
    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")
    
    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)

homePage = HomePage()

#....END PROGRAM.............................................................................................

