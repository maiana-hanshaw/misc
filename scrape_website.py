import requests
import os
from bs4 import BeautifulSoup
import time
import logging
import subprocess
import psutil as psutil
import win32com.client as w32
 

############################# UPDATE THIS SECTION #############################

 
URL_LOGIN= https://xxxxxxxxxxxxxxxxxxxx.com/
URL_TO_MONITOR = https://xxxxxxxxxxxxxxxxxxx.com/members-home/bulletins
 
COOKIES = {
    '_ga': 'XXXXXXXXXXXXXXXXXXXXXXXXXX',
    '_gid': 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
}

DATA = {
    'name': 'XXXXXXXXXXX',
    'pass': 'XXXXXXXXXX',
    'form_build_id': 'form-OvGTuhGaZS3XGhwcIuWmXGo9F9s1dTIOgl4Vdzrrt2U',
    'form_id': 'user_login',
    'op': 'Log in',
}

DELAY_TIME = 43200 # seconds (6h = 21,600s, 12h = 43,200s)


OUTLOOK_PATH = (r"C:\Program Files (x86)\MicrosoftOffice\root\Office16\OUTLOOK.EXE")
RECIPIENT_EMAIL_ADDRESS_1 = xxxxxxx@xxxxxxxx.com # the email address for the notification
RECIPIENT_EMAIL_ADDRESS_2 = xxxxxxx@xxxxxxxx.com # a second email address for the notification

FILE_DIR = "C:/Users/mhanshaw/OneDrive/XXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXX/XXXXXXXXXXXX"
PREVIOUS_CONTENT_FILE = "msrb_previous_content.txt"
PREVIOUS_CONTENT = os.path.join(FILE_DIR, PREVIOUS_CONTENT_FILE)


########################### DEFINE EMAIL FUNCTIONS ############################


def send_email(recipient, subject, body, html=False):  # uses Outlook
    if not is_outlook_open(): 
        print("Opening Outlook")
        open_outlook()
        
    outlook = w32.Dispatch("outlook.application")
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject

    if html:
        mail.HTMLBody = body
    else:
        mail.Body = body

    mail.Send()

 
def open_outlook():
    outlook_path = OUTLOOK_PATH
    
    try:
        subprocess.call([outlook_path])
        os.system(outlook_path)
    except OSError:
        print("Outlook didn't open successfully")


def is_outlook_open():  # searches the list of process IDs to see if Outlook is running
    for item in psutil.pids():
        p = psutil.Process(item)
        if "OUTLOOK.EXE" in p.name():
            return True
    return False


######################### DEFINE WEBPAGE FUNCTIONS ############################


def scrape_website():   
    s = requests.Session()
    s.post(URL_LOGIN, cookies=COOKIES, data=DATA, verify=False)
    response = s.get(URL_TO_MONITOR)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find("div", {"class": "view-content"})

    return results
  

def parse_website_results():   
    results = scrape_website()
    current_content_set = set()

    for result in results:
        links = results.find_all("a")
        for link in links:
            link_url = link["href"]
            current_content_set.add(link_url)

    current_content_list_sorted = sorted(list(current_content_set))

    return current_content_list_sorted


######################### DEFINE COMPARE FUNCTIONS ############################


def get_previous_content():
    if not os.path.exists(PREVIOUS_CONTENT):
        open(PREVIOUS_CONTENT, 'w+').close()

    filehandle = open(PREVIOUS_CONTENT, 'r')
    previous_content_str = filehandle.read()
    filehandle.close()

    return previous_content_str


def get_difference_list():
    current_content_list = parse_website_results()
    current_content = str(current_content_list)
    previous_content = get_previous_content()

    diff_list = []
    for element in current_content_list:
        if str(element) not in previous_content:
            diff_list.append(element)
        else:
            continue    

    diff_list_str = "\n\n".join(diff_list)                

    return current_content, previous_content, diff_list_str


def rewrite_previous_content():
    current_content, _, _ = get_difference_list()

    filehandle_previous = open(PREVIOUS_CONTENT, 'w')
    filehandle_previous.write(current_content)
    filehandle_previous.close()

    return print("Previous Content Rewritten")
 

def compare_content():
    current_content, previous_content, _ = get_difference_list()

    if previous_content == current_content:
        return False
    else:          
        return True 


########################### DEFINE "MAIN" FUNCTION ############################       

   
def main():
    log = logging.getLogger(__name__)
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor") 

    _, _, diff_list_str = get_difference_list()

    while True:
        try:
            if compare_content():
                log.info("WEBPAGE WAS CHANGED.")
                rewrite_previous_content()
                send_email(RECIPIENT_EMAIL_ADDRESS_1, "SUBJECT!", diff_list_str)
                send_email(RECIPIENT_EMAIL_ADDRESS_2, "SUBJECT!", diff_list_str)

            else:
                log.info("Webpage was not changed.")
                send_email(RECIPIENT_EMAIL_ADDRESS_1, "Subject!", " ")

        except:
            log.info("Error checking website.")                   
            send_email(RECIPIENT_EMAIL_ADDRESS_1, "ERROR CHECKING WEBSITE!", "Unable to connect to the website. Check script.") 
        
        time.sleep(DELAY_TIME)   


################################### RUN :) ####################################   


if __name__ == "__main__":
    main()


###############################################################################