from lib import MySQLDB, get_config, PDFReader, get_pdf_content, extract_between, extract_before,extract_after, modified
import re


def insert_questions_to_db(questions):
    try:
        if(questions is None or len(questions)==0):
            exit()
        db = MySQLDB()
        db.connect("localhost","root","Welcome#123","actions")

        ### Checking if db reading is working or not.  
        #b.read_query("show databases;")
        db.create_table('''CREATE TABLE IF NOT EXISTS Questions (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            subject VARCHAR(255),
                            chapter VARCHAR(255),                    
                            question VARCHAR(255),
                            option1 VARCHAR(255),
                            option2 VARCHAR(255),
                            option3 VARCHAR(255),
                            option4 VARCHAR(255),
                            answer VARCHAR(255)
                        )''')
        
        ### Checking if db insert statements are working or not.  

        for question in questions: 
            db.insert_record("INSERT INTO Questions (subject, chapter,question, option1, option2, option3, option4, answer) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)",question)
            print(f"Question {question} is inserted successfully.")
            #for reference and the order to follow
            #values = ("Chemistry","Classification of elements and periodicity","What is the SI unit of mass?","Gram (g)"," Kilogram (kg)","Pound (LB)","Ounce (oz)","B)")


        db.close()
        print("Inserted all questions to database")
    except Exception as e:
        print("Error occured during inserting questions in to database.")
    

def get_insert_values(subject, chapter,questions):
    print("Subject:", subject)
    print("Chapter:", chapter)

    values = []
    full_question_pattern = get_config("project5/config.ini","settings","full_question_pattern")
    question_pattern = get_config("project5/config.ini","settings","question_pattern")
    print("Full Question Pattern:" , full_question_pattern)
    print("Only Question Pattern:" , question_pattern)
    # print(questions)
    matches = re.findall(full_question_pattern,questions,re.DOTALL)

    #match contains the questions, options and answer as well.
    for match in matches:

        #q_match should ideally contain only the question without the options and answer. 
        q_matches = re.findall(question_pattern,match, re.DOTALL)
        if(len(q_matches)>0):

            #q has the correct question now. 
            q = modified(q_matches[0]).replace("A)","")
            option1 = extract_between(match, "A)","B)")
            option2 = extract_between(match, "B)","C)")
            option3 = extract_between(match, "C)","D)")
            option4 = extract_between(match, "D)","Answer")
            answer = extract_after(match, "Answer: ")

            
            print("-------------")
            single_question = (subject, chapter, q, option1.strip(), option2.strip(), option3.strip(), option4.strip(), answer.strip())
            # print(single_question)

            values.append(single_question)
    
    return values
    
def extract_data_to_insert(pdf_file_path):
    chapter_pattern  = get_config("project5/config.ini","settings","chapter_name_pattern")
    pages = get_pdf_content(pdf_file_path)
    content = ""
    ins_values = []

    for page in pages:
        content = content + "\n" +page

    chapters = re.findall(chapter_pattern,content,re.MULTILINE)
    num_of_chapters = len(chapters)
    if num_of_chapters>0:
        subject = extract_before(content,chapters[0])
        print(subject)
        
        for i in range(0,num_of_chapters):
            if i < num_of_chapters-1:

                print("#########################################")
                questions = extract_between(content,chapters[i], chapters[i+1])
                qs = get_insert_values(subject, chapters[i], questions)
                ins_values = ins_values+ qs
                print("#########################################")
                
            else:
                print("#########################################")
                questions = extract_after(content,chapters[i])
                qs = get_insert_values(subject,chapters[i],questions)
                ins_values = ins_values+ qs
                print("#########################################")
    
    print(ins_values)
    return ins_values

def perform_project_5(pdf_file_path):

    qs_to_insert = extract_data_to_insert(pdf_file_path)
    insert_questions_to_db(qs_to_insert)
    