def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
arr = [34, 8, 64, 51, 32, 21]
print("Original list:", arr)
insertion_sort(arr)
print("Sorted list (Insertion Sort):", arr)
