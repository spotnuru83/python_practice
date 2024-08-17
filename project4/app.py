import re

#import os
from lib import file_exists, PDFReader, get_output_file_path, write_lines_to_file, get_config

def perform_project_4(pdf_file):

    pattern = get_config(config_file="project4/config.ini", section="settings",attr="regex")
    
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