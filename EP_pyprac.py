# 2. Write a Python function char_frequency(s) that takes a string s as input and returns a dictionary where the keys are characters in the string, and the values are the frequencies of those characters in the string.The function should not be case-sensitive, meaning 'A' and 'a' should be considered the same character.

# Example usage
#input_string = "Hello, World!"
#result = char_frequency(input_string)
#print(result)


# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def char_frequency(s):
    
    frequency_dict = {}

    s = s.lower()

    
    for char in s:
        if char.isalpha():
            # If the character is already in the dictionary, increase it's count
            if char in frequency_dict:
                frequency_dict[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                frequency_dict[char] = 1

    return frequency_dict

# Example usage
input_string = "Hello, World!"
result = char_frequency(input_string)
print(result)
