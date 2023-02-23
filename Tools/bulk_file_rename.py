import os

# Take input for the location of the files on the folder
folder_path = input("Enter the path of the folder with the files to rename: ")

# Take input for the text file with all the names which will be used to rename all the files.
names_file_path = input(
    "Enter the path of the text file containing the new names: ")

# Read the new names from the text file
with open(names_file_path) as f:
    new_names = f.readlines()

# Remove whitespace and newlines from the new names
new_names = [name.strip() for name in new_names]

# Check if the number of new names matches the number of files in the directory
if len(new_names) != len(os.listdir(folder_path)):
    print("Error: The number of new names in the text file does not match the number of files in the folder.")
    exit()

# Preview the renamed files
print("Preview of renamed files:")
for i, filename in enumerate(os.listdir(folder_path)):
    # Get the file extension
    ext = os.path.splitext(filename)[1]
    # Construct the new filename with incrementing numbers
    new_filename = f"{i+1:03d}_{new_names[i]}" + ext
    # Print the preview
    print(f"{filename} -> {new_filename}")

# Check for conflicts
conflicts = []
for i, filename in enumerate(os.listdir(folder_path)):
    # Get the file extension
    ext = os.path.splitext(filename)[1]
    # Construct the new filename with incrementing numbers
    new_filename = f"{i+1:03d}_{new_names[i]}" + ext
    # Check if the new filename already exists in the directory
    if os.path.exists(os.path.join(folder_path, new_filename)):
        conflicts.append((filename, new_filename))

# Show conflicts if any
if conflicts:
    print("Conflicts detected:")
    for conflict in conflicts:
        print(f"{conflict[0]} -> {conflict[1]}")

# Confirm with the user if they want to proceed with renaming
confirmation = input("Do you want to proceed with renaming? (y/n): ")
if confirmation.lower() != "y":
    exit()

# Rename all the files
for i, filename in enumerate(os.listdir(folder_path)):
    # Get the file extension
    ext = os.path.splitext(filename)[1]
    # Construct the new filename with incrementing numbers
    new_filename = f"{i+1:03d}_{new_names[i]}" + ext
    # Rename the file
    os.rename(os.path.join(folder_path, filename),
              os.path.join(folder_path, new_filename))

# Success message
print("Files successfully renamed.")
# Open the renamed folder
os.startfile(folder_path)
