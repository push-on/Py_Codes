import os
import random
import string

try:
    # Get the number of text files to create from user input
    num_files = int(input("How many files do you want to create? "))

    # Create a directory to store the text files
    os.makedirs("RandomFiles")

    for i in range(num_files):
        # Generate a random name for the text file
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        filename = f"File_{i:02}.txt"
        filepath = os.path.join("RandomFiles", filename)

        # Create the text file with the random name
        with open(filepath, "w") as f:
            # Generate random text without spaces
            text = ''.join(random.choices(string.ascii_lowercase, k=50))
            f.write(text)

    # Check if all files have been created
    if num_files == len(os.listdir("RandomFiles")):
        print("Done creating files and text with random names.")
    else:
        print("Error: not all files were created.")

except Exception as e:
    print(f"Error creating files: {e}")
