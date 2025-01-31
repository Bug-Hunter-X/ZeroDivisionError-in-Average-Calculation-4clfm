def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers) 

#Example usage
print(calculate_average([1,2,3])) # Output: 2.0
print(calculate_average([]))      # Output: 0