from time import sleep
import selenium
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



### Enter details here!

# User name and password
linkedin_username = ".........."
linkedin_password = ".........."

# Enter post url
post_url = "https://www.linkedin.com/posts/dragonflyhk_ali-health-er-report-activity-6839475952322449408-Pcc_"              # Example post with 44 commments





### helper functions

# comments loading functions
def load_all_comments():
    try:
        loadcomments = driver.find_element_by_class_name("comments-comments-list__load-more-comments-button")
        print("Loading comments")
        while True:
            loadcomments.click()
            print("Loading...")
            sleep(5)
            try:
                loadcomments = driver.find_element_by_class_name("comments-comments-list__load-more-comments-button")
            except:
                print("All comments have been loaded")
                break
    except:
        print("already loaded")

# def email_extractor(comments):
#     emails = []
#     for comment in comments:
#         email_match = re.findall(r".+\@.+\..+", str(comment))             # regex not working
#         if email_match:
#             emails.append(email_match)
#         else:
#             emails.append("-")
#     return emails

# email extractor
def extract_emails(all_comments):
    emails = []
    for comment in all_comments:
        email_match = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", str(comment))
        if email_match:
            emails.append(email_match)
        else:
            emails.append("-")
    return emails

# transfer to csv
def transfer_csv():
    for name, headline, email, comment in zip(all_names, all_headlines, all_emails, all_comments):
        writer.writerow([name, headline, email, comment.encode("utf-8")])







# Start of programme

# Open a CSV
writer = csv.writer(
    open(
        "comments.csv",
        "w",
        encoding="utf-8",
    )
)
writer.writerow(["Name", "Headline", "Email", "Comment"])


# Initializing the web driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Opening LinkedIn Homepage and logging in
driver.get("https://www.linkedin.com/")

username = driver.find_element_by_name("session_key")
username.send_keys(linkedin_username)

password = driver.find_element_by_name("session_password")
password.send_keys(linkedin_password)

signin = driver.find_element_by_xpath("""//*[@id="main-content"]/section[1]/div/div/form/button""")
signin.click()

# setting driver to post_url
driver.get(post_url)


# Loading all commments
load_all_comments()


# Stripping all comments raw
comments = driver.find_elements_by_class_name("comments-comment-item__main-content")
all_comments = [i.text.strip() for i in comments]


# Extracting names
names = driver.find_elements_by_class_name("comments-post-meta__name-text")
all_names = [i.text.strip() for i in names]


# Extracting headlines
headlines = driver.find_elements_by_class_name("comments-post-meta__headline")
all_headlines = [i.text.strip() for i in headlines]

# # Extracting profile picture links
# pictures = driver.find_elements_by_class_name()

# extract from all comments
all_emails = extract_emails(all_comments)

# transfer to csv
transfer_csv()

# while(True):
#     pass