test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))
marks = [test1, test2, test3]
marks.sort(reverse=True)
best_two_avg = (marks[0] + marks[1]) / 2
print("The best two test marks are:", marks[0], "and", marks[1])
print("The average of the best two test marks is:", best_two_avg)
