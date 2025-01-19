#WAP to enter two sorted list and add them into third which should ne also sorted
L1=eval(input("enter first list"))
L2=eval(input("enter second list"))
L3=[]
l1=0
l2=0
if len(L1)>len(L2):
    while len(L2)!=l2:
        if L1[l1]>L2[l2]:
            L3=L3+[L2[l2]]
            l2+=1
        else:
            L3=L3+[L1[l1]]
            l1+=1
    for j in range(l1,len(L1)):
        L3=L3+[L1[j]]
else:
    while len(L1)!=l1:
        if L1[l1]>L2[l2]:
            L3=L3+[L2[l2]]
            l2+=1
        else:
            L3=L3+[L1[l1]]
            l1+=1
    for l in range(l2,len(L2)):
        L3=L3+[L2[l]]
print("Third list with sorted elements is->")
print()
print(L3)
