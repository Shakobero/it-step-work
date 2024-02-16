def create_and_write_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.writelines(f"Line {i}: This is line number {i}\n" for i in range(1, 1001))
    except Exception as e:
        print(f"Error: {e}")

def count_filled_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except Exception as e:
        print(f"Error: {e}")
        return 0

file_path = 'example.txt'
create_and_write_file(file_path)
filled_lines = count_filled_lines(file_path)
print("Number of lines filled:", filled_lines)
