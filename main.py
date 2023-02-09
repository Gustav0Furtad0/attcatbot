import scraping
import os
import openpyxl as opx
from colorama import Fore, Style

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

filePrefeitura = {}
fileBranet = ""


    
while True:

    print(BOLD + "\n\n\n------- Arquivo prefeitura -----" + RESET)
    filePrefeitura = {
        "fName": input("Digite o nome do arquivo: "),
        "ixTabela": int(input("Digite o índice da tablea: ")),
        "colunaCodCliente": int(input("Digite o índice da coluna que contenha o código do cliente: ")),
        "colunaNomeCliente": int(input("Digite o índice da coluna que contenha o nome do cliente: ")),
        "colunaQuantidade": int(input("Digite o índice da coluna que contenha a quantidade: ")),
        "colunaUnidade": int(input("Digite o índice da coluna que contenha a unidade do item: "))
    }

    print(BOLD + "\n\n\n------- Arquivo Branet -----" + RESET)
    fileBranet = input("Digite o nome do arquivo: ")

    if not (os.path.isfile(filePrefeitura["fName"]) or os.path.isfile(fileBranet)):
        print(RED + "Arquivo não encontrado, tente novamente..." + RESET)
    else:
        print("Até que entrei no else")
        catologo = opx.load_workbook(filename=filePrefeitura["fName"])
        tabelaEscolha = catologo[catologo.sheetnames[filePrefeitura["ixTabela"]]]
        nomeUnidade = tabelaEscolha.cell(row=2, column=filePrefeitura["colunaQuantidade"]).value
        print(BOLD + "A unidade que deseja alterar o catálogo é " + nomeUnidade + "? (y/n) " + RESET)
        tacerto = input()
        if tacerto == "y":
            break
        else:
            print(RED + 'Por favor, digite novamente os dados...' + RESET)
        


navigator = scraping.ChromeDriver()

navigator.logaSistema('suportejf01', '123456789')

navigator.driver.get("https://juizdefora.branetlogistica.com.br/doms/processos/catalogo.xhtml")

input(BOLD + "Please, opens your modifiable catalog and press Enter..." + RESET)

navigator.itens(fileBranet, filePrefeitura)

navigator.quitDriver()
