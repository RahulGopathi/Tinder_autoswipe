from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


FB_USERNAME = "Your fb username"
FB_PASSWORD = "Your fb password"

# web driver path
web_driver_path = r"C:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(web_driver_path)
driver.get("https://tinder.com/")
time.sleep(6)

# clicking login
login = driver.find_element_by_xpath(
    '//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login.click()
time.sleep(5)

# clicking more options
try:
    more_options = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    time.sleep(4)
except NoSuchElementException:
    time.sleep(2)


# clicking log in with facebook
while True:
    try:
        time.sleep(2)
        fb = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        username = driver.find_element_by_xpath('//*[@id="email"]')
        username.send_keys(FB_USERNAME)
        username.send_keys(Keys.TAB)
        password = driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(FB_PASSWORD)
        login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(6)
        break
    except NoSuchElementException:
        time.sleep(2)

# clicking allow button for location
allow_location = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(1)

# clicking
off_notification = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]')
off_notification.click()
time.sleep(5)

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
            time.sleep(1)

        except NoSuchElementException:
            time.sleep(2)

    # Catches the cases where there is a "Out of Likes" pop-up in front of the "Like" button:
    except NoSuchElementException:
        try:
            out_of_likes = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[2]/button[3]/span')
            out_of_likes.click()
            break
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
