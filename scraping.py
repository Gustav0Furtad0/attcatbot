from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from attcat import listaItens, catBranet
from colorama import Fore, Style, Back, init

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
        input("Pressione ENTER quando estiver logado no centro de custo desejado")
        

    def itens(self, branet, prefeitura):
        dataBranet = catBranet(branet);
        dataPrefeitura = listaItens(prefeitura["fName"], prefeitura["colunaQuantidade"], prefeitura["ixTabela"], prefeitura["colunaNomeCliente"], prefeitura["colunaUnidade"], prefeitura["colunaCodCliente"]);
        
        nonVisitedSys = []
        
        def analyzeItem(name, qtd):
            codItem = 0;
            for item in dataBranet:
                if not (item["codCliente"] is None):
                    if item["codCliente"].isdigit():
                        if item["nomeItem"] == name:
                            codItem = int(item["codCliente"])
                            break
            
            for item in dataPrefeitura:
                if int(item["codCliente"]) == codItem:
                    print("Analisando item: " + name)
                    sleep(1.5)
                    print(Fore.CYAN + "Nome sistema: " + name + Style.RESET_ALL + " | " + Fore.GREEN + "Nome Prefeitura: " + item["nomeCliente"] + Fore.CYAN + "\nQuantidade: " + str(qtd) + Style.RESET_ALL +" | " + Fore.GREEN + "Quantidade e unidade Prefeitura: " + str(item["quantidade"]) + " " + item["unidade"] + Style.RESET_ALL)
                    if input("Os itens acima são iguais ? (y/n) ") == 'y':
                        dataPrefeitura.remove(item)
                        print("")
                        return item["quantidade"]
                    else:
                        item["visited"] = False
                        return False
                
            return False
                            
        
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
                item = 0
                if cels[4].text.isdigit():
                    item = analyzeItem(cels[1].text, int(cels[4].text))
                    if item != False:
                        ix = 0
                        while True:
                            try:
                                btsEdit = cels[12].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'a')
                                btsEdit[0].click()
                                
                                inputQtd = cels[4].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'span').find_elements(By.TAG_NAME, 'input')
                                inputQtd[0].click()
                                inputQtd[0].clear()
                                inputQtd[0].send_keys(item)

                                    
                                inputQtd = cels[7].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'span').find_elements(By.TAG_NAME, 'input')
                                inputQtd[0].click()
                                inputQtd[0].clear()
                                inputQtd[0].send_keys(item)
                                
                                btsEdit[1].click()
                                break
                            except:
                                ix += 1
                                if ix == 5:
                                    break
                                else:
                                    sleep(1)
    
                    else:
                        nonVisitedSys.append([cels[1].text, cels[4].text])
                        
                else:
                    nonVisitedSys.append([cels[1].text, cels[4].text])
                
            navigator = self.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div/span/form/div/div/div/div[1]/span[2]")
            navigator = navigator.find_elements(By.TAG_NAME, 'a')
            
        print("\n\nItens não visitados da prefeitura")
        with open("relatorio.txt", "w") as file:
            for i in dataPrefeitura:
                file.write("Cod: " + str(i["codCliente"]) + " | Nome: " + i["nomeCliente"] + "\n")
                print("Cod: " + str(i["codCliente"]) + " | Nome: " + i["nomeCliente"])
            
        print("FIM DA TAREFA")
            
            
        
    
    def quitDriver(self):
        self.driver.quit()
