#WAP to dilplay sum of series, 2**3/3! + 4**5/5! + ...., using fucntion
def pow(x,y):
    power=1
    for i in range(y):
        power=power*x
    return power
def fact(num):
    f=1
    for j in range(1,num+1):
        f=f*j
    return f
a=int(input("enter last base"))
k=2
s=0
while k<=a:
    numerator=pow(k,k+1)
    denominator=fact(k+1)
    term=numerator/denominator
    s+=term
    k+=2
print("sum of series, 2**3/3! + 4**5/5! + .... , is ->")
print(s)
    
