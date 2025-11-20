class PalindromeChecker:
    def is_palindrome(self, value):
        raise NotImplementedError("Subclasses should implement this!")
class StringPalindromeChecker(PalindromeChecker):
    def is_palindrome(self, value):
        value = value.lower().replace(" ", "") 
        return value == value[::-1]
class IntegerPalindromeChecker(PalindromeChecker):
    def is_palindrome(self, value):
        str_value = str(value)
        return str_value == str_value[::-1]
input_value = input("Enter a value (string or integer): ")

if input_value.isdigit():
    checker = IntegerPalindromeChecker()
    is_pal = checker.is_palindrome(int(input_value))
else:
    checker = StringPalindromeChecker()
    is_pal = checker.is_palindrome(input_value)
if is_pal:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
