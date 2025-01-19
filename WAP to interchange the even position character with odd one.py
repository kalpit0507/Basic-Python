#WAP to interchange the even position character with odd one
str=input("enter a string")
new_str=''
for i in range(len(str)):
    if i%2==0:
        new_str=new_str+str[i+1]
        new_str=new_str+str[i]
print("string before interchanging is",str)
print( )
print("string after interchanging is",new_str)
