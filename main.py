project_num = input("Enter the project number from 1 to 5: ")
project_num = int(project_num)

if project_num >5 or project_num<1 :
    print("Wrong project number, please give within the range ")
    exit()

else:
    match project_num:
        case 1:
            exit()
            
        case 2:
            from project2 import get_file_paths, write_pdf_to_files

            pdfs = get_file_paths("project2/content",".pdf")
            print(pdfs)
            write_pdf_to_files(pdfs)            
            exit()

        case 3:

            from project3 import perform_project_3
            pdf_file = "project3/content/TITAN-Q3-ConCall.pdf"
            perform_project_3(pdf_file)

            exit()

        case 4:
            from project4 import perform_project_4
            pdf_file = "project4/content/TITAN-Q3-ConCall.pdf"
            perform_project_4(pdf_file)
            pass
        case 5:
            from project5 import perform_project_5
            perform_project_5("project5/content/Chemistry Questions.pdf")
            pass