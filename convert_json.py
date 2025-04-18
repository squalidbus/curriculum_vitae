import json
from pathlib import Path


filename_input = input("The input filename is: ")
filename_output = input("The output filename is: ")

with open(filename_input, 'r') as json_file:
    cv_data = json.load(json_file)

    with open(filename_output, 'w') as output_file:

        # latext preamble
        output_file.write((
            "\\documentclass[12pt]{article}\n"
            "\\usepackage[english]{babel}\n"
            "\\usepackae[utf8]{inputenc}\n"
            "\\usepackage{blindtext}\n"
        ))

        # Name/Title
      #  output_file.write(cv_data['name'])

        # Locaton
      #  output_file.write(f"\n{cv_data['location']}")

        # Phone
      #  output_file.write(f"\n{cv_data['phone']}")

        # Email
   #     output_file.write(f"\n{cv_data['email']}")
