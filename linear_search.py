# The following program uses the linear search algorithm to search for specific values.

# List of submitted entries
entries = [32, 14, 89, 62, 10, 20, 88, 40, 22,  91, 88, 65]


# Function that contains the linear search algorithm
def linear_search(values, key):
    # For loop that goes through each list value
    for i in range(len(values)):
        # If statement that checks if the value in entries equals to the key.
        if values[i] == key:
            # Return the index of the searched value
            return i
    # Return an alternative number (-1) if the value isn't found in the list
    return -1


# Call the function and pass the entries and number you're searching for
print(linear_search(entries, 88))