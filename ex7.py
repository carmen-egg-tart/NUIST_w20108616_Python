# Create a new list called studentNames with the following names
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Use a for loop to print each of these first names followed by the last name "Evans"
print("Original List:")
for name in studentNames:
    print(f"{name} Evans")

# Ask the user to add another name to the list
new_name = input("Please enter another name to add to the list: ")

# Add this name and reprint the list with the last names
studentNames.append(new_name)
print("\nUpdated List:")
for name in studentNames:
    print(f"{name} Evans")
