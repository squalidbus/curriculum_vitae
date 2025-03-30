import json
from pathlib import Path


filename_input = input("The input filename is: ")
filename_output = input("The output filename is: ")

with open(filename_input, 'r') as json_file:
    cv_data = json.load(json_file)

    with open(filename_output, 'w') as output_file:
        output_file.write("Hello world")
