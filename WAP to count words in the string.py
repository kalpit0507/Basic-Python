#WAP to count words in the string
str=input("enter a string")
count=0
for i in str:
    count+=1
word_count=0
for j in range(count):
    if str[j]==' ':
        word_count+=1
print("number of words are",word_count+1)
