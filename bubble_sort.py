# The following program uses the bubble sort algorithm to sort values in ascending order.

# List of submitted entries
entries = [32, 14, 89, 62, 10, 20, 88, 40, 22,  91, 88, 65]


# Function that contains the bubble sort algorithm
def bubble_sort(values):
    # For loop that goes through each list value
    for i in range(len(values) - 1):
        # A nested for loop traverses the list to compare the adjacent value
        for j in range(0, len(values) - 1):
            # If statement that checks if the first value is greater than the second value.
            if values[j] > values[j + 1]:
                # If the first element is greater, then swap places in the list.
                # Otherwise, no swap will occur.
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
    # Return the final list of sorted values
    return values


# Call the function and pass the entries as an argument
print(bubble_sort(entries))