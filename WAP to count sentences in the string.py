#WAP to count sentences in the string
str=input("enter a string")
count=0
for i in str:
    count+=1
sentence_count=0
for j in range(count):
    if str[j]=='.':
        sentence_count+=1
print("sentences present in the string are",sentence_count)
