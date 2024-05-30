def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Each pass will move the largest element to the end, so we can reduce the inner loop iterations
        for j in range(n - 1 - i):
            # Compare adjacent elements and swap if necessary
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
alphabets = ['e', 'b', 'd', 'a', 'c']
print("Before sorting:", alphabets)

bubble_sort(alphabets)

print("After sorting:", alphabets)