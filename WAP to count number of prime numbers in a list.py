#WAP to count number of prime numbers in a list
li=eval(input("Enter list:- "))
nl=[]
s=0
for num in li:
    if num<=1:
        continue
    for i in range(2,int(num/2 + 1)):
        if num%i==0:
            break
    else:
        nl.append(num)
        s+=1
print("Number of prime numbers are:- ",s)
print("List of prime numbers is:- ",nl)
