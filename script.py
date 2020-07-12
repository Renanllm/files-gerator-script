import os

input_file = open("files/input-files-name.txt", "r")

files_name_list = []
base_path = "./mfcc"

def convert_files_name_to_list():
    for line in input_file:
        formated_line = line.strip()
        files_name_list.append(formated_line)

def create_base_path_directory():
    os.mkdir(base_path)

def create_directories():
    create_base_path_directory()
    
    for file_name in files_name_list:
        file_path = base_path + "/" + file_name
        os.mkdir(file_path)

convert_files_name_to_list()

create_directories()