# Solutions for Lab: Practicing Augmented Assignments

# Part 1: Basic Operations with Augmented Assignments
# Task 1: Log File Counter
line_count = 0
for _ in range(100):
    line_count += 1  # Increment line_count for each processed line
print("Line count:", line_count)  # Output: 100

# Part 2: Resource Scaling with Augmented Assignments
# Task 2: Scaling CPU Usage
cpu_usage = 50.0
cpu_usage += 10.0  # Increase by 10%
print("After increase:", cpu_usage)  # Output: 60.0

cpu_usage -= 5.0  # Decrease by 5%
print("After decrease:", cpu_usage)  # Output: 55.0

# Part 3: Floor Division and Modulus
# Task 3: Paginate Logs
log_entries = 245
page_size = 50

# Calculate full pages
full_pages = log_entries // page_size
remaining_logs = log_entries % page_size

print("Full pages:", full_pages)  # Output: 4
print("Remaining logs:", remaining_logs)  # Output: 45

# Part 4: Exponentiation in Metrics
# Task 4: Exponential Growth
metric = 2
metric **= 3  # Raise to the power of 3
print("Metric value:", metric)  # Output: 8
