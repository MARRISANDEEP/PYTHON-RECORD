import re

def extract_contacts(filename):
    with open(filename, 'r') as file:
        content = file.read()
    phone_pattern = r"\+91\d{10}"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phones = re.findall(phone_pattern, content)
    emails = re.findall(email_pattern, content)

    print("Phone Numbers Found:")
    for phone in phones:
        print(phone)

    print("\nEmail Addresses Found:")
    for email in emails:
        print(email)

extract_contacts("sample.txt")  
