#WAP to capatilize first character in a list of string
L=eval(input("enter a list"))
L1=[]
for i in L:
    st=''
    if ord(i[0])>=65 and ord(i[0])<=90:
        st+=i
    elif ord(i[0])>=97 and ord(i[0])<=122:
        character=chr(ord(i[0])-32)
        st+=character
        for j in range(1,len(i)):
             st+=i[j]
    L1.append(st)
print("List before capatilizing is -> ",)
print(L)
print("List after capatilizing is -> ",)
print(L1)
