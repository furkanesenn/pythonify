import os 

def check_code(file_path):
    try:
        with open(file_path, 'r+') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f'File is not found while trying to open the file. {file_path}')
    return 0
