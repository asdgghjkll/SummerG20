import os
import glob
import csv
import argparse
import re
import io
import PyPDF2
from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        # 使用 io.BytesIO 将文件对象转换为字节流对象
        pdf_bytes = io.BytesIO(f.read())
        # 使用 PdfReader 读取字节流对象中的 PDF 文档
        pdf_reader = PdfReader(pdf_bytes)
        text = ''
        # 遍历每一页，获取文本内容
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text


def extract_text_from_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().decode('utf-8', 'ignore')
    else:
        return ''


def build_index(input_dir, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for file_path in glob.glob(os.path.join(input_dir, '**/*'), recursive=True):
            if os.path.isfile(file_path):
                text = extract_text_from_file(file_path)
                if text:
                    file_name = os.path.basename(file_path)
                    writer.writerow([file_name, file_path, text])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True, help='The input directory')
    parser.add_argument('--output_file', required=True, help='The output CSV file')
    args = parser.parse_args()
    build_index(args.input_dir, args.output_file)