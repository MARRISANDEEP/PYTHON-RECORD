def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

N = input("Enter the number of terms (N > 0): ")

if N.isdigit():
    N = int(N)
    if N > 0:
        fibonacci(N)
    else:
        print("Invalid input. Please enter a number greater than 0.")
else:
    print("Invalid input. Please enter a positive integer.")
