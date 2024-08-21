from .questions import ObjectiveQuestion, DescriptiveQuestion
from lib import MySQLDB, get_config, PDFReader, get_pdf_content, extract_between, extract_before,extract_after, modified
import re


def get_pdf_full_content(pdf_file_path):
    pages = get_pdf_content(pdf_file_path)
    content = ""

    for page in pages:
        content = content + "\n" +page   

    return content 

def get_chapters_in_content(content):
    chapter_pattern  = get_config("project8/config.ini","settings","chapter_name_pattern")
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

def create_qs(subject, chapter, questions):
    print(subject)
    print(chapter)
    full_question_pattern = get_config("project8/config.ini","settings","full_question_pattern")
    question_pattern = get_config("project8/config.ini","settings","question_pattern")
    matches = re.findall(full_question_pattern,questions,re.DOTALL)
    qs = []
    for match in matches :
        print(" ############################### ")
        #print(match)

        q_matches = re.findall(question_pattern,match, re.DOTALL)
        if(len(q_matches)>0):

            #q has the correct question now. 
            q = modified(q_matches[0]).replace("A)","")
            option1 = extract_between(match, "A)","B)")
            option2 = extract_between(match, "B)","C)")
            option3 = extract_between(match, "C)","D)") 
            option3 = option3 if option3 is not None else "" 
            option4 = extract_between(match, "D)","Answer") 
            option4 = option4 if option4 is not None else ""
            answer = extract_after(match, "Answer: ")        
            newObjQuestion = ObjectiveQuestion(subject, chapter,q )
            newObjQuestion.add_option(1,option1)
            newObjQuestion.add_option(2,option2)
            newObjQuestion.add_option(3,option3)
            newObjQuestion.add_option(4,option4)
            newObjQuestion.add_answser(answer)
            qs.append(newObjQuestion)

            # print(q)
            # print(option1)
            # print(option2)
            # print(option3)
            # print(option4)

            # print(answer)

        else:
            q = extract_before(match, "Answer: ") 
            answer = extract_after(match, "Answer: ") 
            newDescQuestion = DescriptiveQuestion(subject,chapter,q)
            newDescQuestion.add_answser(answer)
            qs.append(newDescQuestion)
            # print(q)
            # print(answer)
        print(" ############################### ")

    return qs

def perform_project_8(pdf_file_path):
    content = get_pdf_full_content(pdf_file_path)
    chapters = get_chapters_in_content(content)
    subject = extract_before(content,chapters[0])
    chapter_number = ask_chapter_to_select(chapters)
    qs = get_chapter_specific_questions(content, chapters,chapter_number)
    qObjs = create_qs(subject,chapters[chapter_number-1],qs)

    print("Number of question objects created: " , len(qObjs))