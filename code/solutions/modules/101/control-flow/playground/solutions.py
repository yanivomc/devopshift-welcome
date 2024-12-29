
# Solution for nestedLoops.py

# Explanation:
# Nested Loops (nestedLoops.py):
# Added messages for outer and inner loop iterations.
# Skips specific iterations using continue.
# Includes a simulation of a 3x3 grid.

print("=== Nested Loops ===")
outer_iterations = 3
inner_iterations = 4

for i in range(outer_iterations):
    print(f"Outer loop iteration {i + 1}")
    for j in range(inner_iterations):
        if j == 2:  # Skip specific inner iteration
            continue
        print(f"  Inner loop iteration {j + 1}")



# Additional nested loop for grid simulation
print("\nSimulating a grid:")
grid_size = 3
for x in range(grid_size):
    for y in range(grid_size):
        print(f"Coordinate: ({x}, {y})")

print("\n")  # Separator for clarity


####

# Solution for oddEven.py
# Classifies numbers into odd, even, and prime groups.
# Stores results in separate lists and prints them.

print("=== Odd, Even, and Prime Numbers ===")
start = 1
end = 20

odd_numbers = []
even_numbers = []
prime_numbers = []

for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    
    # Check for prime numbers
    is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    if is_prime:
        prime_numbers.append(num)

print(f"Odd Numbers: {odd_numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Prime Numbers: {prime_numbers}")
print("\n")  # Separator for clarity


###############


# Solution for rangeLoop.py
# Demonstrates regular and reversed ranges.
# Skips specific numbers using continue.
# Calculates the sum of all numbers in a range.

print("=== Range Loops ===")
# Regular range
print("Regular range output:")
for num in range(1, 10):
    print(num, end=" ")

# Reversed range
print("\nReversed range output:")
for num in range(10, 0, -1):
    print(num, end=" ")

# Skipping numbers
print("\nSkipping certain numbers:")
for num in range(1, 10):
    if num == 5:
        continue
    print(num, end=" ")

# Calculate sum of range
print("\nSum of numbers in range (1-10):")
print(sum(range(1, 11)))

print("\n")  # Separator for clarity







########

# Solution for whileLoops.py
# Automates ping requests with input validation.
# Allows exiting the loop using "exit".
# Implements a retry mechanism with a maximum number of attempts.

print("=== While Loops ===")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter a valid server name (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    elif user_input:
        print(f"Pinging {user_input}... Ping successful.")
    else:
        print("Invalid input. Try again.")
    attempts += 1

if attempts >= max_attempts:
    print("Max attempts reached. Exiting the loop.")


