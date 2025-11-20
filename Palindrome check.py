num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
digit_count = {}

for digit in num:
    if digit.isdigit():  
        digit_count[digit] = digit_count.get(digit, 0) + 1

print("\nDigit Occurrence Count:")
for digit in sorted(digit_count):
    print(f"Digit {digit} occurs {digit_count[digit]} time(s)")
