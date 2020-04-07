from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Digite o nome do grupo ou pessoa:')
msg = input('Digite a mensagem aqui')
count =int(input('Digite sua conta'))

input('O que fazer depois que o qrcode iniciar')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range (count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('compose-btn-send')
    button.click()