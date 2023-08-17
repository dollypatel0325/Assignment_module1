#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def replace_substring(string):
    index_not = string.find('not')
    index_poor = string.find('poor')
    
    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        return string[:index_not] + 'good' + string[index_poor + 4:]
    
    return string

# Example usage
input_string = "The weather is not too poor today."
result = replace_substring(input_string)
print(result)


