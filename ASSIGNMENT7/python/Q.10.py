def generate_binary_numbers(n):
    binary_numbers = []  # List to store binary representations
    for i in range(1, n + 1):
        binary_representation = bin(i)[2:]  # Convert to binary and remove '0b'
        binary_numbers.append(binary_representation)
    return binary_numbers

# Test the function
n = 10  # You can change this value to generate binary numbers for different n
binary_numbers = generate_binary_numbers(n)

# Display the results
print(f"Binary numbers from 1 to {n}:")
for num in binary_numbers:
    print(num)
