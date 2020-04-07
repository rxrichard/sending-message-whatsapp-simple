from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text = 'Oi momo'  # MENSAGEM A SER ENVIADA
no_of_message = 1  # QUANTIDADE DE VEZES A SER ENVIADA PARA A MESMA PESSOA
moblie_no_list = [5511999999999]  # LISTA DE NUMEROS tem que colocar DD + DDD + NUM

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        # verifica conexão com internet
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://web.whatsapp.com")
sleep(10)  # aguarda o scan do codigo do wz


# noinspection PyDeprecation
def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :" + str(phone_no))


for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no, message_text)

    except Exception as e:
        sleep(10)
        is_connected()
