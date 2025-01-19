#WAP to update a binary file
import pickle
file=open("demo.dat","rb+")
found=False
print("\n\n")
Name=input("Enter Name of the student whom you want to update Details:- ")
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
if Ch==1:
    NewName=input("Enter Updated Name:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[0]=NewName
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found \n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
if Ch==2:
    NewClass=input("Enter Updated Class:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[1]=NewClass
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found \n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated \n\n")
if Ch==3:
    NewPhyscicsMarks=input("Enter Updated Physics Marks:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[2]=NewPhyscicsMarks
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found\n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
if Ch==4:
    NewComputerScienceMarks=input("Enter Updated Marks of Computer Science:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[3]=NewComputerScienceMarks
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found\n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
if Ch==5:
    NewChemistryMarks=input("Enter Updated Chemistry Marks:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[4]=NewChemistryMarks
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found\n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
if Ch==6:
    NewMathsMarks=input("Enter Updated Maths Marks:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[5]=NewMathsMarks
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found\n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
if Ch==7:
    NewEnglishMarks=input("Enter Updated English Marks:- ")
    print("\n\n")
    try:
        while True:
            rpos=file.tell()
            data=pickle.load(file)
            if Name==data[0]:
                data[6]=NewEnglishMarks
                file.seek(rpos)
                pickle.dump(data,file)
                found=True
    except EOFError:
        if found==False:
            print("\n\n\t\t\t\t\t Record not found\n\n")
        else:
            print("\n\n\t\t\t\t\tRecord Updated\n\n")
file.close