import os 
import sys 
from check_code import check_code


if __name__ == '__main__':
    print('Welcome to the Pythonify application.\nIn this application, you can '
    'format your Python code to be like as more Pythonic')

    ABSOLUTE_PATH = input('To get started, please enter the absolute path of your Python file.\n')

    if os.path.isfile(ABSOLUTE_PATH) & ABSOLUTE_PATH.endswith('.py'):
        FILE_NAME = os.path.basename(ABSOLUTE_PATH)
        if input(f'File found: {FILE_NAME}, would you like to start formatting?').lower() == 'yes':
            print('Formatting has been started, file is checking.')
            
        else:
            sys.exit(1)
    else:
        print('The path you entered is not a Python file.')
        
