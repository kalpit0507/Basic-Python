#WAP to display longest subtrings containing only consonaints
#I want to go gym.
st=input("enter a string:- ")
if st[-1]!='.':
    print("Enter fullstop at the end of the string")
else:
    greatest=0
    largest_st=''
    L=[]
    st1=''
    for i in st:
        if i==' ' or i=='.':
            L.append(st1)
            st1=''
        else:
            st1+=i
    for i in L:
        flag=1
        count=0
        for j in i:
            count+=1
            if j in ('AEIOUaeiou'):
                flag=0
        if flag==1:
            if greatest<count:
                greatest=count
                largest_st=i
    if largest_st=='':
        print("There is no such substring is present, which contains only consonants")
    else:
        print("The largest substring of only consonant is ->")
        print(largest_st)
