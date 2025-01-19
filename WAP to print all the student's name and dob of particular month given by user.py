#WAP to print all the student's name and dob of particular month given by user
def calculate_month(month,nested_L):
    Months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    for i in range(len(Months)):
        if Months[i]==month:
            Month_number=i+1
            if Month_number<10:
                    Monthnumber="0"+str(Month_number)
    for record in nested_L:
        Date_of_birth=record[2]
        dob=Date_of_birth.split('-')
        if dob[1]==Monthnumber:
            print("\n\nName of student:- ",record[1], "\nDate of Birth of student:- ",record[2], "\n\n")
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
Month=input("\n\nEnter month:- ")
calculate_month(Month,Nested_L)