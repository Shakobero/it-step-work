# Read lines from the first file
with open("1.txt", "r") as file1:
    lines1 = file1.readlines()

# Read lines from the second file
with open("2.txt", "r") as file2:
    lines2 = file2.readlines()

# Merge the lines from both files
merged_lines = lines1 + lines2

# Write the merged lines to a new text file
with open("merged_file.txt", "w") as merged_file:
    merged_file.writelines(merged_lines)

# Read and print the combined file in the terminal
with open("merged_file.txt", "r") as combined_file:
    print(combined_file.read())
