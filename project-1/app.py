import PyPDF2, os
from pathlib import Path


def read_pdf_and_write_to(pdf_file_path, write_file_path = ""):
    lines = []

    src_file = Path(pdf_file_path)
    if not src_file.is_file():
        print("Source file is not available, so exiting the program")
        exit()

    dest_path = Path(write_file_path)
    dest_dir = Path(dest_path.parent)
    

    if not dest_dir.is_dir(): 
        os.makedirs(dest_dir)
        print("Created destination folder as it is not present.")
    
    
    with open(pdf_file_path,'rb') as file:


        content = PyPDF2.PdfReader(file)
        num_of_pages =len(content.pages)

        for i in range ( 0, num_of_pages):
            page = content.pages[i]
            text = page.extract_text()

            #print(text)
            if write_file_path!= "":
                lines.append(text)

    if write_file_path!="":
        with open(write_file_path,"w") as file:
            file.writelines(lines) 
        print("Successfully stored the file in the given target file.")


read_pdf_and_write_to("content/TITAN-Q3-ConCall.pdf","content/output.txt")