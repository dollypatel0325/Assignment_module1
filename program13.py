#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


# Get the input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap the first two characters of each string
new_str1 = string2[:2] + string1[2:]
new_str2 = string1[:2] + string2[2:]

# Concatenate the swapped strings with a space in between
result = new_str1 + ' ' + new_str2

# Print the final result
print(result)

