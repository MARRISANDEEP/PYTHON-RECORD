string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
min_len = min(len(string1), len(string2))
max_len = max(len(string1), len(string2))
match_count = 0
for i in range(min_len):
    if string1[i] == string2[i]:
        match_count += 1
similarity = (match_count / max_len) * 100
print(f"String similarity: {similarity:.2f}%")
