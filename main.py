import openpyxl as opx
import scraping

filePrefeitura = input("Type your prefeitura file name and press Enter...")
fileBranet = input("Type your Branet file name and press Enter...")

navigator = scraping.ChromeDriver()

navigator.logaSistema('suportejf01', '123456789')

navigator.driver.get("https://juizdefora.branetlogistica.com.br/doms/processos/catalogo.xhtml")

input("Please, opens your modifiable catalog and press Enter...")

navigator.itens()

# navigator.quitDriver()
