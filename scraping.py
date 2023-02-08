from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ChromeDriver:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://juizdefora.branetlogistica.com.br/doms')

    def logaSistema(self, userin, passwordin):
        log = self.driver.find_elements(By.XPATH, "/html/body/div[@id='centro']/div[@id='bloco_login']/div[@class='login']/div[@id='conteudo']/form/span/div/input"); 
        log[0].send_keys(userin)
        log[1].send_keys(passwordin)
        btlogin = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/span/input")
        btlogin.click()
        input("Press Enter when you logged...")
        

    def itens(self, branet, prefeitura):
        def analyzeItem(name):
            for item in branet:
                if item.name == name:
                    for 
        
        select = Select(self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/form[@id='cadastro_itens']/div/div/div/div[1]/select"))
        select.select_by_value('500')
        
        sleep(3)
        
        navigator = self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div/span/form/div/div/div/div[1]/span[2]")
        navigator = navigator.find_elements(By.TAG_NAME, 'a')
        
        for i in range(len(navigator)):
            if i != 0:
                navigator[i].click();
                sleep(4)
                
            rows = self.driver.find_elements(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/form/div/div/div/div/table/tbody/tr")
            
            for row in rows:
                cels = row.find_elements(By.TAG_NAME, 'td')
                
                if analyzeItem(cels[1].text):
                    btsEdit = cels[12].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'a')
                    btsEdit[0].click()
                    
                    inputQtd = cels[4].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'span').find_elements(By.TAG_NAME, 'input')
                    inputQtd[0].click()
                    inputQtd[0].clear()
                    inputQtd[0].send_keys('2')

                        
                    inputQtd = cels[7].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'span').find_elements(By.TAG_NAME, 'input')
                    inputQtd[0].click()
                    inputQtd[0].clear()
                    inputQtd[0].send_keys('2')
                    
                    btsEdit[1].click()
                    break
                else:
                    print("Guardar item na lista de não alocados")
                    break
                
            navigator = self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div/span/form/div/div/div/div[1]/span[2]")
            navigator = navigator.find_elements(By.TAG_NAME, 'a')
            
        
    
    def quitDriver(self):
        self.driver.quit()
