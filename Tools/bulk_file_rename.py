import os
import natsort

folder_path = input("Folder Path: ")
names_file_path = input("Text File Path: ")

with open(names_file_path) as f:
    new_names = f.readlines()
new_names = [name.strip() for name in new_names]

if len(new_names) != len(os.listdir(folder_path)):
    print("⚠️ error: textfile line number != total files")
    exit()

sorted_filenames = natsort.natsorted(os.listdir(folder_path))
sorted_new_names = natsort.natsorted(new_names)

print("Preview of renamed files: ")
for i, filename in enumerate(sorted_filenames):
    ext = os.path.splitext(filename)[1]
    new_filename = f"{i+1:03d}_{sorted_new_names[i]}" + ext
    print(f"{filename} -> {new_filename}")

conflicts = []
for i, filename in enumerate(sorted_filenames):
    ext = os.path.splitext(filename)[1]
    new_filename = f"{i+1:03d}_{sorted_new_names[i]}" + ext
    if os.path.exists(os.path.join(folder_path, new_filename)):
        conflicts.append((filename, new_filename))

if conflicts:
    print("Conflicts detected: ")
    for conflict in conflicts:
        print(f"{conflict[0]} -> {conflict[1]}")

confirmation = input("Do you want to proceed with renaming? (y/n): ")
if confirmation.lower() != "y":
    exit()

for i, filename in enumerate(sorted_filenames):
    ext = os.path.splitext(filename)[1]
    new_filename = f"{i+1:03d}_{sorted_new_names[i]}" + ext
    os.rename(os.path.join(folder_path, filename),
              os.path.join(folder_path, new_filename))

print("Files successfully renamed.")
os.startfile(folder_path)
