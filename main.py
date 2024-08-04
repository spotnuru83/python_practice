from project2 import get_file_paths, write_pdf_to_files


pdfs = get_file_paths("project2/content",".pdf")
print(pdfs)
write_pdf_to_files(pdfs)