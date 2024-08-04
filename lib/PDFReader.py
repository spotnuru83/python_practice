import PyPDF2
class PDFReader:
    def __init__(self):
        pass

    def get_pdf_content(self,pdf_file_path):
        lines = []

        with open(pdf_file_path,'rb') as file:


            content = PyPDF2.PdfReader(file)
            num_of_pages =len(content.pages)

            for i in range ( 0, num_of_pages):
                page = content.pages[i]
                text = page.extract_text()

                lines.append(text)        
        return lines
    
    