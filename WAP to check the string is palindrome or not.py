#WAP to check the palindrome of a string
str=input("enter a string")
count=0
for i in str:
    count+=1
flag=1
j=0
while(j<count/2 and flag==1):
    if str[j]!=str[-(j+1)]:
        flag=0
    j+=1
if flag==1:
    print("the given string '",str,"' is palindrome")
else:
    print("the given string '",str,"' is not a palindrome")
