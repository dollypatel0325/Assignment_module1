# Write a Python program to get the Factorial number of given number.

n = int(input("Enter the number: "))
result = 1
for i in range(n,0,-1):
    result = result*i

print("Factorial of",n,"is",result)
