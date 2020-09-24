from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(5)
contatos = [''] #colocar o nome do contato da pessoa, para mais de uma pessoa, colocar uma virgula EX: 'fulano','tal'
mensagem = ''#colocar a mensagem

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(2)

def enviar_mensagem(mensagem):
    for i in range(20): #quantas menssagens tu quer enviar
        campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        campo_mensagem[1].click()                                    
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)

    
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
