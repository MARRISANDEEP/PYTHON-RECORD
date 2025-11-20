def is_binary(s):
    return all(char in '01' for char in s)

def binary_to_decimal(binary_str):
    if is_binary(binary_str):
        decimal = int(binary_str, 2)
        print(f"Binary to Decimal: {binary_str} → {decimal}")
    else:
        print("Invalid binary number. Please enter a number containing only 0s and 1s.")

def is_octal(s):
    return all(char in '01234567' for char in s)

def octal_to_hexadecimal(octal_str):
    if is_octal(octal_str):
        decimal = int(octal_str, 8)
        hexadecimal = hex(decimal)[2:].upper()
        print(f"Octal to Hexadecimal: {octal_str} → {hexadecimal}")
    else:
        print("Invalid octal number. Please enter a number containing digits 0 to 7 only.")


binary_input = input("Enter a binary number: ")
binary_to_decimal(binary_input)

octal_input = input("Enter an octal number: ")
octal_to_hexadecimal(octal_input)
