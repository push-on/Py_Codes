import os
import shutil

folder = input("Enter folder path: ")
files = os.listdir(folder)
print(f"Found {len(files)} files")

while True:
    print("Choose an option:")
    print("1. Check for duplicate file names")
    print("2. Move duplicate file")
    print("3. Delete duplicate file")

    choice = input()

    if choice == '1':
        file_counts = {}
        for filename in files:
            name, ext = os.path.splitext(filename)
            if name in file_counts:
                file_counts[name] += 1
            else:
                file_counts[name] = 1
        duplicate_count = sum(count > 1 for count in file_counts.values())
        print(f"Found {duplicate_count} files with duplicate names.")

        show_duplicates = input("Do you want to see the duplicate file names? (y/n): ")
        if show_duplicates.lower() == 'y':
            print("Duplicate file names:")
            for name, count in file_counts.items():
                if count > 1:
                    print(name, count)

    elif choice == '2':
        dup_counts = {}
        for filename in files:
            name, ext = os.path.splitext(filename)
            if name in dup_counts:
                dup_counts[name].append(filename)
            else:
                dup_counts[name] = [filename]

        dups = {k: v for k, v in dup_counts.items() if len(v) > 1}

        if len(dups) == 0:
            print("No duplicates found")
        else:
            for name, filenames in dups.items():
                biggest_file = max(filenames, key=lambda f: os.path.getsize(os.path.join(folder, f)))
                dest = os.path.join(folder, "duplicates")
                os.makedirs(dest, exist_ok=True)
                shutil.move(os.path.join(folder, biggest_file), dest)

    elif choice == '3':
        dups = {}
        for filename in files:
            name, ext = os.path.splitext(filename)
            if name in dups:
                dups[name].append(filename)
            else:
                dups[name] = [filename]

        dups = {k: v for k, v in dups.items() if len(v) > 1}

        if len(dups) == 0:
            print("No duplicates found")
        else:
            for name, filenames in dups.items():
                biggest_file = max(filenames, key=lambda f: os.path.getsize(os.path.join(folder, f)))
                os.remove(os.path.join(folder, biggest_file))

    again = input("Perform another operation? (y/n) ")
    if again.lower() != 'y':
        break

print("Done")
