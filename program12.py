#Write a Python program to count the occurrences of each word in a given sentence

str=input("Enter Line of String: ")
str=str.split()
i=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"Present", count,"Times")

    i=i+1
