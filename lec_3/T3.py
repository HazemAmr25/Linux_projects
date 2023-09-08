#Lec_2   task3
#Write python code that manage a database for employees

import mysql.connector
 
 
con = mysql.connector.connect(
    host="localhost", user="hazem_amr", database="emb")

# Function to Add_Employee
def Add_Employ():
 
    id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(id) == True):
        print("Employee already exists\nTry Again\n")
        menu()
         
    else:
        Name = input("Enter Employee Name : ")
        Salary = input("Enter Employee Salary : ")
        job_title = input("Enter Employee job_title : ")
        data = (id, Name,Salary,job_title)
      
        # Inserting Employee details in
        # the Employee Table
        sql = 'insert into employee values(%s,%s,%s,%s)'
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
 


 
# Function To Check if Employee with
# given Id Exist or Not
def check_employee(employee_id):
     
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from employee where id=%s'
     
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
     
    # Executing the SQL Query
    c.execute(sql, data)
     
    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 
# Function to Remove Employee with given Id
def Remove_Employ():
    Id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id Exist
    # or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from employee where id=%s'
        data = (Id,)
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Removed")
        menu()
        
# Function to Display All Employees
# from Employee Table
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from employee'
    c = con.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Salary : ", i[2])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")
         
    menu()
 
# menu function to display menu
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Display Employees")
    print("4 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Display_Employees()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice")
        menu()
 
 
# Calling menu function
menu()