#WAP to count the lenght of the each word in the string
str=input("enter a string")
count=0
j=1
for i in range(len(str)):
    count+=1
    if (str[i]==' ' or str[i]=='.'):
        print("lenght of",j,"st word is",count-1)
        count=0
        j+=1
