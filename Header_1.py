import os
import colorama
from colorama import Back, Fore, Style
import datetime
from datetime import date
from datetime import time
colorama.init(autoreset=True)
os.system("cls")
def WelcomeScreen():
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t           __        ____   ____          __     _______   ___   ")
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t   |    | |    |    |      |    | |\  /| |          |     |   |  ")
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t   |    | |__  |    |      |    | | \/ | |__        |     |   |  ")
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t   | /\ | |    |    |      |    | |    | |          |     |   |  ")
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t   |/  \| |__  |___ |____  |____| |    | |__        |     |___|  ")
    print(Fore.LIGHTRED_EX + Back.RED + "\t\t\t\t                                                                 ")
    print("\n\n")   
    Header()
    NextPage=input(Fore.YELLOW + "Press Any Key to go to Next Page:- " + Fore.RESET)
    os.system("cls")
def Header():
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t                           ____   ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t   |\  /|    /\    \   /  |    |  ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t   | \/ |   /  \    \ /   |    |  ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t   |    |  |----|    |    |    |  ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t   |    |  |    |    |    |____|  ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t\t                                  ")
    print("\n\n")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t    ____         _____            _____     ____   ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t   |      |        |      |\   |     |     |       ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t   |      |        |      | \  |     |     |       ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t   |      |        |      |  \ |     |     |       ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t   |____  |____  __|__    |   \|   __|__   |____   ")
    print(Fore.BLACK + Back.BLUE + "\t\t\t\t\t                                                   ")
    print("\n\n\n\n\n\n")
def LoginScreen():
    Header()
    Username=input(Fore.BLACK + Back.CYAN + "Enter Username:-" + Fore.RESET + Back.RESET)
    print()
    Password=input(Fore.BLACK + Back.CYAN + "Enter Password:-" + Fore.RESET + Back.RESET)
    print()
    if Username=='Admin' and Password=='Admin':
        print(Fore.GREEN + "Press 'Y' or 'y' to continue")
        print()
        ch=input(Fore.YELLOW + "Enter Your Choice:-")
        print()
        os.system("cls")
    else:
        print(Fore.RED + "Wrong Username or Password")
def Patient():
    Header()
    print(Fore.GREEN + "Press 1 to See Patient Details")
    print()
    print(Fore.GREEN + "Press 2 to Add Patient Details")
    print()
    print(Fore.GREEN + "Press 3 to Delete Patient Details")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Patient Details")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Patient_Show()
    if ch==2:
        Patient_Add()
    if ch==3:
        Patient_Delete()
    if ch==4:
        Patient_Update()
def Doctor():
    Header()
    print(Fore.GREEN + "Press 1 to See Doctor Details")
    print()
    print(Fore.GREEN + "Press 2 to Add Doctor Details")
    print()
    print(Fore.GREEN + "Press 3 to Delete Doctor Details")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Doctor Details")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Doctor_Show()
    if ch==2:
        Doctor_Add()
    if ch==3:
        Doctor_Delete()
    if ch==4:
        Doctor_Update()
def Appointment():
    Header()
    print(Fore.GREEN + "Press 1 to See Appointment Details")
    print()
    print(Fore.GREEN + "Press 2 to Ask for Appointment")
    print()
    print(Fore.GREEN + "Press 3 to Delete Appointment")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Appointment")
    print()
    print(Fore.GREEN + "Press 5 to See the Status of the Appointment")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Appointment_Show()
    if ch==2:
       Appointment_Add()
    if ch==3:
        Appointment_Delete()
    if ch==4:
        Appointment_Update()
    if ch==5:
        Appointment_Status()
def Admission():
    Header()
    print(Fore.GREEN + "Press 1 to See Admission Details")
    print()
    print(Fore.GREEN + "Press 2 to Admit in the Hospital")
    print()
    print(Fore.GREEN + "Press 3 to Delete Admission Details")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Admission Details")
    print()
    print(Fore.GREEN + "Press 5 to See the Status of the Admission")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Admission_Show()
    if ch==2:
        Admission_Add()
    if ch==3:
        Admission_Delete()
    if ch==4:
        Admission_Update()
    if ch==5:
        Admission_Status()
def Discharge():
    Header()
    print(Fore.GREEN + "Press 1 to See Discharge Details")
    print()
    print(Fore.GREEN + "Press 2 to Discharge from the Hospital")
    print()
    print(Fore.GREEN + "Press 3 to Delete Discharge Details")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Discharge Details")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Discharge_Show()
    if ch==2:
        Discharge_Add()
    if ch==3:
        Discharge_Delete()
    if ch==4:
        Discharge_Update()
def Medical_Records():
    Header()
    print(Fore.GREEN + "Press 1 to See Medical Records")
    print()
    print(Fore.GREEN + "Press 2 to Add Records in the Hospital")
    print()
    print(Fore.GREEN + "Press 3 to Delete Medical Records")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Records")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Medical_Records_Show()
    if ch==2:
        Medical_Records_Add()
    if ch==3:
        Medical_Records_Delete()
    if ch==4:
        Medical_Records_Update()
def Billing_and_Invoicing():
    Header()
    print(Fore.GREEN + "Press 1 to See Billing Details")
    print()
    print(Fore.GREEN + "Press 2 to Add Billing Details")
    print()
    print(Fore.GREEN + "Press 3 to Delete Delete Details")
    print()
    print(Fore.GREEN + "Press 4 to Update/Alter Billing Details")
    print()
    print(Fore.GREEN + "Press 5 to See the Status of the Billing")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Billing_and_Invoicing_Show()
    if ch==2:
        Billing_and_Invoicing_Add()
    if ch==3:
        Billing_and_Invoicing_Delete()
    if ch==4:
        Billing_and_Invoicing_Update()
    if ch==5:
        Billing_and_Invoicing_Status()
def Patient_Show():
    Header()
    os.system("cls")
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        cursor.execute("SELECT PatientID from Patient")
        print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
        for Patient_ID in cursor:
            for x in Patient_ID:
                print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter PatientID for seeing the details:-" + Fore.RESET)
        print()
        Patient_id=(id,)
        sql=("SELECT * from Patient where PatientID=%s")
        cursor.execute(sql,Patient_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "PatientID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Patient Name is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Gender of Patient is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Date of Birth of Patient is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print(Fore.RED + "Phone Number of Patient is -" + Fore.RESET, Fore.GREEN + str(li[4]))
        print(Fore.RED + "Address of Patient is -" + Fore.RESET, Fore.GREEN + str(li[5]))
        print(Fore.RED + "Aadhar Number of Patient is -" + Fore.RESET, Fore.GREEN + str(li[6]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Patient (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Patient_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        PatientID=int(input(Fore.RED + "Input Patient ID you want to add:- " + Fore.RESET + Fore.GREEN))
        PatientName=input(Fore.RED + "Input Patient Name:- " + Fore.RESET + Fore.GREEN)
        PatientGender=input(Fore.RED + "Input Patient Gender(M,F,O):- " + Fore.RESET + Fore.GREEN)
        PDOB=eval(input(Fore.RED + "Input Patient's Year of Birth in this format([YYYY,MM,DD]):- " + Fore.RESET + Fore.GREEN))
        PatientDOB=datetime.datetime(PDOB[0],PDOB[1],PDOB[2])
        PatientPhoneNumber=input(Fore.RED + "Input Patient Phone Number:- " + Fore.RESET + Fore.GREEN)
        PatientAddress=input(Fore.RED + "Input Patient Address:- " + Fore.RESET + Fore.GREEN)
        PatientAadharNumber=input(Fore.RED + "Input Aadhar Number:- " + Fore.RESET + Fore.GREEN)
        Lst=[PatientID,PatientName,PatientGender,PatientDOB,PatientPhoneNumber,PatientAddress,PatientAadharNumber]
        memdata=(Lst)
        sql=("insert into Patient(PatientID,Name,Gender,DOB,Mobile_Number,Address,Aadhaar_Number)values(%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(sql,memdata)
        mycon.commit()
        print(Fore.LIGHTYELLOW_EX + "One Record Added")
        print("\n\n")
        ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    mycon.close
def Patient_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj 
  
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  cursor=mycon.cursor()
  ch='Y'
  while ch=='Y' or ch=='y':
    try:
      os.system("cls")
      Header()
      cursor.execute("SELECT PatientID from Patient")
      for Patient_ID in cursor:
        for x in Patient_ID:
            print(Fore.BLUE + str(x))
      print("\n\n")
      id=input(Fore.RED + "Enter PatientID of Whom you want to Delete Details:-" + Fore.RESET)
      print()
      Patient_id=tuple(id)
      sql=("DELETE FROM Patient where PatientID=%s")
      cursor.execute(sql,Patient_id)
      mycon.commit
      print(Fore.YELLOW + "One Record Deleted")
      print("\n\n")
      ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
    except:
      print(Fore.BLUE + "First Delete Record from Appointment, Admission, Medical_Records and Billing_and_Invoicing of Same Patient ID")
      print("\n\n")
      ch='N'
  mycon.close
def Patient_Update():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    cursor=mycon.cursor()
    choice='Y'
    while choice=='Y' or choice=='y':
        os.system("cls")
        Header()
        sql=("Select PatientID from Patient")
        print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
        cursor.execute(sql)
        for x in cursor:
            for y in x:
                print(Fore.LIGHTGREEN_EX + str(y))
        print("\n\n")
        id=int(input(Fore.RED + "Enter Patient's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
        print("\n\n\n")
        os.system("cls")
        Header()
        print(Fore.GREEN + "Press 1 for Update Patient's Name")
        print()
        print(Fore.GREEN + "Press 2 for Update Patient's Gender")
        print()
        print(Fore.GREEN + "Press 3 for Update Patient's Date of Birth")
        print()
        print(Fore.GREEN + "Press 4 for Update Patient's Phone Number")
        print()
        print(Fore.GREEN + "Press 5 for Update Patient's Address")
        print()
        print(Fore.GREEN + "Press 6 for Update Patient's Aadhaar Number")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            NewName=input(Fore.RED + "Enter New Name:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewName)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set Name=%s where PatientID=%s")
        if ch==2:
            NewGender=input(Fore.RED + "Enter New Gender:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewGender)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set Gender=%s where PatientID=%s")
        if ch==3:
            NewDOB_Year=input(Fore.RED + "Enter New Date of Birth (Year[YYYY]):- " + Fore.RESET + Fore.GREEN)
            NewDOB_Month=input(Fore.RED + "Enter New Date of Birth (Month[MM]):- " + Fore.RESET + Fore.GREEN)
            NewDOB_Date=input(Fore.RED + "Enter New Date of Birth (Date[DD]):- " + Fore.RESET + Fore.GREEN)
            NewDOB=datetime.datetime(NewDOB_Year,NewDOB_Month,NewDOB_Date)
            print()
            Vals=[]
            Vals.append(NewDOB)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set DOB=%s where PatientID=%s")
        if ch==4:
            NewMobileNumber=input(Fore.RED + "Enter New Mobile Number:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewMobileNumber)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set Mobile_Number=%s where PatientID=%s")
        if ch==5:
            NewAddress=input(Fore.RED + "Enter New Address:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewAddress)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set Address=%s where PatientID=%s")
        if ch==6:
            NewAadhaaarNumber=input(Fore.RED + "Enter New Aadhar Number:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewAadhaaarNumber)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Patient Set Aadhaar_Number=%s where PatientID=%s")
        cursor.execute(sql,TVals)
        mycon.commit()
        print("\n\n")
        print(Fore.YELLOW + "Table Updated" + Fore.RESET)
        print("\n\n")
        choice=input(Fore.RED + "Want to Update More Record(Y/N):- " + Fore.RESET)
    mycon.close
def Doctor_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        cursor.execute("SELECT DoctorID from Doctor")
        print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
        for Doctor_ID in cursor:
            for x in Doctor_ID:
                print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter DoctorID for seeing the details:- " + Fore.RESET + Fore.GREEN)
        print()
        Doctor_id=(id,)
        sql=("SELECT * from Doctor where DoctorID=%s")
        cursor.execute(sql,Doctor_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "DoctorID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Doctor's Name is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Doctor's Speacialization is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Doctor's Mobile Number is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Doctor (Y/N)")
        print()
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Doctor_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        DoctorID=int(input(Fore.RED + "Input Doctor's ID you want to add:- " + Fore.RESET + Fore.GREEN))
        DoctorName=input(Fore.RED + "Input Doctor's Name:- " + Fore.RESET + Fore.GREEN)
        DoctorSpeacialization=input(Fore.RED + "Input Doctor's Speacialization:- " + Fore.RESET + Fore.GREEN)
        DoctorPhoneNumber=input(Fore.RED + "Input Doctor's Phone Number:- " + Fore.RESET + Fore.GREEN)
        Lst=[DoctorID,DoctorName,DoctorSpeacialization,DoctorPhoneNumber]
        memdata=(Lst)
        sql=("insert into Doctor(DoctorID,Name,Speacialization,Mobile_Number)values(%s,%s,%s,%s)")
        cursor.execute(sql,memdata)
        mycon.commit()
        print(Fore.LIGHTYELLOW_EX + "One Record Added")
        print("\n\n")
        ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    mycon.close
def Doctor_Update():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    cursor=mycon.cursor()
    choice='Y'
    while choice=='Y' or choice=='y':
        os.system("cls")
        Header()
        sql=("Select DoctorID from Doctor")
        print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
        cursor.execute(sql)
        for x in cursor:
            print(Fore.LIGHTGREEN_EX + str(x))
        print("\n\n")
        id=int(input(Fore.RED + "Enter Doctor's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
        print("\n\n\n")
        os.system("cls")
        Header()
        print(Fore.GREEN + "Press 1 for Update Doctor's Name")
        print()
        print(Fore.GREEN + "Press 2 for Update Doctor's Specialization")
        print()
        print(Fore.GREEN + "Press 3 for Update Doctor's Phone Number")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            NewName=input(Fore.RED + "Enter New Name:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewName)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Doctor Set Name=%s where DoctorID=%s")
        if ch==2:
            NewSpeacialization=input(Fore.RED + "Enter New Speacialization:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewSpeacialization)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Doctor Set Speacialization=%s where DoctorID=%s")
        if ch==3:
            NewMobileNumber=input(Fore.RED + "Enter New Mobile Number:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewMobileNumber)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Doctor Set Mobile_Number=%s where DoctorID=%s")
        cursor.execute(sql,TVals)
        mycon.commit()
        print("\n\n")
        print(Fore.YELLOW + "Table Updated" + Fore.RESET)
        print("\n\n")
        choice=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    mycon.close
def Doctor_Delete():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    cursor=mycon.cursor()
    ch='Y'
    try:
        while ch=='Y' or ch=='y':
            os.system("cls")
            Header()
            print(Fore.RED + "Select DoctorID of Whom you want to Delete Details:-" + Fore.RESET)
            print()
            cursor.execute("SELECT DoctorID from Doctor")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter DoctorID of Whom you want to Delete Details:-" + Fore.RESET)
            print()
            Doctor_id=tuple(id)
            sql=("DELETE FROM Doctor where DoctorID=%s")
            cursor.execute(sql,Doctor_id)
            mycon.commit
            print(Fore.YELLOW + "One Record Deleted")
            print("\n\n")
            ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
    except:
        print(Fore.BLUE + "First Delete Record from Appointment, Admission and Medical_Records of Same Doctor ID" + Fore.RESET)
        print("\n\n")
        ch='N'
    mycon.close
def Appointment_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 for See Appointment Details by Entering Appointment ID")
        print(Fore.YELLOW + "Press 2 for See Appointment Details by Entering Patient ID")
        print(Fore.YELLOW + "Press 3 for See Appointment Details by Entering Doctor ID")
        print("\n\n")
        choice=int(input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN))
        if choice==1:
            cursor.execute("SELECT AppointmentID from Appointment")
            print(Fore.LIGHTBLUE_EX + "Appointment IDs are as Follows")
            for Appointment_ID in cursor:
                for x in Appointment_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter AppointmentID for seeing the details:-" + Fore.RESET)
            print()
            Appointment_id=(id,)
            sql=("SELECT * from Appointment where AppointmentID=%s")
            cursor.execute(sql,Appointment_id)
        if choice==2:
            print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
            cursor.execute("SELECT PatientID from Appointment")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Patient ID for seeing the details:-" + Fore.RESET)
            print()
            Patient_id=(id,)
            sql=("SELECT * from Appointment where PatientID=%s")
            cursor.execute(sql,Patient_id)
        if choice==3:
            print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
            cursor.execute("SELECT DoctorID from Appointment")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Doctor ID for seeing the details:-" + Fore.RESET)
            print()
            Doctor_id=(id,)
            sql=("SELECT * from Appointment where DoctorID=%s")
            cursor.execute(sql,Doctor_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "AppointmentID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Date of Appointment is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Time of Appointment is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Patient ID is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print(Fore.RED + "Doctor ID is -" + Fore.RESET, Fore.GREEN + str(li[4]))
        print(Fore.RED + "Status of Appointment is -" + Fore.RESET, Fore.GREEN + str(li[5]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Appointment (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Appointment_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        try:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "Select one from The following Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "Select one from The following Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            AppointmentID=int(input(Fore.RED + "Input Appointment ID you want to add:- " + Fore.RESET + Fore.GREEN))
            Date_Time=datetime.datetime.now()
            AppointmentDate=date.today()
            AppointmentTime=Date_Time.strftime('%X')
            PatientID=int(input(Fore.RED + "Input Patient ID you want to add:- " + Fore.RESET + Fore.GREEN))
            DoctorID=int(input(Fore.RED + "Input Doctor ID you want to add:- " + Fore.RESET + Fore.GREEN))
            Status=(input(Fore.RED + "Input Status of Appointment:- " + Fore.RESET + Fore.GREEN))
            print("\n\n")
            Lst=[AppointmentID,AppointmentDate,AppointmentTime,PatientID,DoctorID,Status]
            memdata=(Lst)
            sql=("insert into Appointment(AppointmentID,Date_of_Appointment,Time_of_Appointment,PatientID,DoctorID,Status)values(%s,%s,%s,%s,%s,%s)")
            cursor.execute(sql,memdata)
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX + "One Record Added")
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
        except:
            print(Fore.YELLOW + "Add Patient Details First of that Patient ID in the Patient \n \t\t\t or \nAdd Doctor Details First of that Doctor ID in the Doctor" + Fore.RESET)
            ch='N'
        print("\n\n\n\n")
    mycon.close
def Appointment_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  cursor=mycon.cursor()
  ch='Y'
  while ch=='Y' or ch=='y':
      print(Fore.YELLOW + "Press 1 for delete record via Appointment ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 2 for delete record via Patient ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 3 for delete record via Doctor ID" + Fore.RESET)
      print("\n\n")
      Choice=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET + Fore.GREEN))
      if Choice==2:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT PatientID from Appointment")
        for Patient_ID in cursor:
          for x in Patient_ID:
              print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Patient_id=(id,)
        sql=("DELETE FROM Appointment where PatientID=%s")
        cursor.execute(sql,Patient_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==1:
        os.system("cls")
        Header()
        print(Fore.RED + "Select AppointmentID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT AppointmentID from Appointment")
        for Appointment_ID in cursor:
            for x in Appointment_ID:
                print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter AppointmentID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Appointment_id=(id,)
        sql=("DELETE FROM Appointment where AppointmentID=%s")
        cursor.execute(sql,Appointment_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==3:
        os.system("cls")
        Header()
        print(Fore.RED + "Select  Docotr ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT DoctorID from Appointment")
        for Docotr_ID in cursor:
          for x in Docotr_ID:
              print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter AppointmentID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Doctor_id=(id,)
        sql=("DELETE FROM Appointment where DoctorID=%s")
        cursor.execute(sql,Appointment_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
  mycon.close
def Appointment_Update():
    TVals=()
    sql=""
    def Conditions():
        global TVals
        global sql
        os.system("cls")
        print(Fore.GREEN + "Press 1 for Update Appointment's Date")
        print()
        print(Fore.GREEN + "Press 2 for Update Appointment's Time")
        print()
        print(Fore.GREEN + "Press 3 for Update Appointment's Patient ID")
        print()
        print(Fore.GREEN + "Press 4 for Update Appointment's Doctor ID")
        print()
        print(Fore.GREEN + "Press 5 for Update Appointment's Status")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            New_Date=input(Fore.RED + "Enter New Date in this format('YYYY-MM-DD'):- " + Fore.RESET + Fore.GREEN)
            Date=New_Date.split('-')
            NewDate=datetime.datetime(Date[0],Date[1],Date[2])
            print()
            Vals=[]
            Vals.append(NewDate)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Appointment Set Date_of_Appointment=%s where AppointmentID=%s")
        if ch==2:
            New_Time=input(Fore.RED + "Enter New Time in this format(HH:MM:SS):- " + Fore.RESET + Fore.GREEN)
            NewTime=datetime.datetime.strptime(New_Time,'%H:%M:%S')
            print()
            Vals=[]
            Vals.append(NewTime)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Appointment Set Time_of_Appointment=%s where AppointmentID=%s")
        if ch==3:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewPatientID=int(input(Fore.RED + "Enter New Patient ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewPatientID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Appointment Set PatientID=%s where AppointmentID=%s")
        if ch==4:
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "You Can Only These Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewDoctorID=int(input(Fore.RED + "Enter New Doctor ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewDoctorID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Appointment Set DocotrID=%s where AppointmentID=%s")
        if ch==5:
            NewStatus=input(Fore.RED + "Enter New Status:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewStatus)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Appointment Set Status=%s where AppointmentID=%s")
    try:
        os.system("cls")
        Header()
        import mysql.connector as sqlObj
        mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
        if mycon.is_connected():
            print("Connection is Successful")
            print()
        else:
            print("Sorry!!! Connectivity not done")
            print()
        cursor=mycon.cursor()
        ch='Y'
        while ch=='Y' or ch=='y':
            os.system("cls")
            Header()
            print(Fore.YELLOW + "Press 1 For Update Details Via Appointment ID")
            print()
            print(Fore.YELLOW + "Press 2 For Update Details Via Patient ID")
            print()
            print(Fore.YELLOW + "Press 3 For Update Details Via Doctor ID")
            print("\n\n\n\n")
            Choice=int(input(Fore.RED + "Enter Your Choice:- "))
            if Choice==1:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Appointment IDs are as Follows")
                SQL=("Select AppointmentID from Appointment")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Appointment's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==2:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
                SQL=("Select PatientID from Appointment")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Patient's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==3:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
                SQL=("Select DoctorID from Appointment")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Doctor's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            cursor.execute(sql,TVals)
            mycon.commit()
            print("\n\n")
            print(Fore.YELLOW + "Table Updated" + Fore.RESET)
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    except:
        print("\n\n\n")
        print(Fore.RED + "A error has Occured")
    mycon.close
def Appointment_Status():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        print(Fore.YELLOW + "Press 1 for See Status via Appointment ID")
        print(Fore.YELLOW + "Press 2 for See Status via Patieint ID")
        print(Fore.YELLOW + "Press 3 for See Status via Doctor ID")
        print("\n\n\n")
        Choice=int(input(Fore.RED + ("Enter Your Choice:- ") + Fore.RESET + Fore.GREEN))
        print("\n\n")
        if Choice==1:
            sql=("Select Status from Appointment where AppointmentID=%s")
            SQL=("Select AppointmentID from Appointment")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            print("\n\n")
            AppointmentID=input(Fore.RED + "Enter Appointment of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(AppointmentID,)
        if Choice==2:
            SQL=("Select PatientID from Appointment")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            sql=("Select Status from Appointment where PatientID=%s")
            print("\n\n")
            PatientID=input(Fore.RED + "Enter Patient ID of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(PatientID,)
        if Choice==3:
            SQL=("Select DoctorID from Appointment")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            sql=("Select Status from Appointment where DoctorID=%s")
            print("\n\n")
            DoctorID=input(Fore.RED + "Enter Doctor ID of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(DoctorID,)
        cursor.execute(sql,vals)
        print("\n\n\n")
        for y in cursor:
            print(Fore.YELLOW + str(y))
        print("\n\n\n")
        ch=input(Fore.RED + "Want to See Status of Other Appointments (Y/N):- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Admission_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 for See Admission Details by Entering Admission ID")
        print(Fore.YELLOW + "Press 2 for See Admission Details by Entering Patient ID")
        print(Fore.YELLOW + "Press 3 for See Admission Details by Entering Doctor ID")
        print("\n\n")
        choice=int(input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN))
        if choice==1:
            cursor.execute("SELECT AdmissionID from Admission")
            print(Fore.LIGHTBLUE_EX + "Admission IDs are as Follows")
            for Admission_ID in cursor:
                for x in Admission_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter AdmissionID for seeing the details:-" + Fore.RESET)
            print()
            Admission_id=(id,)
            sql=("SELECT * from Admission where AdmissionID=%s")
            cursor.execute(sql,Admission_id)
        if choice==2:
            print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
            cursor.execute("SELECT PatientID from Admission")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Patient ID for seeing the details:-" + Fore.RESET)
            print()
            Patient_id=(id,)
            sql=("SELECT * from Admission where PatientID=%s")
            cursor.execute(sql,Patient_id)
        if choice==3:
            print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
            cursor.execute("SELECT DoctorID from Admission")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Doctor ID for seeing the details:-" + Fore.RESET)
            print()
            Doctor_id=(id,)
            sql=("SELECT * from Admission where DoctorID=%s")
            cursor.execute(sql,Doctor_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "AdmissionID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Date of Admission is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Time of Admission is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Patient ID is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print(Fore.RED + "Doctor ID is -" + Fore.RESET, Fore.GREEN + str(li[4]))
        print(Fore.RED + "Ward or Room Information is -" + Fore.RESET, Fore.GREEN + str(li[5]))
        print(Fore.RED + "Status of Admission is -" + Fore.RESET, Fore.GREEN + str(li[6]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Admission (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Admission_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        try:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "You Can Only These Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            AdmissionID=int(input(Fore.RED + "Input Admission ID you want to add:- " + Fore.RESET + Fore.GREEN))
            Date_Time=datetime.datetime.now()
            AdmissionDate=date.today()
            AdmissionTime=Date_Time.strftime('%X')
            PatientID=int(input(Fore.RED + "Input Patient ID you want to add:- " + Fore.RESET + Fore.GREEN))
            DoctorID=int(input(Fore.RED + "Input Doctor ID you want to add:- " + Fore.RESET + Fore.GREEN))
            WardInformation=input(Fore.RED + "Input Ward Information you want to add:- " + Fore.RESET + Fore.GREEN)
            Status=(input(Fore.RED + "Input Status of Admission:- " + Fore.RESET + Fore.GREEN))
            print("\n\n")
            Lst=[AdmissionID,AdmissionDate,AdmissionTime,PatientID,DoctorID,WardInformation,Status]
            memdata=(Lst)
            sql=("insert into Admission(AdmissionID,Admission_Date,Admission_Time,PatientID,DoctorID,Ward_Information,Admission_Status)values(%s,%s,%s,%s,%s,%s,%s)")
            cursor.execute(sql,memdata)
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX + "One Record Added")
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
        except:
            print(Fore.YELLOW + "Add Patient Details First of that Patient ID in the Patient \n \t\t\t or \nAdd Doctor Details First of that Doctor ID in the Doctor" + Fore.RESET)
            ch='N'
        print("\n\n\n\n")
    mycon.close
def Admission_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  Header()
  cursor=mycon.cursor()
  ch='Y'
  try:
    while ch=='Y' or ch=='y':
      print(Fore.YELLOW + "Press 1 for delete record via Admission ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 2 for delete record via Patient ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 3 for delete record via Doctor ID" + Fore.RESET)
      print("\n\n")
      Choice=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET + Fore.GREEN))
      if Choice==2:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT PatientID from Admission")
        for Patient_ID in cursor:
          for x in Patient_ID:
            print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Patient_id=(id,)
        sql=("DELETE FROM Admission where PatientID=%s")
        cursor.execute(sql,Patient_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==1:
        os.system("cls")
        Header()
        print(Fore.RED + "Select AdmissionID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT AdmissionID from Admission")
        for Admission_ID in cursor:
          for x in Admission_ID:
            print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter AdmissionID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Admission_id=(id,)
        sql=("DELETE FROM Admission where AdmissionID=%s")
        cursor.execute(sql,Admission_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print()
        print()
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==3:
        os.system("cls")
        Header()
        print(Fore.RED + "Select  Docotr ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT DoctorID from Admission")
        for Doctor_ID in cursor:
          for x in Doctor_ID:
            print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter AdmissionID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Doctor_id=(id,)
        sql=("DELETE FROM Admission where DoctorID=%s")
        cursor.execute(sql,Admission_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
  except:
    print(Fore.YELLOW + "First Delete Record from Discharge of Same Admission ID " + Fore.RESET)
    print("\n\n")
  mycon.close
def Admission_Update():
    TVals=()
    def Conditions():
        global TVals
        os.system("cls")
        Header()
        print(Fore.GREEN + "Press 1 for Update Admission's Date")
        print()
        print(Fore.GREEN + "Press 2 for Update Admission's Time")
        print()
        print(Fore.GREEN + "Press 3 for Update Admission's Patient ID")
        print()
        print(Fore.GREEN + "Press 4 for Update Admission's Doctor ID")
        print()
        print(Fore.GREEN + "Press 5 for Update Admission's Ward/Room Information")
        print()
        print(Fore.GREEN + "Press 6 for Update Admission's Status")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            New_Date=input(Fore.RED + "Enter New Date in this format('YYYY-MM-DD'):- " + Fore.RESET + Fore.GREEN)
            Date=New_Date.split('-')
            NewDate=datetime.datetime(Date[0],Date[1],Date[2])
            print()
            Vals=[]
            Vals.append(NewDate)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set Admission_Date=%s where AdmissionID=%s")
        if ch==2:
            New_Time=input(Fore.RED + "Enter New Time in this format(HH:MM:SS):- " + Fore.RESET + Fore.GREEN)
            NewTime=datetime.datetime.strptime(New_Time,'%H:%M:%S')
            print()
            Vals=[]
            Vals.append(NewTime)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set Admission_Time=%s where AdmissionID=%s")
        if ch==3:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewPatientID=int(input(Fore.RED + "Enter New Patient ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewPatientID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set PatientID=%s where AdmissionID=%s")
        if ch==4:
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "You Can Only Enter These Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewDoctorID=int(input(Fore.RED + "Enter New Doctor ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewDoctorID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set DocotrID=%s where AdmissionID=%s")
        if ch==5:
            NewWard=input(Fore.RED + "Enter New Ward/Room Information:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewWard)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set Ward_Information=%s where AdmissionID=%s")
        if ch==6:
            NewStatus=input(Fore.RED + "Enter New Status:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewStatus)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Admission Set Admission_Status=%s where AdmissionID=%s")
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 For Update Details Via Admission ID")
        print()
        print(Fore.YELLOW + "Press 2 For Update Details Via Patient ID")
        print()
        print(Fore.YELLOW + "Press 3 For Update Details Via Doctor ID")
        print("\n\n\n\n")
        Choice=int(input(Fore.RED + "Enter Your Choice:- "))
        if Choice==1:
            print("\n\n")
            print(Fore.LIGHTBLUE_EX + "Admission IDs are as Follows")
            sql=("Select AdmissionID from Admission")
            cursor.execute(sql)
            for x in cursor:
                print(Fore.LIGHTGREEN_EX + str(x))
            print("\n\n")
            id=(input(Fore.RED + "Enter Admission's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
            Conditions()
        if Choice==2:
            print("\n\n")
            print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
            sql=("Select PatientID from Admission")
            cursor.execute(sql)
            for x in cursor:
                print(Fore.LIGHTGREEN_EX + str(x))
            print("\n\n")
            id=(input(Fore.RED + "Enter Patient's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
            Conditions()
        if Choice==3:
            print("\n\n")
            print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
            sql=("Select DoctorID from Admission")
            cursor.execute(sql)
            for x in cursor:
                print(Fore.LIGHTGREEN_EX + str(x))
            print("\n\n")
            id=(input(Fore.RED + "Enter Doctor's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
            Conditions()
        cursor.execute(sql,TVals)
        mycon.commit()
        print("\n\n")
        print(Fore.YELLOW + "Table Updated" + Fore.RESET)
        print("\n\n")
        ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    mycon.close
def Admission_Status():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        print(Fore.YELLOW + "Press 1 for See Status via Admission ID")
        print(Fore.YELLOW + "Press 2 for See Status via Patieint ID")
        print(Fore.YELLOW + "Press 3 for See Status via Doctor ID")
        print("\n\n\n")
        Choice=int(input(Fore.RED + ("Enter Your Choice:- ") + Fore.RESET + Fore.GREEN))
        print("\n\n")
        if Choice==1:
            SQL=("Select AdmissionID from Admission")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            print("\n\n")
            AdmissionID=input(Fore.RED + "Enter Admission of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            sql=("Select Admission_Status from Admission where AdmissionID=%s")
            vals=(AdmissionID,)
        if Choice==2:
            SQL=("Select PatientID from Admission")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            sql=("Select Admission_Status from Admission where PatientID=%s")
            print("\n\n")
            PatientID=input(Fore.RED + "Enter Patient ID of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(PatientID,)
        if Choice==3:
            SQL=("Select DoctorID from Admission")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            sql=("Select Admission_Status from Admission where DoctorID=%s")
            print("\n\n")
            DoctorID=input(Fore.RED + "Enter Doctor ID of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(DoctorID,)
        cursor.execute(sql,vals)
        print("\n\n\n")
        for y in cursor:
            print(Fore.YELLOW + str(y))
        print("\n\n\n")
        ch=input(Fore.RED + "Want to See Status of Other Admissions (Y/N):- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Discharge_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 for See Discharge Details by Entering Discharge ID")
        print(Fore.YELLOW + "Press 2 for See Discharge Details by Entering Admission ID")
        print("\n\n")
        choice=int(input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN))
        print("\n\n")
        if choice==1:
            cursor.execute("SELECT DischargeID from Discharge")
            print(Fore.LIGHTBLUE_EX + "Discharge IDs are as Follows")
            print()
            for Discharge_ID in cursor:
                for x in Discharge_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter DischargeID for seeing the details:-" + Fore.RESET)
            print()
            Discharge_id=(id,)
            sql=("SELECT * from Discharge where DischargeID=%s")
            cursor.execute(sql,Discharge_id)
        if choice==2:
            print(Fore.LIGHTBLUE_EX + "Admission IDs are as Follows")
            cursor.execute("SELECT AdmissionID from Discharge")
            print()
            for Admission_ID in cursor:
                for x in Admission_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Admission ID for seeing the details:-" + Fore.RESET)
            print()
            Patient_id=(id,)
            sql=("SELECT * from Discharge where AdmissionID=%s")
            cursor.execute(sql,Patient_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "DischargeID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Date of Discharge is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Time of Discharge is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Admission ID is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Discharge (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Discharge_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        try:
            cursor.execute("SELECT AdmissionID from Admission")
            print(Fore.YELLOW + "You Can Only Enter These Admission IDs" + Fore.RESET)
            print("\n\n")
            for Admission_ID in cursor:
                for x in Admission_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            DischargeID=int(input(Fore.RED + "Input Discharge ID you want to add:- " + Fore.RESET + Fore.GREEN))
            Date_Time=datetime.datetime.now()
            DischargeDate=date.today()
            DischargeTime=Date_Time.strftime('%X')
            AdmissionID=int(input(Fore.RED + "Input Admission ID you want to add:- " + Fore.RESET + Fore.GREEN))
            print("\n\n")
            Lst=[DischargeID,DischargeDate,DischargeTime,AdmissionID]
            memdata=(Lst)
            sql=("insert into Discharge(DischargeID,Discharge_Date,Discharge_Time,AdmissionID)values(%s,%s,%s,%s)")
            cursor.execute(sql,memdata)
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX + "One Record Added")
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
        except:
            print(Fore.YELLOW + "Add Admission Details First of that Patient ID in the Admission " + Fore.RESET)
            ch='N'
        print("\n\n\n\n")
    mycon.close
def Discharge_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  Header()
  cursor=mycon.cursor()
  ch='Y'
  while ch=='Y' or ch=='y':
      print(Fore.YELLOW + "Press 1 for delete record via Discharge ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 2 for delete record via Admission ID" + Fore.RESET)
      print("\n\n")
      Choice=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET + Fore.GREEN))
      if Choice==2:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Admission ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT AdmissionID from Discharge")
        for Admission_ID in cursor:
          for x in Admission_ID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Admission ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Admission_id=(id,)
        sql=("DELETE FROM Discharge where AdmissionID=%s")
        cursor.execute(sql,Admission_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==1:
        os.system("cls")
        Header()
        print(Fore.RED + "Select DischargeID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT DischargeID from Discharge")
        for Discharge_ID in cursor:
          for x in Discharge_ID:
            print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter DischargeID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Discharge_id=(id,)
        sql=("DELETE FROM Discharge where DischargeID=%s")
        cursor.execute(sql,Discharge_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
  mycon.close
def Discharge_Update():
    TVals=()
    sql=""
    def Conditions():
        global TVals
        global sql
        os.system("cls")
        Header()
        print(Fore.GREEN + "Press 1 for Update Discharge's Date")
        print()
        print(Fore.GREEN + "Press 2 for Update Discharge's Time")
        print()
        print(Fore.GREEN + "Press 3 for Update Discharge's Admission ID")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            New_Date=input(Fore.RED + "Enter New Date in this format('YYYY-MM-DD'):- " + Fore.RESET + Fore.GREEN)
            Date=New_Date.split('-')
            NewDate=datetime.datetime(Date[0],Date[1],Date[2])
            print()
            Vals=[]
            Vals.append(NewDate)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Discharge Set Discharge_Date=%s where DischargeID=%s")
        if ch==2:
            New_Time=input(Fore.RED + "Enter New Time in this format(HH:MM:SS):- " + Fore.RESET + Fore.GREEN)
            NewTime=datetime.datetime.strptime(New_Time,'%H:%M:%S')
            print()
            Vals=[]
            Vals.append(NewTime)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Discharge Set Discharge_Time=%s where DischargeID=%s")
        if ch==3:
            cursor.execute("SELECT  AdmissionID from Admission")
            print(Fore.YELLOW + "You Can Only Enter These Admission IDs" + Fore.RESET)
            print("\n\n")
            for Admission_ID in cursor:
                for x in Admission_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewPatientID=int(input(Fore.RED + "Enter New Admission ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewPatientID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Discharge Set AdmissionID=%s where DischargeID=%s")
    try:
        os.system("cls")
        Header()
        import mysql.connector as sqlObj
        mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
        if mycon.is_connected():
            print("Connection is Successful")
            print()
        else:
            print("Sorry!!! Connectivity not done")
            print()
        os.system("cls")
        Header()
        cursor=mycon.cursor()
        ch='Y'
        while ch=='Y' or ch=='y':
            print(Fore.YELLOW + "Press 1 For Update Details Via Discharge ID")
            print()
            print(Fore.YELLOW + "Press 2 For Update Details Via Admission ID")
            print("\n\n\n\n")
            Choice=int(input(Fore.RED + "Enter Your Choice:- "))
            if Choice==1:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Discharge IDs are as Follows")
                SQL=("Select DischargeID from Discharge")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Discharge's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==2:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Admission IDs are as Follows")
                SQL=("Select PatientID from Discharge")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Admission's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            cursor.execute(sql,TVals)
            mycon.commit()
            print("\n\n")
            print(Fore.YELLOW + "Table Updated" + Fore.RESET)
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    except:
        print("\n\n")
        print(Fore.RED + "A error has occured")
    mycon.close
def Medical_Records_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 for See Medical_Records Details by Entering Records ID")
        print(Fore.YELLOW + "Press 2 for See Medical_Records Details by Entering Patient ID")
        print(Fore.YELLOW + "Press 3 for See Medical_Records Details by Entering Doctor ID")
        print("\n\n")
        choice=int(input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN))
        if choice==1:
            cursor.execute("SELECT RecordID from Medical_Records")
            print(Fore.LIGHTBLUE_EX + "Medical_Record IDs are as Follows")
            for Medical_Records_ID in cursor:
                for x in Medical_Records_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Medical_RecordsID for seeing the details:-" + Fore.RESET)
            print()
            Medical_Records_id=(id,)
            sql=("SELECT * from Medical_Records where RecordID=%s")
            cursor.execute(sql,Medical_Records_id)
        if choice==2:
            print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
            cursor.execute("SELECT PatientID from Medical_Records")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Patient ID for seeing the details:-" + Fore.RESET)
            print()
            Patient_id=(id,)
            sql=("SELECT * from Medical_Records where PatientID=%s")
            cursor.execute(sql,Patient_id)
        if choice==3:
            print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
            cursor.execute("SELECT DoctorID from Medical_Records")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Doctor ID for seeing the details:-" + Fore.RESET)
            print()
            Doctor_id=(id,)
            sql=("SELECT * from Medical_Records where DoctorID=%s")
            cursor.execute(sql,Doctor_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "Medical_RecordsID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Patient ID is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Doctor ID is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Diagnosis is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Medical_Records (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Medical_Records_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        try:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                print(Fore.BLUE + str(Patient_ID))
            print("\n\n")
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "You Can Only These Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            Medical_RecordsID=int(input(Fore.RED + "Input Medical_Records ID you want to add:- " + Fore.RESET + Fore.GREEN))
            PatientID=int(input(Fore.RED + "Input Patient ID you want to add:- " + Fore.RESET + Fore.GREEN))
            DoctorID=int(input(Fore.RED + "Input Doctor ID you want to add:- " + Fore.RESET + Fore.GREEN))
            Diagnosis=input(Fore.RED + "Input Diagnosis you want to add:- " + Fore.RESET + Fore.GREEN)
            print("\n\n")
            Lst=[Medical_RecordsID,PatientID,DoctorID,Diagnosis]
            memdata=(Lst)
            sql=("insert into Medical_Records(RecordID,PatientID,DoctorID,Diagnosis)values(%s,%s,%s,%s)")
            cursor.execute(sql,memdata)
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX + "One Record Added")
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
        except:
            print(Fore.YELLOW + "Add Patient Details First of that Patient ID in the Patient \n \t\t\t or \nAdd Doctor Details First of that Doctor ID in the Doctor" + Fore.RESET)
            ch='N'
        print("\n\n\n\n")
    mycon.close
def Medical_Records_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  Header()
  cursor=mycon.cursor()
  ch='Y'
  while ch=='Y' or ch=='y':
      print(Fore.YELLOW + "Press 1 for delete record via Medical_Records ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 2 for delete record via Patient ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 3 for delete record via Doctor ID" + Fore.RESET)
      print("\n\n")
      Choice=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET + Fore.GREEN))
      if Choice==2:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT PatientID from Medical_Records")
        for Patient_ID in cursor:
          for x in Patient_ID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Patient_id=(id,)
        sql=("DELETE FROM Medical_Records where PatientID=%s")
        cursor.execute(sql,Patient_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==1:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Medical_RecordsID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT RecordID from Medical_Records")
        for Medical_Records_ID in cursor:
          for x in Medical_Records_ID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Medical_RecordsID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Medical_Records_id=(id,)
        sql=("DELETE FROM Medical_Records where RecordID=%s")
        cursor.execute(sql,Medical_Records_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==3:
        os.system("cls")
        Header()
        print(Fore.RED + "Select  Docotr ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT DoctorID from Medical_Records")
        for Doctor_ID in cursor:
          for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Medical_RecordsID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Doctor_id=(id,)
        sql=("DELETE FROM Medical_Records where DoctorID=%s")
        cursor.execute(sql,Medical_Records_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
  mycon.close
def Medical_Records_Update():
    TVals=()
    sql=""
    def Conditions():
        global sql
        global TVals
        os.system("cls")
        Header()
        print()
        print(Fore.GREEN + "Press 1 for Update Medical_Records's Patient ID")
        print()
        print(Fore.GREEN + "Press 2 for Update Medical_Records's Doctor ID")
        print()
        print(Fore.GREEN + "Press 3 for Update Medical_Records's Diagnosis")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewPatientID=int(input(Fore.RED + "Enter New Patient ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewPatientID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Medical_Records Set PatientID=%s where RecordID=%s")
        if ch==2:
            cursor.execute("SELECT DoctorID from Doctor")
            print(Fore.YELLOW + "You Can Only Enter These Doctor ID's" + Fore.RESET)
            print("\n\n")
            for Doctor_ID in cursor:
                for x in Doctor_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewDoctorID=int(input(Fore.RED + "Enter New Doctor ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewDoctorID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Medical_Records Set DocotrID=%s where RecordID=%s")
        if ch==3:
            NewDaignosis=input(Fore.RED + "Enter New Diagnosis:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewDaignosis)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Medical_Records Set Diagnosis=%s where RecordsID=%s")
    try:
        os.system("cls")
        Header()
        import mysql.connector as sqlObj
        mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
        if mycon.is_connected():
            print("Connection is Successful")
            print()
        else:
            print("Sorry!!! Connectivity not done")
            print()
        cursor=mycon.cursor()
        ch='Y'
        while ch=='Y' or ch=='y':
            os.system("cls")
            Header()
            print(Fore.YELLOW + "Press 1 For Update Details Via Medical_Records ID")
            print()
            print(Fore.YELLOW + "Press 2 For Update Details Via Patient ID")
            print()
            print(Fore.YELLOW + "Press 3 For Update Details Via Doctor ID")
            print("\n\n\n\n")
            Choice=int(input(Fore.RED + "Enter Your Choice:- "))
            if Choice==1:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Medical_Records IDs are as Follows")
                SQL=("Select RecordID from Medical_Records")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Medical_Records's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==2:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
                SQL=("Select PatientID from Medical_Records")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Patient's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==3:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Doctor IDs are as Follows")
                SQL=("Select DoctorID from Medical_Records")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Doctor's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            cursor.execute(sql,TVals)
            mycon.commit()
            print("\n\n")
            print(Fore.YELLOW + "Table Updated" + Fore.RESET)
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    except:
        print("\n\n")
        print(Fore.RED + "A error has Occured")
    mycon.close
def Billing_and_Invoicing_Show():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
      print("Connection is Successful")
      print()
    else:
      print("Sorry!!! Connectivity not done")
      print()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='y' or ch=='Y':
        os.system("cls")
        Header()
        print(Fore.YELLOW + "Press 1 for See Billing_and_Invoicing Details by Entering Billing_and_Invoicing ID")
        print(Fore.YELLOW + "Press 2 for See Billing_and_Invoicing Details by Entering Patient ID")
        print("\n\n")
        choice=int(input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN))
        print("\n\n")
        if choice==1:
            cursor.execute("SELECT BillID from Billing_and_Invoicing")
            print(Fore.LIGHTBLUE_EX + "Billing_and_Invoicing IDs are as Follows")
            print()
            for Billing_and_Invoicing_ID in cursor:
                for x in Billing_and_Invoicing_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Billing_and_InvoicingID for seeing the details:-" + Fore.RESET)
            print()
            Billing_and_Invoicing_id=(id,)
            sql=("SELECT * from Billing_and_Invoicing where BillID=%s")
            cursor.execute(sql,Billing_and_Invoicing_id)
        if choice==2:
            print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
            cursor.execute("SELECT PatientID from Billing_and_Invoicing")
            print()
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            id=input(Fore.RED + "Enter Patient ID for seeing the details:-" + Fore.RESET)
            print()
            Patient_id=(id,)
            sql=("SELECT * from Billing_and_Invoicing where PatientID=%s")
            cursor.execute(sql,Patient_id)
        li=[]
        for details in cursor:
            li+=list(details)
        print(Fore.CYAN + "Details are as follows")
        print()
        print(Fore.RED + "Billing_and_InvoicingID is -" + Fore.RESET, Fore.GREEN + str(li[0]))
        print(Fore.RED + "Patient ID is -" + Fore.RESET, Fore.GREEN + str(li[1]))
        print(Fore.RED + "Total Payment is -" + Fore.RESET, Fore.GREEN + str(li[2]))
        print(Fore.RED + "Payment Status is -" + Fore.RESET, Fore.GREEN + str(li[3]))
        print("\n\n\n")
        print(Fore.LIGHTGREEN_EX + "Want to See Details of other Billing_and_Invoicing (Y/N)")
        ch=input(Fore.RED + "Enter your Choice:- " + Fore.RESET + Fore.GREEN)
    mycon.close
def Billing_and_Invoicing_Add():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        try:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            Billing_and_InvoicingID=int(input(Fore.RED + "Input Billing_and_Invoicing ID you want to add:- " + Fore.RESET + Fore.GREEN))
            PatientID=int(input(Fore.RED + "Input Patient ID you want to add:- " + Fore.RESET + Fore.GREEN))
            TotalPayment=float(input(Fore.RED + "Input Total Payment you want to add:- " + Fore.RESET + Fore.GREEN))
            PaymentStatus=input(Fore.RED + "Input Payment Status you want to add:- " + Fore.RESET + Fore.GREEN)
            print("\n\n")
            Lst=[Billing_and_InvoicingID,PatientID,TotalPayment,PaymentStatus]
            memdata=(Lst)
            sql=("insert into Billing_and_Invoicing(BillID,PatientID,Total_Payment,Payment_Status)values(%s,%s,%s,%s)")
            cursor.execute(sql,memdata)
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX + "One Record Added")
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
        except:
            print(Fore.YELLOW + "Add Patient Details First of that Patient ID in the Patient " + Fore.RESET)
            ch='N'
        print("\n\n\n\n")
    mycon.close
def Billing_and_Invoicing_Delete():
  os.system("cls")
  Header()
  import mysql.connector as sqlObj
  mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
  if mycon.is_connected():
    print("Connection is Successful")
    print()
  else:
    print("Sorry!!! Connectivity not done")
    print()
  os.system("cls")
  Header()
  cursor=mycon.cursor()
  ch='Y'
  while ch=='Y' or ch=='y':
      print(Fore.YELLOW + "Press 1 for delete record via Bill ID" + Fore.RESET)
      print(Fore.YELLOW + "Press 2 for delete record via Patient ID" + Fore.RESET)
      print("\n\n")
      Choice=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET + Fore.GREEN))
      if Choice==2:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT PatientID from Billing_and_Invoicing")
        for Patient_ID in cursor:
          for x in Patient_ID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Patient ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Patient_id=(id,)
        sql=("DELETE FROM Billing_and_Invoicing where PatientID=%s")
        cursor.execute(sql,Patient_id)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
      if Choice==1:
        os.system("cls")
        Header()
        print(Fore.RED + "Select Bill ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        cursor.execute("SELECT BillID from Billing_and_Invoicing")
        for BillID in cursor:
          for x in BillID:
                    print(Fore.BLUE + str(x))
        print("\n\n")
        id=input(Fore.RED + "Enter Bill ID of Whom you want to Delete Details:-" + Fore.RESET)
        print()
        Billid=(id,)
        sql=("DELETE FROM Billing_and_Invoicing where BillID=%s")
        cursor.execute(sql,Billid)
        mycon.commit
        print(Fore.YELLOW + "One Record Deleted")
        print("\n\n")
        ch=input(Fore.RED + "Want to Delete More Record(Y/N):- " + Fore.RESET)
  mycon.close
def Billing_and_Invoicing_Update():
    TVals=()
    sql=""
    def Conditions():
        global TVals
        global sql
        os.system("cls")
        Header()
        print()
        print(Fore.GREEN + "Press 1 for Update Billing_and_Invoicing's Patient ID")
        print()
        print(Fore.GREEN + "Press 2 for Update Billing_and_Invoicing's Total Payment")
        print()
        print(Fore.GREEN + "Press 3 for Update Billing_and_Invoicing's Payment Status")
        print("\n\n\n\n\n\n")
        ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
        print()
        if ch==1:
            cursor.execute("SELECT PatientID from Patient")
            print(Fore.YELLOW + "You Can Only Enter These Patient IDs" + Fore.RESET)
            print("\n\n")
            for Patient_ID in cursor:
                for x in Patient_ID:
                    print(Fore.BLUE + str(x))
            print("\n\n")
            NewPatientID=int(input(Fore.RED + "Enter New Patient ID:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewPatientID)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Billing_and_Invoicing Set PatientID=%s where RecordID=%s")
        if ch==2:
            NewTotalPayment=int(input(Fore.RED + "Enter New Total Payment:- " + Fore.RESET + Fore.GREEN))
            print()
            Vals=[]
            Vals.append(NewTotalPayment)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Billing_and_Invoicing Set DocotrID=%s where RecordID=%s")
        if ch==3:
            NewStatus=input(Fore.RED + "Enter New Status:- " + Fore.RESET + Fore.GREEN)
            print()
            Vals=[]
            Vals.append(NewStatus)
            Vals.append(id)
            TVals=tuple(Vals)
            sql=("Update Billing_and_Invoicing Set Diagnosis=%s where RecordsID=%s")
    try:
        os.system("cls")
        Header()
        import mysql.connector as sqlObj
        mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
        if mycon.is_connected():
            print("Connection is Successful")
            print()
        else:
            print("Sorry!!! Connectivity not done")
            print()
        cursor=mycon.cursor()
        ch='Y'
        while ch=='Y' or ch=='y':
            os.system("cls")
            Header()
            print(Fore.YELLOW + "Press 1 For Update Details Via Billing_and_Invoicing ID")
            print()
            print(Fore.YELLOW + "Press 2 For Update Details Via Patient ID")
            print("\n\n\n\n")
            Choice=int(input(Fore.RED + "Enter Your Choice:- "))
            if Choice==1:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Billing_and_Invoicing IDs are as Follows")
                SQL=("Select BillID from Billing_and_Invoicing")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Billing_and_Invoicing's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            if Choice==2:
                print("\n\n")
                print(Fore.LIGHTBLUE_EX + "Patient IDs are as Follows")
                SQL=("Select PatientID from Billing_and_Invoicing")
                cursor.execute(SQL)
                for x in cursor:
                    print(Fore.LIGHTGREEN_EX + str(x))
                print("\n\n")
                id=(input(Fore.RED + "Enter Patient's ID of whom details you want to Update:- " + Fore.RESET + Fore.GREEN))
                Conditions()
            cursor.execute(sql,TVals)
            mycon.commit()
            print("\n\n")
            print(Fore.YELLOW + "Table Updated" + Fore.RESET)
            print("\n\n")
            ch=input(Fore.RED + "Want to Add More Record(Y/N):- " + Fore.RESET)
    except:
        print("\n\n")
        print(Fore.RED + "A error has occured")
    mycon.close
def Billing_and_Invoicing_Status():
    os.system("cls")
    Header()
    import mysql.connector as sqlObj
    mycon=sqlObj.connect(host="localhost",user="root",passwd="12345",database="Mayo_Clinic")
    if mycon.is_connected():
        print("Connection is Successful")
        print()
    else:
        print("Sorry!!! Connectivity not done")
        print()
    os.system("cls")
    Header()
    cursor=mycon.cursor()
    ch='Y'
    while ch=='Y' or ch=='y':
        print(Fore.YELLOW + "Press 1 for See Status via Billing_and_Invoicing ID")
        print(Fore.YELLOW + "Press 2 for See Status via Patieint ID")
        print("\n\n\n")
        Choice=int(input(Fore.RED + ("Enter Your Choice:- ") + Fore.RESET + Fore.GREEN))
        print("\n\n")
        if Choice==1:
            SQL=("Select BillID from Billing_and_Invoicing")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            print("\n\n")
            Billing_and_InvoicingID=input(Fore.RED + "Enter Billing_and_Invoicing of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            sql=("Select Payment_Status from Billing_and_Invoicing where BillID=%s")
            vals=(Billing_and_InvoicingID,)
        if Choice==2:
            SQL=("Select PatientID from Billing_and_Invoicing")
            cursor.execute(SQL)
            for i in cursor:
                print(Fore.GREEN + str(i))
            sql=("Select Payment_Status from Billing_and_Invoicing where PatientID=%s")
            print("\n\n")
            PatientID=input(Fore.RED + "Enter Patient ID of whom you want to see Status:- " + Fore.RESET + Fore.GREEN)
            vals=(PatientID,)
        cursor.execute(sql,vals)
        print("\n\n\n")
        for y in cursor:
            print(Fore.YELLOW + str(y))
        print("\n\n\n")
        ch=input(Fore.RED + "Want to See Status of Other Billing_and_Invoicings (Y/N):- " + Fore.RESET + Fore.GREEN)
    mycon.close
def MainMenu():
    Header()
    print(Fore.GREEN + "Press 1 for Open Patient Menu")
    print()
    print(Fore.GREEN + "Press 2 for Open Doctor Menu")
    print()
    print(Fore.GREEN + "Press 3 for Open Appointment Menu")
    print()
    print(Fore.GREEN + "Press 4 for Open Admission Menu")
    print()
    print(Fore.GREEN + "Press 5 for Open Discharge Menu")
    print()
    print(Fore.GREEN + "Press 6 for Open Medical Records Menu")
    print()
    print(Fore.GREEN + "Press 7 for Open Billing and Invoicing Menu")
    print("\n\n\n\n\n\n")
    ch=int(input(Fore.RED + "Enter Your Choice:-" + Fore.RESET))
    os.system('cls')
    if ch==1:
        Patient()
    if ch==2:
        Doctor()
    if ch==3:
        Appointment()
    if ch==4:
        Admission()
    if ch==5:
        Discharge()
    if ch==6:
        Medical_Records()
    if ch==7:
        Billing_and_Invoicing()
WelcomeScreen()
LoginScreen()
Option='Y'
while Option=='Y' or Option=='y':
    os.system("cls")
    MainMenu()
    print("\n\n\n\n")
    Option=input(Fore.RED + "Want to any Other Task (Y/N):- " + Fore.RESET + Fore.GREEN)