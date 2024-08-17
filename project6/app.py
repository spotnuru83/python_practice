from lib import MySQLDB, get_config, PDFReader, get_pdf_content, extract_between, extract_before,extract_after, modified
import re
    
def get_pdf_full_content(pdf_file_path):
    pages = get_pdf_content(pdf_file_path)
    content = ""

    for page in pages:
        content = content + "\n" +page   

    return content 

def get_chapters_in_content(content):
    chapter_pattern  = get_config("project6/config.ini","settings","chapter_name_pattern")
    chapters = []
    chapters = re.findall(chapter_pattern,content,re.MULTILINE)
    return chapters

def ask_chapter_to_select(chapters):
    print("Here are the chapters available in this document.")
    for chapter in chapters:
        print(chapter)
    chapter_num = int(input("Provide the chapter number for which you want to get the questions:"))

    if chapter_num<1 or chapter_num >len(chapters):
        print("Please select project number next time. ")
        exit()
    return chapter_num
    
def get_chapter_specific_questions(content, chapters, chapter_num):
    chapters_cnt = len(chapters)
    questions_data = ""
    if(chapter_num == chapters_cnt):
        questions_data = extract_after(content,chapters[chapter_num-1])
    elif (chapter_num>0 and chapter_num<chapters_cnt):
        questions_data = extract_between(content, chapters[chapter_num-1],chapters[chapter_num])
    return questions_data
    

def perform_project_6(pdf_file_path):

    content = get_pdf_full_content(pdf_file_path)
    chapters = get_chapters_in_content(content)
    chapter_number = ask_chapter_to_select(chapters)
    qs = get_chapter_specific_questions(content, chapters,chapter_number)
    print(qs)
    