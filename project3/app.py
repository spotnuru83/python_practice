
import PyPDF2, os
from pathlib import Path

def perform_project_3(pdf_file):
    lines = []

    src_file = Path(pdf_file)
    output_dir = src_file.parent.absolute().as_posix() 
    print("Output Directory: " + output_dir)
    output_file  = output_dir + "/output.txt"

    if not src_file.is_file():
        print("Source file is not available, so exiting the program")
        exit()

    page_num = input("Please provide a page number that needs to be saved?")
    page_num = int(page_num)
    page_text = ""
    page_found = False

    with open(pdf_file,'rb') as file:
        content = PyPDF2.PdfReader(file)
        num_of_pages =len(content.pages)

        if page_num < num_of_pages:
            page = content.pages[page_num]
            page_text = page.extract_text()
            page_found = True

    if page_found:
        #print(page_text)

        with open(output_file,"w") as file:
            file.writelines([page_text])         
            print("Page content is written to the output file.")
        pass
    else:
        print("Page number given may not be available in the source PDF file.")


