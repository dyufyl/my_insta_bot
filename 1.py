import schedule
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.webdriver.firefox.options import Options

#firefox options
firefox_options = Options()
firefox_options.headless = False
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-sh-usage")

def login():
    try:
        global driver
        username = "ahsan__bro" # username
        #driver
        driver = webdriver.Firefox(options=firefox_options, executable_path=GeckoDriverManager().install())
        #open instagram
        driver.get("https://instagram.com")
        #cokies = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]') #cockies
        #cokies.click()
        sleep(7)
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input').send_keys('natural_private_328')#username
        sleep(5)
        password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input').send_keys('KaliNethunter1')#password
        sleep(3)
        login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[3]').click()#login btn
        sleep(7)
        not_now_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()#now now btn
        sleep(7)
        no_not = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()#not notification btn
        sleep(5)
        message_btn = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()# message btn
        sleep(7)
        send_mes_btn = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]').click()#send message btn
        sleep(6)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys("ahsan__bro")#send message username
        sleep(5)
        btn = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()#send message by username click btn
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()#click on username
        sleep(3)
        text_area = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')#textarea of user
        sleep(1)
        #text_area.send_keys(context1) #principala parte din mesaje
        text_area.send_keys("Cf?")
        sleep(5)
        text_area.send_keys(Keys.ENTER)
        driver.quit()
    except Exception as err:
        print("Eroare" + "\n" + err)

def main():

    schedule.every().day.at('16:35').do(login)
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()