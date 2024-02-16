import csv
def filter_and_save_survivors(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r', newline='') as infile, open(output_csv_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            if row[0] == '100': 
                writer.writerow(row)

    print(f"Survivor information saved to '{output_csv_file}'.")

input_csv_file = 'titanic.csv'
output_csv_file = 'survived.csv'

filter_and_save_survivors(input_csv_file, output_csv_file)
