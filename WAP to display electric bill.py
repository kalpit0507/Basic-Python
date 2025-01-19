#WAP to display electric bill
unit=int(input("enter number of units"))
print("----------------------------------------------")
u5000=0
u1000=0
u100=0
bill=0
if unit>5000:
    u5000=unit-5000
    unit_cost1=10*u5000
    tax1=unit_cost1*25/100
    bill=bill+unit_cost1+tax1
if unit>1000:
    u1000=unit-1000-u5000
    unit_cost2=7*u1000
    tax2=unit_cost2*15/100
    bill=bill+unit_cost2+tax2
if unit>100:
    u100=unit-100-u5000-u1000
    unit_cost3=5*u100
    tax3=unit_cost3*5/100
    bill=bill+unit_cost3+tax3
if unit>0:
    bill+=500
else:
    print("enter valid number of unit")
GST=5*bill/100
service_tax=15*bill/100
total_bill=bill+GST+service_tax+100
print("GST is -> ",GST)
print()
print("Service Tax is -> ",service_tax)
print()
print("Meter tax is -> 100")
print()
print("Total bill is -> ",total_bill)
