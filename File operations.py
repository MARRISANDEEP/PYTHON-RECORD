def main():
    filename = input("Enter the filename: ")
 try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("Error: File not found!")
        return

    N = int(input("Enter number of lines to display: "))
    print(f"\nFirst {N} lines of the file:")

    for i in range(N):
        line = file.readline()
        if line == '':
            print("End of file reached.")
            break
        print(line.strip())

    file.close()
    word = input("\nEnter the word to find its frequency: ").lower()

    with open(filename, 'r') as file:
        content = file.read().lower()

    frequency = content.count(word)

    print(f"\nThe word '{word}' occurred {frequency} times in the file.")
main()
