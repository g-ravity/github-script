from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from animation import Animation
import time
import json

driver = None


def setup():
    global driver

    # Initializing chrome in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    driver.get("https://github.com/")

    # Completing the login process
    sign_in = driver.find_element_by_link_text("Sign in")
    sign_in.click()

    email_elem = driver.find_element(
        By.XPATH, '//*[@id="login_field"]')
    password_elem = driver.find_element(
        By.XPATH, '//*[@id="password"]')
    email_elem.send_keys(email)
    password_elem.send_keys(password)
    login_btn = driver.find_element(
        By.XPATH, '//*[@id="login"]/form/div[3]/input[4]')
    login_btn.click()


def deleteRepo(repo_list):
    for repo in repo_list:
        try:
            loader = Animation(f"Deleting {repo}", 0.1)
            loader.start()
            driver.get(f"https://www.github.com/{username}/{repo}")

            elem = driver.find_element_by_link_text("Settings")
            elem.click()
            time.sleep(2)
            delete_btn = driver.find_element(
                By.XPATH, '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')
            delete_btn.click()
            delete = driver.find_element(
                By.XPATH, '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')
            delete.send_keys(repo)
            delete_btn = driver.find_element(
                By.XPATH, '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')
            delete_btn.click()

            loader.stop()
            print(f"Successfully deleted {repo} repository")
        except Exception as err:
            loader.stop()
            print(f"Some error occurred while deleting {repo} repository")
            print(f"Error: {err}")


with open("../info.json") as file:
    data = json.load(file)
    username = data["username"]
    email = data["email"]
    password = data["password"]

setup()

repo_list = input(
    'List of repositories to be deleted, separated by space: ').split(' ')

deleteRepo(repo_list)
