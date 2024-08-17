import os
from pathlib import Path
import configparser
import pdfplumber

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

def get_config(config_file , section ,attr):
    value = None
    try:
        # Initialize the ConfigParser
        config = configparser.ConfigParser(interpolation=None)
        #if os.path.exists(config_file):
        if file_exists(config_file):
            print("File exists")
        else:
            print("File does not exists")
            exit()
        # Read the configuration file
        config.read(config_file)

        if section in config:
            print("------------------- Section Exists ----------------")
        else:
            print("------------------- Section does not Exists ----------------")
        # Access a specific value
        value =  config[section][attr]
    except Exception as e:
        print(f"Key {attr} does not exist in the configuration file or configruation file does not exist.")

    return value  

def get_pdf_content(file_path):
    pages = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # print(page.extract_text())
            pages.append(page.extract_text())

    return pages