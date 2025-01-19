#Income Tax
Basic_monthly_salary=float(input("Enter input basic monthly salary: "))
print()
HRA=float(input("Enter amount of House Rent Allounce: "))
print()
TA=float(input("Enter amount of Travelling Allounce: "))
print()
DA_rate=float(input("Enter rate of Dearence Allounce: "))
print()
OA=float(input("Enter amount of Other Allounce: "))
print()
DA=Basic_monthly_salary*DA_rate/100
Monthly_Salary=Basic_monthly_salary+HRA+TA+DA+OA
Annual_Income=12*Monthly_Salary
Education_Tution_Fee_Monthly=float(input("Enter Monthly Education Tution Fees: "))
Education_Tution_Fee=12*Education_Tution_Fee_Monthly
print()
Home_Loan=float(input("Enter amount of HomeLoan: "))
print()
Rate_Home_Loan=float(input("Enter rate of home loan: "))
print()
Interest_Homeloan=Home_Loan*Rate_Home_Loan/100
EPF_savings=float(input("Enter savings in Employment Profident Fund: "))
print()
PF_savings=float(input("Enter savings in Profident Fund: "))
print()
Other_Savings=float(input("Enter other savings: "))
print()
Savings=EPF_savings+PF_savings+Other_Savings
if Savings>150000:
    Taxable_Income=Annual_Income-Education_Tution_Fee-Interest_Homeloan-150000
else:
    Taxable_Income=Annual_Income-Education_Tution_Fee-Interest_Homeloan-Savings
age=int(input("Enter Age: "))
print()
print("----------------------------------------------------------------------------")
income_tax=0
tax_1500000=0
tax_1250000=0
tax_1000000=0
tax_750000=0
tax_500000=0
tax_300000=0
tax_250000=0
if Taxable_Income>1500000:
    tax_1500000=Taxable_Income-1500000
    if age>80:
        tax1=tax_1500000*30/100
        income_tax+=tax1
    elif age>60 and age<80:
        tax1=tax_1500000*30/100
        income_tax+=tax1
    else:
        tax1=tax_1500000*30/100
        income_tax+=tax1
if Taxable_Income>1250000:
    tax_1250000=Taxable_Income-1250000-tax_1500000
    if age>80:
        tax2=tax_1250000*30/100
        income_tax+=tax2
    elif age>60 and age<80:
        tax2=tax_1250000*30/100
        income_tax+=tax2
    else:
        tax2=tax_1250000*30/100
        income_tax+=tax2
if Taxable_Income>1000000:
    tax_1000000=Taxable_Income-1000000-tax_1500000-tax_1250000
    if age>80:
        tax3=tax_1000000*30/100
        income_tax+=tax3
    elif age>60 and age<80:
        tax3=tax_1000000*30/100
        income_tax+=tax3
    else:
        tax3=tax_1000000*30/100
        income_tax+=tax3
if Taxable_Income>750000:
    tax_750000=Taxable_Income-750000-tax_1500000-tax_1250000-tax_1000000
    if age>80:
        tax4=tax_750000*20/100
        income_tax+=tax4
    elif age>60 and age<80:
        tax4=tax_750000*20/100
        income_tax+=tax4
    else:
        tax4=tax_750000*20/100
        income_tax+=tax4
if Taxable_Income>500000:
    tax_500000=Taxable_Income-500000-tax_1500000-tax_1250000-tax_1000000-tax_750000
    if age>80:
        tax5=tax_500000*20/100
        income_tax+=tax5
    elif age>60 and age<80:
        tax5=tax_500000*20/100
        income_tax+=tax5
    else:
        tax5=tax_500000*20/100
        income_tax+=tax5
if Taxable_Income>300000:
    tax_300000=Taxable_Income-300000-tax_1500000-tax_1250000-tax_1000000-tax_750000-tax_500000
    if age>80:
        income_tax+=0
    elif age>60 and age<80:
        tax6=tax_300000*5/100
        income_tax+=tax6
    else:
        tax6=tax_300000*5/100
        income_tax+=tax6
if Taxable_Income>250000:
    tax_250000=Taxable_Income-250000-tax_1500000-tax_1250000-tax_1000000-tax_750000-tax_500000-tax_300000
    if age>80:
        income_tax+=0
    elif age>60 and age<80:
        income_tax+=0
    else:
        tax7=tax_250000*5/100
        income_tax+=tax7
if Taxable_Income>0:
    if age>80:
        income_tax+=0
    elif age>60 and age<80:
        income_tax+=0
    else:
        income_tax+=0
print("Basic monthly salary is -> ", Basic_monthly_salary)
print()
print("HRA is -> ",HRA)
print()
print("TA is-> ",TA)
print()
print("DA is-> ",DA)
print()
print("OA is -> ",OA)
print()
print("Monthly Salary after adding all allounces is -> ", Monthly_Salary)
print()
print("Annual Salary is -> ", Annual_Income)
print()
print("Savings in Employment Profident Fund -> ",EPF_savings)
print()
print("Savings in Profident Fund -> ",PF_savings)
print()
print("Other Savings are -> ",Other_Savings)
print()
print("Total Savings are -> ",Savings)
print()
print("Taxable Income is -> ", Taxable_Income)
print()
print("Income Tax is -> ",income_tax)
print()
print("Annual Salary after TAX Deduction is -> ",Annual_Income-income_tax)
print()
print()
print("--------------------- TAX CALCULATED ---------------------")
