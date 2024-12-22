# Solutions for Lab: Exploring Type-Specific Methods

# Part 1: String-Specific Methods
# Task 1: Process Log Messages
log_message = "ERROR: Unable to connect to database"

# Normalize the log message using lower()
normalized_message = log_message.lower()

# Check if the log message starts with "error" using startswith()
is_error = log_message.startswith("ERROR")

# Find the position of the word "database" using find()
database_index = log_message.find("database")

# Print the processed results
print("Normalized message:", normalized_message)
print("Starts with 'ERROR':", is_error)
print("Position of 'database':", database_index)

# Part 2: Number-Specific Methods
# Task 2: Process Resource Usage
cpu_usage = 87.6589

# Round the CPU usage to 2 decimal places
rounded_cpu = round(cpu_usage, 2)

# Calculate the remaining capacity
remaining_capacity = abs(100 - cpu_usage)

# Print the results
print("Rounded CPU usage:", rounded_cpu)
print("Remaining capacity:", remaining_capacity)

# Part 3: Combining Methods
# Task 3: Validate User Input
user_input = "8080"

# Check if the input is numeric using isdigit()
is_valid = user_input.isdigit()

if is_valid:
    # Convert the input to an integer and raise it to the power of 2 using pow()
    port_squared = pow(int(user_input), 2)
    print("Port squared:", port_squared)
else:
    print("Invalid input")
