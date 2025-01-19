#WAP to count the vowels in the string
str=input("enter a string")
vcount=0
for i in str:
    if i in 'AEIOUaeiou':
        vcount+=1
print("number of vowels are",vcount)
