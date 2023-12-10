def check_highest_consonant(string):
    vowels = "aeiou"
    consonant_strings = []
    new_string = ""
    #loop through
    for i in string.lower():
        if i not in vowels:
            new_string = new_string + i
        else:
            if new_string:
                consonant_strings.append(new_string)
                new_string = ""
    #check last substring of consonant
    if new_string:
        consonant_strings.append(new_string)
    #calculate the value of each consonant string
    values = [sum(ord(c) - ord('a') + 1 for c in substring) for substring in consonant_strings]


    #return highest consonant count
    return max(values, default=0)

print (check_highest_consonant("Animal"))
print (check_highest_consonant("Butterfly"))