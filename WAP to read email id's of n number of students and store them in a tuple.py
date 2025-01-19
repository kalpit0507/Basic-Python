#WAP to read email id's of n number of students and store them in a tuple
#Create two new tuples, one to store only username from the email ids
#second to store the domain names from the email ids
n=int(input("Enter number of students"))
email=[]
username=[]
domain_name=[]
for i in range(n):
    Username=''
    Domain_name=''
    count=0
    Email=input("Enter email of student")
    for j in Email:
        count+=1
        if j=='@':
            break
    for k in range(count-1):
        Username+=Email[k]
    for l in range(count,len(Email)):
        Domain_name+=Email[l]
    email.append(Email)
    username.append(Username)
    domain_name.append(Domain_name)
EMail=tuple(email)
UserName=tuple(username)
Domain_Name=tuple(domain_name)
print("Emails of students are ->")
print(EMail)
print()
print("Usernames of students are->")
print(UserName)
print()
print("Domain Name of students are->")
print(Domain_Name)
