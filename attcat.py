import openpyxl as opx

def listaItens(name, ixtable = 0, column = 2):
    catologo = opx.load_workbook(filename=name)
    tabelaEscolha = catologo[catologo.sheetnames[ixtable]]
    lista = []
    for i in range(3, tabelaEscolha.max_row):
        line = {
                "codCliente": tabelaEscolha.cell(row=i, column=1).value,
                tabelaEscolha.cell(row=i, column=column).value,
            }
        if tabelaEscolha.cell(row=i, column=2).value != None:
            lista.append(line)
        
    return lista

def catBranet(name):
    catologo = opx.load_workbook(filename=name)
    tabelaEscolha = catologo[catologo.sheetnames[1]]
    lista = []
    for i in range(3, tabelaEscolha.max_row):
        line = {
                "codCliente": tabelaEscolha.cell(row=i, column=2).value,
                "nomeItem": tabelaEscolha.cell(row=i, column=3).value,
            }
        if tabelaEscolha.cell(row=i, column=3).value != None:
            lista.append(line)
            
    return lista