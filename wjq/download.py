import argparse
import os


def download(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            file_path, text = line.strip().split(',', 1)
            file_name = os.path.basename(file_path)
            with open(file_name + '.txt', 'w', encoding='utf-8') as out_f:
                out_f.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, help='The input CSV file')
    args = parser.parse_args()
    download(args.input_file)