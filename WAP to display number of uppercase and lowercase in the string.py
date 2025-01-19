#WAP to display number of uppercase and lowercase in the string
Str=input("Enter a string")
upper=0
lower=0
for i in Str:
    if i not in "12345678":
        if i.isupper():
            upper+=1
        else:
            lower+=1
    else:
        upper="can't be calculated"
        lower="can't be calculated"
        print("enter valid string")
        break
print("number of uppercase is",upper)
print("number of lowercase is",lower)
