#WAP to display longest subtrings comtaining only consonaints
st=input("enter a string:- ")
L=st.split()
greatest=0
largest_st=''
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
