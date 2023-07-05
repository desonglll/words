import os
import csv
import codecs

def convert_csv_encoding_to_utf8(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    with open(file_path, 'w', encoding='utf-8-sig') as file:
        file.write(content)

def convert_csv_files_in_directory(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory, file_name)
            convert_csv_encoding_to_utf8(file_path)
            print(f"Converted: {file_path}")

# 设置当前目录
directory = os.getcwd()
# 转换CSV文件编码格式为UTF-8
convert_csv_files_in_directory(directory)

