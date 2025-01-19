import pickle
def add_record():
    file=open("demo.dat","ab")
    ch='Y'
    while ch=='Y' or ch=='y':
        Name=input("Enter Name of Student:- ")
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
add_record()