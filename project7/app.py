import threading
import time
import feedparser
from lib import write_lines_to_file, replace_special_chars_with

def read_content(url):
    try:
        feed = feedparser.parse(url)
        content = ""
        output_file = ""
        for entry in feed.entries:
            content = content + "\nArticle Title:" + entry.title + "\n"
            content = content + "Published Date:" + entry.published + "\n"
            content = content + "Link:"+ entry.link + "\n"
            content = content + "Summary:" + entry.summary + "\n-------------------\n"

        #print(content)
        
        output_file = f"project7/content/output_{replace_special_chars_with(feed.feed.title)}.txt"
        write_lines_to_file(content, output_file)
        print("Feed written to outout file :  " , output_file)
    except Exception as e:
        print("----------------------------Error-----------------------")
        print(f"Error occurred to read and write the feed to output file : {output_file}")
        print(e)
        print("--------------------------------------------------------")



def perform_project_7():
    # urls = ["https://testingtools.co","https://google.com","https://chat.openai.com","https://www.saucedemo.com/v1/"]
    urls = ["https://rss.app/feeds/P1adIhGf0NVWNGge.xml","https://rss.app/feeds/CQ3KRm74ODjfhsRh.xml","https://rss.app/feeds/eSGJi6R1Cioygt4V.xml"]
    num_threads = len(urls)

    threads =  [] 
    for i in range(0,num_threads):
        threads.append(threading.Thread(target=read_content(urls[i])))

    for i in range(0,num_threads):
        threads[i].start()

    for i in range(0,num_threads):
        threads[i].join()

    print("All threads are completed")
    pass