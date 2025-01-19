#Menu Driven program for performing all binary data
import pickle
def add_record():
    file=open("demo.dat","ab")
    ch='Y'
    while ch=='Y' or ch=='y':
        Name=input("\n\n\nEnter Name of Student:- ")
        Class=int(input("Enter Class of the Student:- "))
        MarkPhy=int(input("Enter Marks of the Student in Physics:- "))
        MarksCS=int(input("Enter Marks of the Student in Computer Science:- "))
        MarksChem=int(input("Enter Marks of the Student in Chemistry- "))
        MarksMaths=int(input("Enter Marks of the Student in Maths:- "))
        MarksEng=int(input("Enter Marks of the Student in English:- "))
        Rec=[Name,Class,MarkPhy,MarksCS,MarksChem,MarksMaths,MarksEng]
        print("\n\n")
        ch=input("Want to Add more Data (Y/N)= ")
        print("\n\n")
        pickle.dump(Rec,file)
    file.close()
    print("\t\t\t\t\t Record has been Appended \n\n\n")
def read_record():
    file=open("demo.dat","rb")
    try:
        print("\n\n")
        i=1
        while True:
            data=pickle.load(file)
            print("Record of Student ",i," is as follow: ")
            print("\n\n")
            print("Name of student is :- ", data[0])
            print("Class of the student is :-", data[1])
            print("Marks of the student in Physics is :- ", data[2])
            print("Marks of the student in Computer Science is :- ", data[3])
            print("Marks of the student in Chemistry is :- ", data[4])
            print("Marks of the student in Maths is :- ", data[5])
            print("Marks of the student in English is :- ", data[6])
            print("\n\n\n")
            i+=1
    except EOFError:
        print("\t\t\t\t\t     All records has been read\n\n\n\n")
    file.close
def update_record():
    file=open("demo.dat","rb")
    Record=[]
    try:
        print("\n\n")
        name=input("Enter Name in which Record has to be Updated:- ")
        print("\n\n")
        print("Press 1 for update Name \n")
        print("Press 2 for upadte Class \n")
        print("Press 3 for upadte Physics Marks \n")
        print("Press 4 for upadte Computer Science Marks \n")
        print("Press 5 for upadte Chemistry \n")
        print("Press 6 for upadte Maths \n")
        print("Press 7 for upadte English \n")
        Ch=int(input("Enter Your Choice:- "))
        print("\n\n")
        while True:
            data=pickle.load(file)
            if data[0]==name:
                if Ch==1:
                    NewName=input("Enter Name to be updated:- ")
                    data[0]=NewName
                if Ch==2:
                    NewClass=int(input("Enter New Class:- "))
                    data[1]=NewClass
                if Ch==3:
                    NewPhyscicsMarks=int(input("Enter Marks of Physics to be updated:- "))
                    data[2]=NewPhyscicsMarks
                if Ch==4:
                    NewCSMarks=int(input("Enter Marks of Computer Science to be updated:- "))
                    data[3]=NewCSMarks
                if Ch==5:
                    NewChemistryMarks=int(input("Enter Marks of Chemistry to be updated:- "))
                    data[4]=NewChemistryMarks
                if Ch==6:
                    NewMathsMarks=int(input("Enter Marks of Maths to be updated:- "))
                    data[5]=NewMathsMarks
                if Ch==7:
                    NewEnglishMarks=int(input("Enter Marks of English to be updated:- "))
                    data[6]=NewEnglishMarks
                Record.append(data)
            else:
                Record.append(data)
    except EOFError:
        pass
    print("\n\n")
    file.close()
    newfile=open("demo.dat","wb")
    for records in Record:
        pickle.dump(records,newfile)
    newfile.close()
    print("\t\t\t\t\t     Record has been Updated \n\n\n")
def delete_record():
    file=open("demo.dat","rb")
    Record=[]
    try:
        print("\n\n")
        name=input("Enter Name of whose Record has to be Deleted:- ")
        print("\n\n")
        while True:
            data=pickle.load(file)
            if data[0]==name:
                pass
            else:
                Record.append(data)
    except EOFError:
        pass
    print("\n\n")
    file.close()
    newfile=open("demo.dat","wb")
    for records in Record:
        pickle.dump(records,newfile)
    newfile.close()
    print("\t\t\t\t\t Record has been Deleted \n\n\n")
def mainmenu():
    choice='Y'
    while choice=='y' or choice=='Y':
        print("\n\nPress 1 for Read Binary File \n")
        print("Press 2 for Append Record in Binary File \n")
        print("Press 3 for Update Record in Binary File \n")
        print("Press 4 for Delete Record in Binary File \n")
        ch=int(input("Enter Your Choice :- "))
        if ch==1:
            read_record()
        elif ch==2:
            add_record()
        elif ch==3:
            update_record()
        elif ch==4:
            delete_record()
        choice=input("Want to do Other Work (Y/N) :- ")
    print("\n\n\t\t\t\t\t      All works completed")
mainmenu()