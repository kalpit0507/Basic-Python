#WAP to display positive integers in list in desending order on left side
#negative integers in list in asending order on right side
#[5,2,3,7,-5,-1,-2,4,-6,10,12]
L=eval(input("Enter a list"))
for i in range(len(L)):
    for j in range(len(L)-i-1):
        if L[j]<L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
count=0
while L[count]>=0:
    count+=1
for k in range(count,len(L)):
    for l in range(count,len(L)-1):
        if L[l]>L[l+1]:
            L[l],L[l+1]=L[l+1],L[l]
print("List after sorting is ->")
print(L)
