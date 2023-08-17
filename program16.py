#Write a Python function to reverses a string if its length is a multiple of 4
def reverse_string_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]  # Reverse the string using slicing
    else:
        return string

def string_check(data):
    if len(data) %4 == 0:
        return data[::-1]
    return data


text=input("Enter string: ")
result=string_check(text)
print("Final String is:", result)

