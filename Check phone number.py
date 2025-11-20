PROGRAM  WITHOUT USING REGULAR EXPRESSION:
def isphonenumber(s):
    if len(s) != 12:
        return False
    if s[3] != '-' or s[7] != '-':
        return False
    if not (s[0:3].isdigit() and s[4:7].isdigit() and s[8:12].isdigit()):
        return False
    return True
print("Without regex:")
print(isphonenumber("415-555-4242"))  
print(isphonenumber("415-55A-4242"))  
print(isphonenumber("415-5555-242"))  


PROGRAM USING REGULAR EXPRESSION:
import re

def isphonenumber_regex(s):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.fullmatch(pattern, s))

print("\nWith regex:")
print(isphonenumber_regex("415-555-4242"))  
print(isphonenumber_regex("415-55A-4242"))  
print(isphonenumber_regex("4155554242"))    
