def generate_fibonacci(n):
    # Starting values
    sequence = [0, 1]
    
    # Loop to calculate the next numbers
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:n]

# Change this number to see more or fewer results
count = 10
print(f"The first {count} Fibonacci numbers are:")
print(generate_fibonacci(count))