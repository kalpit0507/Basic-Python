#WAP to display income tax using function
import os
import colorama
from colorama import Back, Fore, Style

def tax_slab1(tax_1500000):
    tax1=tax_1500000*30/100
    income_tax=tax1
    return income_tax

def tax_slab2(tax_1250000):
    tax2=tax_1250000*30/100
    income_tax=tax2
    return income_tax

def tax_slab3(tax_1000000):
    tax3=tax_1000000*30/100
    income_tax=tax3
    return income_tax

def tax_slab4(tax_750000):
    tax4=tax_750000*20/100
    income_tax=tax4
    return income_tax

def tax_slab5(tax_500000):
    tax5=tax_500000*20/100
    income_tax=tax5
    return income_tax

def tax_slab6(tax_300000):
    tax6=tax_300000*5/100
    income_tax=tax6
    return income_tax

def tax_slab7(tax_200000):
    tax7=tax_250000*5/100
    income_tax=tax7
    return income_tax

def tax_slab8():
    income_tax=0
    return income_tax

def print_func():
    os.system('cls')
    print()
    print("Basic Monthly Salary is                             :-> ", Basic_monthly_salary)
    print()
    print("Monthly House Rent Allounce is                      :-> ",HRA)
    print()
    print("Monthly Travel Allounce is                          :-> ",TA)
    print()
    print("Monthly Dearence Allounce is                        :-> ",DA)
    print()
    print("Monthly Other Allounce is                           :-> ",OA)
    print()
    print("Monthly Salary After Adding All Allounces is        :-> ", Monthly_Salary)
    print()
    print("Annual Salary is                                    :-> ", Annual_Income)
    print()
    print("Yearly Savings in Employment Profident Fund         :-> ",EPF_savings)
    print()
    print("Yearly Savings in Profident Fund                    :-> ",PF_savings)
    print()
    print("Yearly Other Savings are                            :-> ",Other_Savings)
    print()
    print("Yearly Total Savings are                            :-> ",Savings)
    print()
    print("Monthly Taxable Income is                           :-> ", Taxable_Income/12)
    print()
    print("Yearly Taxable Income is                            :-> ", Taxable_Income)
    print()
    print("Monthly Income Tax is                               :-> ",TAX/12)
    print()
    print("Yearly Income Tax is                                :-> ",TAX)
    print()
    print("Monthly Salary after TAX Deduction is               :-> ",(Annual_Income-TAX)/12)
    print()
    print("Annual Salary after TAX Deduction is                :-> ",Annual_Income-TAX)
    print()
    print()
    print("---------------------------------------------------------------------------------------------------------------------")
    print()
    print("                                     |||  T A X - C A L C U L A T E D  ||| ")
    print()
    print("---------------------------------------------------------------------------------------------------------------------")

os.system('cls')
print()
print("---------------------------------------------------------------------------------------------------------------------")
print()
print("                                            |||  I N C O M E - T A X  ||| ")
print()
print("---------------------------------------------------------------------------------------------------------------------")
print()

Basic_monthly_salary=float(input("Enter Basic Monthly Salary                          :-> "))
print()
HRA=float(input("Enter Amount of Monthly House Rent Allounce         :-> "))
print()
TA=float(input("Enter Amount of Monthly Travelling Allounce         :-> "))
print()
DA_rate=float(input("Enter Rate of Monthly Dearence Allounce             :-> "))
print()
OA=float(input("Enter Amount of Other Monthly Allounce              :-> "))
print()

#*********Computation of Annual salary*********************************

DA=Basic_monthly_salary*DA_rate/100
Monthly_Salary=Basic_monthly_salary+HRA+TA+DA+OA
Annual_Income=12*Monthly_Salary

#**************Calcuation of Various Deduction*************************

Education_Tution_Fee_Monthly=float(input("Enter Monthly Education Tution Fees                 :-> "))
Education_Tution_Fee=12*Education_Tution_Fee_Monthly
print()
Monthly_EMI_Homeloan=float(input("Enter Monthly EMI of homeloan                       :-> "))
print()
Rate_Homeloan=float(input("Enter Rate of Homeloan                              :-> "))
print()
Monthly_Interest_Homeloan=Monthly_EMI_Homeloan*Rate_Homeloan/100
Yearly_Interest_Homeloan=12*Monthly_Interest_Homeloan
Monthly_EPF_savings=float(input("Enter Monthly Savings in Employment Profident Fund  :-> "))
EPF_savings=12*Monthly_EPF_savings
print()
Monthly_PF_savings=float(input("Enter Monthly Savings in Profident Fund             :-> "))
PF_savings=12*Monthly_PF_savings
print()
Monthly_Other_Savings=float(input("Enter Monthly Other Savings                         :-> "))
Other_Savings=12*Monthly_Other_Savings
print()
Savings=EPF_savings+PF_savings+Other_Savings
if Savings>150000:
    Taxable_Income=Annual_Income-Education_Tution_Fee-Yearly_Interest_Homeloan-150000
else:
    Taxable_Income=Annual_Income-Education_Tution_Fee-Yearly_Interest_Homeloan-Savings
age=int(input("Enter Age                                           :-> "))
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("---------------------------------------------------------------------------------------------------------------------")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

tax_1500000=0
tax_1250000=0
tax_1000000=0
tax_750000=0
tax_500000=0
tax_300000=0
tax_250000=0
TAX=0

if Taxable_Income>1500000:
    tax_1500000=Taxable_Income-1500000
    if age>80:
        TAX+=tax_slab1(tax_1500000)
    elif age>60 and age<80:
        TAX+=tax_slab1(tax_1500000)
    else:
        TAX+=tax_slab1(tax_1500000)

if Taxable_Income>1250000:
    tax_1250000=Taxable_Income-1250000-tax_1500000
    if age>80:
        TAX+=tax_slab2(tax_1250000)
    elif age>60 and age<80:
        TAX+=tax_slab2(tax_1250000)
    else:
        TAX+=tax_slab2(tax_1250000)

if Taxable_Income>1000000:
    tax_1000000=Taxable_Income-1000000-tax_1500000-tax_1250000
    if age>80:
        TAX+=tax_slab3(tax_1000000)
    elif age>60 and age<80:
        TAX+=tax_slab3(tax_1000000)
    else:
        TAX+=tax_slab3(tax_1000000)

if Taxable_Income>750000:
    tax_750000=Taxable_Income-750000-tax_1500000-tax_1250000-tax_1000000
    if age>80:
        TAX+=tax_slab4(tax_750000)
    elif age>60 and age<80:
        TAX+=tax_slab4(tax_750000)
    else:
        TAX+=tax_slab4(tax_750000)

if Taxable_Income>500000:
    tax_500000=Taxable_Income-500000-tax_1500000-tax_1250000-tax_1000000-tax_750000
    if age>80:
        TAX+=tax_slab5(tax_500000)
    elif age>60 and age<80:
        TAX+=tax_slab5(tax_500000)
    else:
        TAX+=tax_slab5(tax_500000)

if Taxable_Income>300000:
    tax_300000=Taxable_Income-300000-tax_1500000-tax_1250000-tax_1000000-tax_750000-tax_500000
    if age>80:
        TAX+=tax_slab8()
    elif age>60 and age<80:
        TAX+=tax_slab6(tax_300000)
    else:
        TAX+=tax_slab6(tax_300000)

if Taxable_Income>250000:
    tax_250000=Taxable_Income-250000-tax_1500000-tax_1250000-tax_1000000-tax_750000-tax_500000-tax_300000
    if age>80:
        TAX+=tax_slab8()
    elif age>60 and age<80:
        TAX+=tax_slab8()
    else:
        TAX+=tax_slab7(tax_250000)

if Taxable_Income>0:
    if age>80:
        TAX+=tax_slab8()
    elif age>60 and age<80:
        TAX+=tax_slab8()
    else:
        TAX+=tax_slab8()

print_func()
