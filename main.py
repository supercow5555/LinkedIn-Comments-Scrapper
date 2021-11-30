from time import sleep
import selenium
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Enter post url
post_url = "https://www.linkedin.com/posts/dragonflyhk_ali-health-er-report-activity-6839475952322449408-Pcc_/"

def load_all_comments(class_name):

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
username.send_keys("...........")

password = driver.find_element_by_name("session_password")
password.send_keys("...........")

signin = driver.find_element_by_xpath("""//*[@id="main-content"]/section[1]/div/div/form/button""")
signin.click()

# setting driver to post_url
driver.get(post_url)


# Loading all commments


loadcomments = driver.find_element_by_class_name("comments-comments-list__load-more-comments-button")
loadcomments.click()


while(True):
    pass