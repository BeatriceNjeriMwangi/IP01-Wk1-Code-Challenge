def check_highest_consonant(string):
    vowels = "aeiou"
    consonant_strings = []
    new_string = ""

    for i in string.lower():
        if i not in vowels:
            new_string = new_string + i
        else:
            if new_string:
                consonant_strings.append(new_string)
                new_string = ""

    if new_string:
        consonant_strings.append(new_string)

    return max(check_highest_consonant(string) for string in consonant_string)

print (check_highest_consonant("Animal"))