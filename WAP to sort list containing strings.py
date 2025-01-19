#WAP to sort list containing strings
#['Kalpit','Kalpesh','Divij','Deepak','Armaan','kalpit']
def sort_list(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
List=eval(input("Enter a list of strings"))
print("List before sorting is:-")
print(List)
print("------------------------------------------------------------")
print("List after sorting is:-")
print(sort_list(List))
