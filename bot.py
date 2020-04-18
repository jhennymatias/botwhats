from selenium import webdriver
import time

class Whats:
    def __init__(self):
        # qual a mensagem 
        self.message = "testando um bot"
        
        # para quem 
        self.grupos = ['TESTE','Eduardo']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome('./chromedriver')
        
    def Enviar(self):
        self.driver.get('https://web.whatsapp.com')
        ## aqui valida codigo do whats
        self.driver.implicitly_wait(15)
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos:
            campo_grupo = self.driver.find_element_by_xpath("//span[@title='{}']".format(grupo_ou_pessoa))
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
       
bot = Whats()
bot.Enviar()