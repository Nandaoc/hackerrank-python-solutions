def swap_case(s):
    new_string = ""
    for letter in s:
        if letter.islower():
            new_string = new_string + letter.upper()
        if letter.isupper():
            new_string = new_string + letter.lower()
        if not letter.isalnum(): 
            new_string = new_string + letter
        if letter.isdigit():
            new_string = new_string + letter
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)