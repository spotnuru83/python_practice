import os
from pathlib import Path

def write_lines_to_file(lines, to_file):
    print(to_file)
    with open(to_file,"w") as file:
        file.writelines(lines) 

def file_exists ( file_path):
    if os.path.exists(file_path):
        return True
    return False

def get_output_file_path(src_path):
    src_file = Path(src_path)
    output_dir = src_file.parent.absolute().as_posix() 
    print("Output Directory: " + output_dir)
    output_file  = output_dir + "/output.txt"
    return output_file
