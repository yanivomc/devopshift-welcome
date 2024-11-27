import csv
import json

def csv_to_es_bulk():
    # Ask user for input and output filenames
    source_file = input("Please provide the source CSV filename with its path: ")
    output_file = input("Please provide the desired output filename: ")

    # Read the first line of the CSV to determine the number of columns and their headers
    with open(source_file, 'r') as f:
        first_line = f.readline().strip().split(',')
        num_columns = len(first_line)
        print(f"Your CSV has {num_columns} columns. The first row looks like this:\n{first_line}")

    # Ask the user for column titles
    user_columns = input(f"Please provide {num_columns} comma-separated column titles or leave blank for generic titles: ").split(',')

    # Validate and process user input
    if len(user_columns) != num_columns:
        print("You provided a different number of column titles. Using generic titles for the remaining columns.")
        user_columns += [f"title{i+1}" for i in range(len(user_columns), num_columns)]

    # Read the CSV and convert to Elasticsearch _bulk JSON format
    with open(source_file, mode='r') as infile, open(output_file, mode='w') as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
            # Each document in a _bulk API needs an index action line before the actual data
            action_metadata = json.dumps({"index": {}})
            movie_data = {}
            for col in user_columns:
                movie_data[col] = row[col]
            outfile.write(action_metadata + "\n" + json.dumps(movie_data) + "\n")

    print(f"Data has been transformed and saved into {output_file}.")

if __name__ == "__main__":
    csv_to_es_bulk()

