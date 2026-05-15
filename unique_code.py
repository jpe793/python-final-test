def unique_code(text):
    code = ""
    for letter in text:
        code += str(ord(letter) + 1) # new feature: shifts each letter
    return code