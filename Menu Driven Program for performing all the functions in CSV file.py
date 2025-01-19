#Menu Driven Program for performing all the functions in CSV file
import csv
def AppendData():
    with open ("demo.csv","a",newline="") as file:
        writer=csv.writer(file)
        Data=[]
        Ch='Y'
        while Ch=='Y' or Ch=='y':
            print("\n\n")
            Name=input("Enter Name of the Student:- ")
            Class=input("Enter Class of the Student:- ")
            PhysicsMarks=input("Enter Physics Marks:- ")
            ChemistryMarks=input("Enter Chemistry Marks:- ")
            ComputerMarks=input("Enter Computer Science Marks:- ")
            MathsMarks=input("Enter Maths Marks:- ")
            EnglishMarks=input("Enter English Marks:- ")
            Record=[Name,Class,PhysicsMarks,ChemistryMarks,ComputerMarks,MathsMarks,EnglishMarks]
            Data.append(Record)
            print("\n\n")
            Ch=input("Want to enter more data (Y/N):- ")
            print("\n\n")
        writer.writerows(Data)
        print("\t\t\t\t\t\t Data Appended Successfully \n\n\n")
def ReadData():
    with open ("demo.csv","r") as file:
        reader=csv.reader(file)
        i=1
        for record in reader:
            print("\n\n\nName of the Student ",i," is :- ",record[0],"\n")
            print("Class of the Student ",i," is :- ",record[1],"\n")
            print("Physics Marks of the Student ",i," is :- ",record[2],"\n")
            print("Chemistry Marks of the Student ",i," is :- ",record[3],"\n")
            print("Computer Science Marks of the Student ",i," is :- ",record[4],"\n")
            print("Maths Marks of the Student ",i," is :- ",record[5],"\n")
            print("English Marks of the Student ",i," is :- ",record[6],"\n\n\n")
            i+=1
        print("\t\t\t\t\t\t Record read Successfully \n\n\n")
def SearchRecord():
    with open("demo.csv","r") as file:
        searcher=csv.reader(file)
        found=False
        Name=input("Enter Name of whom you want to Search Record:- ")
        for rec in searcher:
            if Name==rec[0]:
                found=True
                break
            else:
                found=False
        if found==True:
            print("\n\nRecord of that Student is present in file\n\n\n")
        else:
            print("\n\nRecord of that student does not present in file\n\n\n")
def UpdateRecord():
    file=open("demo.csv","r")
    reader=csv.reader(file)
    Name=input("Enter Name of the Student of whom you want to Update Record:- ")
    Found=False
    for record in reader:
        if Name==record[0]:
            Found=True
            break
        else:
            Found=False
    file.close()
    if Found==False:
        print("\n\n\t\t\t\t\t\tNo Record Found of that Record\n\n")
    else:
        print("\n\n")
        print("Press 1 for update Name \n")
        print("Press 2 for upadte Class \n")
        print("Press 3 for upadte Physics Marks \n")
        print("Press 4 for upadte Chemistry Marks \n")
        print("Press 5 for upadte Computer Science \n")
        print("Press 6 for upadte Maths \n")
        print("Press 7 for upadte English \n")
        Ch=int(input("Enter Your Choice:- "))
        print("\n\n")
        if Ch==1:
            New=input("Enter Updated Name:- ")
            print("\n\n")
        if Ch==2:
            New=input("Enter Updated Class:- ")
            print("\n\n")  
        if Ch==3:
            New=input("Enter Updated Physcis Marks:- ")
            print("\n\n")
        if Ch==4:
            New=input("Enter Updated Chemistry Marks:- ")
            print("\n\n")
        if Ch==5:
            New=input("Enter Updated Computer Science Marks:- ")
            print("\n\n")
        if Ch==6:
            New=input("Enter Updated Maths Marks:- ")
            print("\n\n")
        if Ch==7:
            New=input("Enter Updated English Marks:- ")
            print("\n\n")
        file1=open("demo.csv","r")
        reader1=csv.reader(file1)
        NewData=[]
        for record in reader1:
            if Name==record[0]:
                record[Ch-1]=New
                NewData.append(record)
            else:
                NewData.append(record)
        file1.close()
        with open("demo.csv","w",newline="") as File2:
            writer=csv.writer(File2)
            writer.writerows(NewData)
        print("\t\t\t\t\t\t Record Updated Successfully \n\n\n")
def delete_record():
    file=open("demo.csv","r")
    reader=csv.reader(file)
    Name=input("Enter Name of the Student of whom you want to Delete Record:- ")
    print("\n\n")
    NewData=[]
    for record in reader:
        if Name==record[0]:
            pass
        else:
            NewData.append(record)
    file.close()
    with open("demo.csv","w",newline="") as File:
        writer=csv.writer(File)
        writer.writerows(NewData)
    print("t\t\t\t\t\t Record deleted Successfully \n\n\n")
def MainMenu():
    Choice='Y'
    while Choice=='Y' or Choice=='y':
        print("\n\n\nPress 1 for Append Data in a file\n")
        print("Press 2 for Read Data from a file\n")
        print("Press 3 for Search Record from a file\n")
        print("Press 4 for Update Record in a file\n")
        print("Press 5 for Delete Record from a file\n\n")
        Ch=int(input("Enter Your Choice:- "))
        print("\n\n\n")
        if Ch==1:
            AppendData()
        if Ch==2:
            ReadData()
        if Ch==3:
            SearchRecord()
        if Ch==4:
            UpdateRecord()
        if Ch==5:
            delete_record()
        Choice=input("Want to Perform More Function(Y/N) :- ")
        print("\n")
    print("\n\n\t\t\t\t\t\t\t THANK YOU \n\n\n")
MainMenu()