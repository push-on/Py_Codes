import os
import random
import string

try:
    num_files = int(input("How many files do you want to create? "))
    os.makedirs("RandomFiles")

    for i in range(num_files):
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        filename = f"File_{i:02}.txt"
        filepath = os.path.join("RandomFiles", filename)
        with open(filepath, "w") as f:
            text = ''.join(random.choices(string.ascii_lowercase, k=50))
            f.write(text)

    if num_files == len(os.listdir("RandomFiles")):
        print("Done creating files and text with random names.")
    else:
        print("Error: not all files were created.")

except Exception as e:
    print(f"Error creating files: {e}")
