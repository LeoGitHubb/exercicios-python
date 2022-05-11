def questao1(nomeArq,mesa):
    mesa = 'Mesa '+str(mesa)+','
    arquivo = open(nomeArq,'r')
    info = ''
    linha = arquivo.readline()
    while linha!= '':
        if mesa in linha:
            info = info+linha
        else:
            info = info
        linha = arquivo.readline()
    arquivo.close()
    return info
print(questao1('rest1.txt',1))
print(questao1('rest1.txt',10))
print(questao1('rest1.txt',20))
print(questao1('rest2.txt',1))
print('----------------------------------------------------------------')

def questao2(arquivo,NumMesa):
    linha = questao1(arquivo,NumMesa)
    if linha == '':
        return 0,0
    else:
        lin = linha[0:len(linha)]
        lin = lin.split(',')
        pessoas = int(lin[1])
        gastotal = 0
        valorCliente = 0
        a = lin[3:len(lin):2]
        b = str(a[-1])
        b = float(b[0:4])
        for valor in a:
            if valor == a[-1]:
                gastotal = gastotal+b
            else:
                gastotal = gastotal+float(valor)
    valorCliente = gastotal/pessoas
    return gastotal,valorCliente
print(questao2('rest1.txt',1))
print(questao2('rest1.txt',10))
print(questao2('rest1.txt',20))
print(questao2('rest2.txt',20))
print(questao2('rest2.txt',1))
print(questao2('rest2.txt',10))
print(questao2('rest3.txt',4))

print('----------------------------------------------------------------')
def questao3(Arq,novo,mesas):
    new = open(novo,'w')
    for mesa in mesas:
        linha = questao1(Arq,mesa)
        if linha!='':
            new.write(linha)
    new.close()
    return 0

print(questao3('rest1.txt','novo.txt',[1,2,7,10,20]))
print(questao3('rest1.txt','novo.txt', [20,10,7,2,1]))
print(questao3('rest1.txt','novo.txt', [2,7,10]))
print(questao3('rest2.txt','novo.txt',[1]))
print('----------------------------------------------------------------')
def questao4(arquivo):
    arq = open(arquivo,'r')
    dicItens = {}
    dicPrecos = {}
    itens = []
    precos = []
    linha = arq.readline()
    i = 0
    while linha!= '':
        linha = linha.split(',')
        itens = itens+linha[2:len(linha):2]
        precos = precos+linha[3:len(linha):2]
        linha = arq.readline()
    for produto in itens:
        valor = precos[i]
        if '\n' in valor:
            valor = valor[:-1]
            dicPrecos[produto] = float(valor)
        else:
            dicPrecos[produto] = float(valor)
        i = i+1
    for prod in itens:
        if prod in dicItens:
            dicItens[prod] = dicItens[prod]+1
        else:
            dicItens[prod] = 1

    arq.close()
    return dicPrecos,dicItens
print(questao4('rest1.txt'))
print(questao4('rest2.txt'))
print(questao4('rest3.txt'))
print('----------------------------------------------------------------')
import numpy as np
def questao5():
    A = np.array([[2,4,1,1],[-3/2,0,1,1/2],[-10/3,0,0,5/6]])
    B = np.array([[0,1/4,1,0],[-2,1,-4,4],[2,-2,0,8]])
    BT = B.transpose()
    soma = A+B
    sub = A-B
    mult = A*B
    mult_matriz = A.dot(BT)
    inv = np.linalg.inv(mult_matriz)
    return soma,sub,mult,mult_matriz,inv
print(questao5())
print('----------------------------------------------------------------')
def questao6():
    a = np.array([[1,2,0.5,4,3],[0,1,1,-10,0],[8,3,0,1,-0.5],[4,4,1,2,1],[-10,5,-1,10,-2]])
    b = ([25,7,-4,20,5])
    x = np.linalg.inv(a).dot(b)
    return x
print(questao6())
    







