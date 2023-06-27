import csv
import argparse
import re


def search(input_file, query, output_file):
    with open(input_file, 'r', encoding='utf-8') as f, \
            open(output_file, 'w', newline='', encoding='utf-8') as out_f:
        reader = csv.reader(f)
        writer = csv.writer(out_f)
        for row in reader:
            file_name, file_path, text = row
            if re.search(query, text, re.IGNORECASE):
                writer.writerow([file_path, text])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, help='The input CSV file')
    parser.add_argument('--query', required=True, help='The query string')
    parser.add_argument('--output_file', required=True, help='The output CSV file')
    args = parser.parse_args()
    search(args.input_file, args.query, args.output_file)