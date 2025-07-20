# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Use while loop for rows and for loop for columns to draw pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
