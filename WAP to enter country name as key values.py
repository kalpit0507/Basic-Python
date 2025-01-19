#WAP to enter country name as key values and capital and population(in form of list) as values in dictionary
#Also create a new dictionary in which lenght of capital is key and population is values
D={}
ch='Y'
print("\n\n\n\n")
while ch=='Y' or ch=='y':
    Val=[]
    CoName=input("Enter Country Name:- ")
    CaName=input("Enter Captital of the Country:- ")
    Population=int(input("Enter Population:- "))
    Val.append(CaName)
    Val.append(Population)
    D[CoName]=Val
    print("\n\n")
    ch=input("Want to enter more data(Y/N):- ")
    print("\n\n")
print("Dictionary after adding records is:- ")
print(D)
print("\n\n\n\n")
def NewDic(D):
    Vals=list(D.values())
    NewD={}
    for i in Vals:
        Keys=list(NewD.keys())
        lenghtC=len(i[0])
        while lenghtC in Keys:
            lenghtC+=1
            NewD[lenghtC]=i[1]
        else:
            NewD[len(i[0])]=i[1]
    print("New Dictionary is where lenght of Capital is key and Popualation is value:- ")
    print(NewD)
NewDic(D)