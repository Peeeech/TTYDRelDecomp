import os

# Function to clean up consecutive underscores and remove trailing underscores
def clean_underscores(text):
    while "__" in text:
        text = text.replace("__", "_")
    return text.rstrip("_")  # Remove any trailing underscores
# Ensure the last character before the .txt isn't an underscore
    if filename[-5] == "_":  # -5 because ".txt" takes 4 characters, and we're checking before that
        filename[-5] = ""  # Remove the underscore before ".txt"

# Ask for the prefix once
prefix = input("Enter the prefix: ").replace(" ", "_")
prefix = clean_underscores(prefix)

# Ask for the suffix once (optional)
suffix = input("Enter an optional suffix (or press Enter to skip): ").replace(" ", "_")
suffix = clean_underscores(suffix)

# Ask for the starting number for i, defaulting to 1 if Enter is pressed
start_num_input = input("Enter the starting number for i (or press Enter to start from 1): ")
i = int(start_num_input) if start_num_input.isdigit() else 1

# Infinite loop to ask for the name and create files
while True:
    # Ask for the file name part
    name = input("Enter the name for the file ('q' to quit, 'p' to change prefix, 's' to change suffix, 'i' to change starting number): ").replace(" ", "_")
    name = clean_underscores(name)

    # Break the loop if the user types 'q'
    if name.lower() == 'q':
        print("Exiting program.")
        break

    # Check if the user wants to update the prefix
    if name.lower() == 'p':
        prefix = input("Enter the new prefix: ").replace(" ", "_")
        prefix = clean_underscores(prefix)
        print(f"Prefix updated to: {prefix}")
        continue

    # Check if the user wants to update the suffix
    if name.lower() == 's':
        suffix = input("Enter the new suffix (or press Enter to skip): ").replace(" ", "_")
        suffix = clean_underscores(suffix)
        print(f"Suffix updated to: {suffix}")
        continue

    # Check if the user wants to update the starting number i
    if name.lower() == 'i':
        start_num_input = input("Enter the new starting number for i: ")
        i = int(start_num_input) if start_num_input.isdigit() else i
        print(f"Starting number updated to: {i}")
        continue

    # Construct the file name based on the provided prefix, name, and suffix
    if suffix:
        filename = f"{i} - {prefix}_{name}_{suffix}.txt"
    else:
        filename = f"{i} - {prefix}_{name}.txt"

    # Clean up any double underscores or trailing underscores in the filename
    filename = clean_underscores(filename)

    # Create the blank file
    with open(filename, 'w') as file:
        pass  # Create an empty file

    print(f"Created file: {filename}")

    # Increment the counter
    i += 1
