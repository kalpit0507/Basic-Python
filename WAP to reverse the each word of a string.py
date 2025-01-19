#WAP to reverse each word in a string
str=input("enter a string")
count=0
lenght=0
if str[-1]=='.':
    print("string before reversing the words is->")
    print(str)
    print()
    print("string after revesing the words is->")
    for i in range(len(str)):
        count+=1
        lenght+=1
        if (str[i]==' ' or str[i]=='.'):
            new_str=''
            for j in range(count-1):
                new_str+=str[-(len(str)-lenght+2)]
                lenght-=1
            lenght+=count-1
            count=0
            print(new_str,end=' ')
else:
    print("Please put full stop in the end of the string")
        
