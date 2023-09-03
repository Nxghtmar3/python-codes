def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    return input_string == input_string[::-1]
