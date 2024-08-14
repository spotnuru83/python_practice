import re
import configparser
#import os
from lib import file_exists, PDFReader, get_output_file_path, write_lines_to_file


def get_config(config_file="project4/config.ini", section="settings",attr="regex"):
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
    


def perform_project_4(pdf_file):

    pattern = get_config()
    
    if pattern is None:
        print("Pattern is not provided in configuration file, please provide to extract data accordingly or configuration file is missing. ")
        exit()
    pdf_exists = file_exists(pdf_file)
    
    if(not pdf_exists):
        print("PDF file does not exist, try again")
        exit()

    reader = PDFReader ()
    pages = reader.get_pdf_content(pdf_file)

    matched = []
    for page in pages:
        matches = re.findall(pattern, page,re.MULTILINE )

        if (len(matches)>0):
            matched = matched + matches

        else:
            print("Matches not found")
        #print(page)
    
    if(len(matched)>0):
        output_path = get_output_file_path(pdf_file)
        #print(matched)
        extracted_content = '\n'.join(matched)
        write_lines_to_file(extracted_content,output_path)
        print("Matches found based on the regex and written to the output file. ")
    else:
        print("No matches found based on the regex provided in config file")