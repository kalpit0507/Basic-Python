#WAP to print the data of student up to age given by user
from datetime import date
def age_print(age,Nested_L):
    Today=date.today()
    today=str(Today)
    TODAY=today.split('-')
    for record in Nested_L:
        Date_of_birth=record[2]
        dob=Date_of_birth.split('-')
        Year=int(TODAY[0])-int(dob[2])
        if int(TODAY[1])<int(dob[1]):
            Age=Year-1
        elif int(TODAY[1])==int(dob[1]):
            if int(TODAY[2])<int(dob[0]):
                Age=Year-1
            else:
                Age=Year
        else:
            Age=Year
        if Age<age:
            print("Reg number of student is:- ",record[0])
            print("Name of sudent is:- ",record[1])
            print("Date of birth of student is:- ",record[2],"\n\n\n")
Nested_L=[]
ch='y'
while ch=='Y' or ch=='y':
    Li=[]
    reg_no=input("Enter reg no:- ")
    Name=input("Enter Name:- ")
    DOB=input("Enter Date of birth in this format 'DD-MM-YYYY':-  ")
    print()
    Li=[reg_no,Name,DOB]
    Nested_L.append(Li)
    ch=input("Want to enter more data (Y/N):- ")
    print()
age=int(input("\n\nEnter age:- "))
print("\n\n\n")
age_print(age,Nested_L)