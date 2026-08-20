def analyze_string(text):
    #counter for each category.
    vowels = 0
    consonants = 0
    digits = 0
    specials = 0
    vowels_set = "aeiouAEIOU"

    # Traverse the string index by index (not just "for ch in text")
    # so we practice index manipulation directly
    i = 0
    while i < len(text):
        ch = text[i]
        code = ord(ch)

        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1

        elif ch.isdigit():
            digits += 1

        elif ch != ' ':
            specials += 1

        i += 1

    return vowels, consonants, digits, specials
text = "Hello World 123 !@#"
v, c, d, s = analyze_string(text)

print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Special characters: {s}")