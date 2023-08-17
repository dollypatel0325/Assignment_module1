#Write a Python program to get the Fibonacci series of given range.

n = int(input("enter how many number you want in series: "))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp+second
