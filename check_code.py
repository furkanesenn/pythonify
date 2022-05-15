import re 

def check_code(file_path):
    try:
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            for line in lines:
                formatted_line = line.lstrip(' ').rstrip(' ')
                compiled = re.compile(line)
                presented = compiled.match('\B_')
                print(presented)
    except FileNotFoundError:
        print(f'File is not found while trying to open the file. {file_path}')
    return None
