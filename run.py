import telebot
from telebot import types
import requests
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
firefox_options.headless = True

TOKEN = "5046387950:AAG1oQLrZvube-_W3x1-_6ZwVptlVxmQMm4"
CHAT_ID = "1226791374" #a meu
Cristina = "2003867461"
client = telebot.TeleBot(TOKEN)

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Online")
#requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={Cristina}&text=Online")

def send_message(message, mess):
    client.send_message(message.chat.id, mess)

@client.message_handler(commands=["start"])
def start(message):
	rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btns = ["/insta_spamer", "/insta_follower"]

	for btn in btns:
		rmk.add(types.KeyboardButton(btn))
	client_id = message.chat.id
	print(client_id)
	client.send_message(message.chat.id, "Alege ce o sa faci:", reply_markup=rmk)

@client.message_handler(commands=["insta_spamer"])
def send_message1(message):
    message_text = client.send_message(message.chat.id, "Ce Mesaj? (Exit pentru a iesi)")
    client.register_next_step_handler(message_text, message_text1)
def message_text1(message):
    if message.text == "Exit":
        start(message)
    else:
        global context1
        context1 = message.text
        username = client.send_message(message.chat.id, "Cui?")
        client.register_next_step_handler(username, get_username)
def get_username(message):
    global username1
    if message.text == "natural_private_328":
        client.send_message(message.chat.id, "Acest nume nu poate fi utilizat")
        start(message)
    elif message.text == "Natural":
        client.send_message(message.chat.id, "Acest nume nu poate fi utilizat")
        start(message)
    else:
        username1 = (message.text)
        numbers = client.send_message(message.chat.id, "Cate mesaje?")
        client.register_next_step_handler(numbers, get_numbers)
def get_numbers(message):
    try:
        global get_number
        get_number = message.text
        driver = webdriver.Firefox(options=firefox_options, executable_path=GeckoDriverManager().install())
        driver.get("https://instagram.com")
        cokies = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        cokies.click()
        sleep(7)
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input').send_keys('bot_C01')
        send_message(message, mess="10%")
        sleep(5)
        password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input').send_keys('KaliNethunter')
        sleep(3)
        login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[3]').click()
        send_message(message, mess="15%")
        sleep(10)
        not_now_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(10)
        no_not = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        send_message(message, mess="20%")
        sleep(5)
        message_btn = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()
        sleep(7)
        send_mes_btn = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]').click()
        send_message(message, mess="50%")
        sleep(5)
        send_mes = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(username1)
        send_message(message, mess="80%")
        sleep(5)
        btn = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
        send_message(message, mess="90%")
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
        sleep(3)
        text_area = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        send_message(message, mess="100%, trimit mesaje")
        mes = 0
        n = get_number
        while mes < int(n):
            afk = randint(1,2,3,4)
            text_area.send_keys(context1)
            sleep(0.08)
            text_area.send_keys(Keys.ENTER)
            mes += 1
            send_message(message, mess=f"S-o trimis {mes}")
        driver.quit()
        client.send_message(message.chat.id, f"Gata, ai trimis {mes}")
        start(message)
    except Exception as err:
        send_message(message, mess=f"Eroare {err}")
        start(message)

@client.message_handler(commands=["insta_follower"])
def insta_follower(message):
    get_username_follow_int = client.send_message(message.chat.id, "La cine? (Exit pentru a iesi)")
    client.register_next_step_handler(get_username_follow_int, get_follow)
def get_follow(message):
    global cavo
    cavo = message.text
    if cavo == "Exit":
        start(message)
    else:
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            driver.get("https://instagram.com")
            cokies = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
            cokies.click()
            sleep(3)
            username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input').send_keys('bot_C01')
            sleep(3)
            password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input').send_keys('KaliNethunter')
            sleep(3)
            login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[3]').click()
            sleep(5)
            not_now_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            sleep(5)
            no_not = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            sleep(1)
            driver.get(f"https://instagram.com/{cavo}/")
            sleep(4)
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
            send_message(message, mess="Gata")
        except Exception as err:
            send_message(message, mess="Eroare")
            start(message)

client.polling()
