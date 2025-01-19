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
    New=input("Enter Updated Name:- ")
    print("\n\n")
if Ch==2:
    New=input("Enter Updated Class:- ")
    print("\n\n")
if Ch==3:
    New=input("Enter Updated Physics Marks:- ")
    print("\n\n")
if Ch==4:
    New=input("Enter Updated Computer Science Marks:- ")
    print("\n\n")
if Ch==5:
    New=input("Enter Updated Chemistry Marks:- ")
    print("\n\n")
if Ch==6:
    New=input("Enter Updated Maths Marka:- ")
    print("\n\n")
if Ch==7:
    New=input("Enter Updated English Marks:- ")
    print("\n\n")
try:
    while True:
        rpos=file.tell()
        data=pickle.load(file)
        if Name==data[0]:
            data[Ch-1]=New
            file.seek(rpos)
            pickle.dump(data,file)
            found=True
except EOFError:
    if found==False:
        print("\n\n\t\t\t\t\t Record not found \n\n")
    else:
        print("\n\n\t\t\t\t\tRecord Updated\n\n")
file.close