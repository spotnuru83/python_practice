import threading
import time

def read_content(url):
    print(url)
    time.sleep(1)


def perform_project_7():
    urls = ["https://testingtools.co","https://google.com","https://chat.openai.com","https://www.saucedemo.com/v1/"]
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