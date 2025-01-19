#WAP to display age
def age(DOB,current_date):
    Num_Days=current_date[0]-DOB[0]
    Num_Months=current_date[1]-DOB[1]
    Num_Years=current_date[2]-DOB[2]
    Age=[Num_Years,Num_Months,Num_Days]
    return Age
DOB=eval(input("Enter Date of birth, in this format-> [DD,MM,YYYY]"))
current_date=eval(input("Enter Current date, in this format-> [DD,MM,YYYY]"))
print()
if DOB[0]>current_date[0]:
    current_date[0]+=30
    current_date[1]-=1
if DOB[1]>current_date[1]:
    current_date[1]+=12
    current_date[2]-=1
if DOB[2]>current_date[2]:
    print("Enter Valid Date")
else:
    AGE=age(DOB,current_date)
    print("Age is ->")
    print(AGE[0],"years ",AGE[1],"months ",AGE[2],"days")
