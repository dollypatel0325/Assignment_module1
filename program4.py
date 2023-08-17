#Write python program that swap two number with temp variable and without temp variable.

a = 10
b = 20
print("Before swaping values: ")
print("a: ",a)
print("b: ",b)

#Using third variable name temp

temp = a
a = b
b = temp
print("After swaping values: ")
print("a: ",a)
print("b: ",b)

# Without third variable

a = a+b   #a = 30
b = a-b   #b = 30-20 b = 10
a = a-b   #a = 30-10 a = 20
print("After swaping values: ")

print("a: ",a)
print("b: ",b)
