import os
from lib import PDFReader as PDF
from lib import write_lines_to_file
from pathlib import Path

def get_file_paths(src_path, file_ext):
    pdf_files = []
    for root, dirs, files in os.walk(src_path):
        
        for file in files:
            print (file)
            if file_ext in file:
                pdf_files.append(root+ "/"+file)
        for dir in dirs:
            temp_pdf_files = get_file_paths(dir,file_ext)
            pdf_files = pdf_files + temp_pdf_files

    return pdf_files

def write_pdf_to_files(list_of_files):

    print(len(list_of_files))
    pdf = PDF()
    for file in list_of_files:
        content = pdf.get_pdf_content(file)
        file = Path(file)
        parent_dir = file.parent
        # print(parent_dir)
        dest_file = parent_dir.absolute().as_posix() +"/output.txt"

        # print(dest_file)
        write_lines_to_file(content,dest_file)
        print(f"red the pdf file {file} and stored to {dest_file}")

        pass

# all_pdfs = get_file_paths("content",".pdf")
# write_pdf_to_files(all_pdfs)

# print(all_pdfs)