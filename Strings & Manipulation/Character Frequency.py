from collections import Counter

text = input("Enter a string: ")

char_count = Counter(text)

for ch, count in char_count.items():
    print(f"'{ch}' : {count}")