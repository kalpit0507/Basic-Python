#WAP to reverse the string
str=input("enter a string")
count=0
for i in str:
    count+=1
reverse_str=''
for j in range(count):
    reverse_str=reverse_str+str[-(j+1)]
print("correct order of string is",str)
print("reverse order of string is",reverse_str)
