#Menu driven program to perform various functions in list containing data in form of dictionary
def menudriven():
    global Li
    print("Press 1 for append data in list")
    print("Press 2 for delete data in list")
    print("Press 3 for update data in list")
    print("Press 4 for view data")
    print()
    choice=int(input("Enter your choice:- "))
    print("\n\n")
    if choice==1:
        ch='Y'
        while ch=='Y' or ch=='y':
            Reg=input("Enter reg number:- ")
            Name=input("Enter Name:- ")
            DOB=input("Enter DOB in this format (DD-MM-YYYY):- ")
            Dic={"Regno":Reg,"Name":Name,"DOB":DOB}
            print()
            Li.append(Dic)
            ch=input("Want to enter more data:- ")
            print()
    if choice==2:
        i=0
        Flag=False
        Reg=int(input("Enter Reg Number of whom you want to delete data:- "))
        for data in Li:
            if int(data["Regno"])==Reg:
                del Li[i]
                Flag=True
            else:
                i+=1
        if Flag==False:
            print("\n\nNo record found")
        print("\n\nRecord Deleted Successfully\n\n")
    if choice==3:
        Reg=int(input("Enter Reg Number of whom you want to update data:- "))
        print("\nPress 1 for update Reg number")
        print("\nPress 2 for update Name")
        print("\nPress 3 for update DOB\n")
        ch=int(input("Enter your choice:- "))
        Flag=False
        for data in Li:
            if int(data["Regno"])==Reg:
                Flag=True
                if ch==1:
                    Regno=input("Enter Updated Reg Number:- ")
                    data["Regno"]=Regno
                if ch==2:
                    Name=input("Enter Updated Name:- ")
                    data["Name"]=Name
                if ch==3:
                    DOB=input("Enter Updated Date of Birth:- ")
                    data["DOB"]=DOB
        if Flag==False:
            print("\n\nNo record found")
        print("\n\nRecord Updated Successfully\n\n")
    if choice==4:
        Reg=int(input("Enter Reg Number of whom you want to see data:- "))
        Flag=False
        for data in Li:
            if int(data["Regno"])==Reg:
                print("\n\nReg Number is :- ",data["Regno"])
                print("Name is:-  ",data["Name"])
                print("Date of Birth is:- ",data["DOB"])
                Flag=True
        if Flag==False:
            print("No record found")
        else:
            print("\n\nRecord readed Successfully")
    print("\n\n")
CH='Y'
Li=[]
while CH=='Y' or CH=='y':
    Reg=input("Enter reg number:- ")
    Name=input("Enter Name:- ")
    DOB=input("Enter DOB in this format (DD-MM-YYYY):- ")
    Dic={"Regno":Reg,"Name":Name,"DOB":DOB}
    print()
    Li.append(Dic)
    CH=input("Want to enter more data:- ")
    print()
ch='Y'
while ch=='Y' or ch=='y':
    menudriven()
    ch=input("Want to perform other function (Y/N):- ")