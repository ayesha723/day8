def max_value(s):
    max_char = ''  # Start with an empty string as the initial max character
    for char in s:
        if char != ' ' and (max_char == '' or char > max_char):
            max_char = char
    return max_char

# Use the function with the string "Hello World"
result = max_value("hello world")
print(result)
