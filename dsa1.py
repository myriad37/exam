def count_occurrences(numbers, search_number):
    count = 0
    for i in numbers:
        if i == search_number:
            count += 1
    return count

# Input sequence of numbers
sequence = input("Enter the sequence of numbers (space-separated): ")
numbers = list(map(int, sequence.split()))

# Number to search
search_number = int(input("Enter the number to be searched: "))

# Search and count occurrences
occurrences = count_occurrences(numbers, search_number)

# Display the result
if occurrences > 0:
    print(f"The number {search_number} appears {occurrences} time(s) in the array.")
else:
    print(f"The number {search_number} is not found in the array.")