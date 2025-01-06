try:
    result = 10 / int(input("Enter a number: "))
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Error: {e}")