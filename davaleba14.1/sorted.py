import csv

def sort_by_employees(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r', newline='') as infile, open(output_csv_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        sorted_rows = sorted(reader, key=lambda x: int(x[2]), reverse=True)

        writer.writerows(sorted_rows)

    print(f"Sorted information saved to '{output_csv_file}'.")

input_csv_file = 'organizations-100.csv'
output_csv_file = 'sorted_csv.csv'

sort_by_employees(input_csv_file, output_csv_file)

sort_by_employees(input_csv_file, output_csv_file)
