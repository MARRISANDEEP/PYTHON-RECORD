sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
digit_count = 0
uppercase_count = 0
lowercase_count = 0
for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        uppercase_count += 1
    elif ch.islower():
        lowercase_count += 1
print(f"\nWord Count: {word_count}")
print(f"Digit Count: {digit_count}")
print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
