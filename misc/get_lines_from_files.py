# a script to read files in folder and outputs all lines that match pattern to output file:
# usage: get_lines_from_files.py <input_folder> <output_file> <pattern>
# example: get_lines_from_files.py /home/user/inputs /home/user/output "^[0-9]{1,3}$"

import os, sys, re
from datetime import datetime

if len(sys.argv) != 4:
    input_folder = "./inputs"
    output_file = "output"
    pattern = "new_type_id:10"
else:
    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    pattern = sys.argv[3]

if not os.path.isdir(input_folder):
    print("inputs folder does not exist")
    sys.exit(1)

if os.path.exists(output_file):
    print("output file already exists - using timestamp as filename")
    output_file = output_file + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")

with open(output_file, "w") as f:
    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), "r") as f2:
            for line in f2:
                if re.search(pattern, line):
                    print("adding line: " + line)
                    f.write(line)
                    f.flush()

print("done")
sys.exit(0)

