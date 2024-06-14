#----------------IMPORTS---------------------

import mysql.connector
import random
import datetime

#-----------------CONNECTING --------------------

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhikshu@1234",
    database="covid19_db"
    
)

#----------------CONNECTION LINE---------------------

mycursor = mydb.cursor()

#-----------------REGISTER NEW PATIENTS --------------------

def register_patients():
    
    print("---------  ENTER PATIENT DETAILS    -----------\n \n")

    sql_query="insert into total_cases(id,first_name,last_name,age,admitdate,status) values(%s,%s,%s,%s,%s,%s)"
    id = random.randint(0,500)
    first_name=input("Enter the first name of the patient :")
    last_name=input("Enter the last name of the patient : ")
    age=int(input("Enter the age: "))
    admitdate=datetime.datetime.now().date()
    status=input("Enter the status: ")# active or closed or recovered 
    values=(id,first_name,last_name,age,admitdate,status)
    mycursor.execute(sql_query,values)
    mydb.commit()
    print("--------- DATA SAVED SUCCESSFULLY!   -----------\n \n")


#-------------VIEW EXISTING PATIENTS------------------------

def view_patient_details():
    
    print("---------  PATIENT DETAILS    -----------\n \n")
    sql_query="select * from total_cases"
    mycursor.execute(sql_query)
    for i in mycursor:
        print(i)

#-----------------VIEW ACTIVE CASES --------------------

def  view_active_cases():

    print("---------  ACTIVE  CASES    -----------\n \n")
    sql_query="select * from total_cases where status='active'"
    mycursor.execute(sql_query)
    for i in mycursor:
        print(i) 
        
#----------------- VIEW RECOVERED CASES   --------------------
        
def view_recovered_cases():
    
    print("---------  RECOVERED  CASES    -----------\n \n")
    sql_query="select * from total_cases where status='recovered'"
    mycursor.execute(sql_query)
    for i in mycursor:
        print(i) 

#--------------------VIEW DEATH CASES -----------------

def view_death_cases():
    print("--------- UPDATED DEATH CASES    -----------\n")
    sql_query="select * from total_cases where status='closed'"
    mycursor.execute(sql_query)
    for i in mycursor:
        print(i)
        
#--------------------ADD DEATH CASES -----------------
  
def death_cases():

    print("---------  ENTER THE PATIENT DETAILS FOR DEATH CASES..  -----------\n \n")
    sql_query="insert into death_cases(id,first_name,last_name,age,admitdate,deathdate) values(%s,%s,%s,%s,%s,%s)"
    id = random.randint(0,500)
    first_name=input("Enter the first name of the patient :\n")
    last_name=input("Enter the last name of the patient :\n ")
    age=int(input("Enter the age: \n"))
    admitdate=datetime.datetime.now().date()
    available_days = random.randint(0,500)
    deathdate=datetime.datetime.now().date()+datetime.timedelta(days=available_days)
    values=(id,first_name,last_name,age,admitdate,deathdate)
    mycursor.execute(sql_query,values)
    mydb.commit()
    print("--------- DATA SAVED SUCCESSFULLY   -----------\n \n")
    
    print("--------- CLOSING THE CASE   -----------\n \n")

    
    sql_query="UPDATE total_cases SET status = 'closed' WHERE first_name IN (SELECT first_name FROM death_cases) "
    mycursor.execute(sql_query)
    
    mydb.commit()

def TotalCountOfCases():
    print("--------- TOTAL COUNT OF CASES -----------\n")

    # Calculate total count of active cases
    sql_query = "SELECT COUNT(*) FROM total_cases WHERE status = 'active'"
    mycursor.execute(sql_query)
    active_count = mycursor.fetchone()[0]

    # Calculate total count of recovered cases
    sql_query = "SELECT COUNT(*) FROM total_cases WHERE status = 'recovered'"
    mycursor.execute(sql_query)
    recovered_count = mycursor.fetchone()[0]

    # Calculate total count of death cases
    sql_query = "SELECT COUNT(*) FROM death_cases"
    mycursor.execute(sql_query)
    death_count = mycursor.fetchone()[0]

    print("Total Active Cases:", active_count)
    print("Total Recovered Cases:", recovered_count)
    print("Total Death Cases:", death_count)
    print("-----------------------------------------\n")



        
    

#-------------------------------------    
print("---------------------------------------------------\n \n")       
print(" ***** 🚑 Welcome to Sanjeevni Hospital 🚑 *****\n \n")
print("---------------------------------------------------\n \n")

res=input("Enter the number of operation you want to perform :  \n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n  8. exit \n \n" )


while(res != "8"):
    if res == "1":
        register_patients() 
        print("---------------------------------------------------\n \n")
        res = input("Enter the number of operation you want to perform \n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n or 8 to exit:\n")
        print("Data saved successfully!\n \n") 
        print("---------------------------------------------------\n \n")

    if res == "2":
        print("Details are as follows:\n \n ")
        print("---------------------------------------------------\n \n")
        view_patient_details() 
        res = input("Enter the number of operation you want to perform \n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n  or 8 to exit:\n")
        print("---------------------------------------------------\n \n")   

    if res == "3":
        view_active_cases() 
        print("---------------------------------------------------\n \n")
        res = input("Enter the number of operation you want to perform or 8 to exit: \n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count  \n")
        print("---------------------------------------------------\n \n")

    if res == "4":
        view_recovered_cases()
        print("---------------------------------------------------\n \n") 
        res = input("Enter the number of operation you want to perform or 8 to exit:\n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n  8. exit \n")
        print("---------------------------------------------------\n \n")

    if res == "6":
        death_cases() 
        print("---------------------------------------------------\n \n")
        res = input("Enter the number of operation you want to perform or 8 to exit:\n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n  8. exit \n")
        print("---------------------------------------------------\n \n")

    if res == "5":
        view_death_cases()
        print("---------------------------------------------------\n \n")
        res = input("Enter the number of operation you want to perform or 8 to exit:\n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n  7.View Total Cases Count \n  8. exit\n")
        print("---------------------------------------------------\n \n")
        
    if res == "7":
        # Call the function
        TotalCountOfCases()
        print("---------------------------------------------------\n \n")
        res = input("Enter the number of operation you want to perform or 8 to exit:\n 1.Register New Patients \n 2.View Patient Details  \n 3.View Active Cases \n 4.View Recovered Cases \n 5.View Death Cases \n 6. Add New Death Case \n 7.View Total Cases Count \n 8. exit \n")
        print("---------------------------------------------------\n \n")
