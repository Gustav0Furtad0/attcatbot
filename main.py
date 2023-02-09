import scraping
import os
import openpyxl as opx

filePrefeitura = {}
fileBranet = ""

def innerData():
    print("\n\n\n------- Arquivo prefeitura -----")
    filePrefeitura = {
        "fName": input("Digite o nome do arquivo: "),
        "ixTabela": int(input("Digite o índice da tablea: ")),
        "colunaCodCliente": int(input("Digite o índice da coluna que contenha o código do cliente: ")),
        "colunaNomeCliente": int(input("Digite o índice da coluna que contenha o nome do cliente: ")),
        "colunaQuantidade": int(input("Digite o índice da coluna que contenha a quantidade: ")),
        "colunaUnidade": int(input("Digite o índice da coluna que contenha a unidade do item: "))
    }

    print("\n\n\n------- Arquivo Branet -----")
    fileBranet = input("Digite o nome do arquivo: ")
    
while True:
    innerData()
    if os.path.isfile(filePrefeitura["fName"]) and os.path.isfile(fileBranet):
        break
    else:
        print("Arquivo não encontrado, tente novamente...")
        
    catologo = opx.load_workbook(filename=filePrefeitura["fName"])
    tabelaEscolha = catologo[catologo.sheetnames[filePrefeitura["ixtable"]]]
    nomeUnidade = tabelaEscolha.cell(row=2, column=filePrefeitura["colunaCodCliente"]).value
    
    if input("A unidade que deseja alterar o catálogo é " + nomeUnidade + "? (y/n)") == "y":
        break
    else:
        print('Por favor, digite novamente os dados...')
        


navigator = scraping.ChromeDriver()

navigator.logaSistema('suportejf01', '123456789')

navigator.driver.get("https://juizdefora.branetlogistica.com.br/doms/processos/catalogo.xhtml")

input("Please, opens your modifiable catalog and press Enter...")

navigator.itens(fileBranet, filePrefeitura)

navigator.quitDriver()
