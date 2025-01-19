#WAP to calculate age
import datetime
from datetime import date
DOB=eval(input("enter Date of Birth in this format [YYYY,MM,DD]:-"))
CURRENTDATE=str(date.today())
CDATE=CURRENTDATE.split('-')
CDATE[0]=int(CDATE[0])
CDATE[1]=int(CDATE[1])
CDATE[2]=int(CDATE[2])
if DOB[2]>(CDATE[2]):
    (CDATE[2])+=30
    (CDATE[1])-=1
if DOB[1]>(CDATE[1]):
    (CDATE[1])+=12
    (CDATE[0])-=1
AGEDATE=(CDATE[2])-DOB[2]
AGEMONTH=(CDATE[1])-DOB[1]
AGEYEAR=(CDATE[0])-DOB[0]
print("AGE is :- ",AGEYEAR,' years, ',AGEMONTH,' months, ',AGEDATE,' days',)
