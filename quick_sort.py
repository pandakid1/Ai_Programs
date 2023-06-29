# The following program uses the quick sort algorithm to sort values in ascending order.
# List of submitted entries
entries = [32, 14, 89, 62, 10, 20, 88, 40, 22,  91, 88, 65]


# Function that iterates through the list and partitions the values
def partition(values, low, high):
    pivot = values[high]
    pointer = low - 1
    # Create a for loop that iterates through all the values
    for i in range(low, high):
        # Compare each list value to the pivot to determine if it belongs in the left or right sub-array
        if values[i] <= pivot:
            pointer += 1
            temp = values[pointer]
            values[pointer] = values[i]
            values[i] = temp
    # Move the pivot to its final position
    temp2 = values[pointer + 1]
    values[pointer + 1] = values[high]
    values[high] = temp2
    # Return the value of the partition
    return pointer + 1

# Function that contains the quick sort algorithm
def quick_sort(values, low, high):
    # Sort the values in the left and right sub-arrays to their final positions.
    if low < high:
        # Call the partition function to find the pivot and divide the list into left or right sub-array
        partition_values = partition(values, low, high)
        # Call the quick_sort function to sort the left sub-array
        quick_sort(values, low, partition_values - 1)
        # Call the quick_sort function to sort the right sub-array
        quick_sort(values, partition_values + 1, high)


# Call the function and pass the entries as an argument
quick_sort(entries, 0, len(entries) - 1)
# Print the sorted list
print(entries)