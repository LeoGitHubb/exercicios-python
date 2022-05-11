def questao1(lista,elemento,pos=0):
    new_list = []
    anterior = []
    posterior = []
    if pos>len(lista)-1:
        new_list = lista+[elemento]
    else:
        anterior = lista[:pos]
        posterior = lista[pos:]
        lista[pos] = elemento
        new_list = new_list+anterior+[lista[pos]]+posterior
    return new_list

print(questao1([1,2,3,4],0))
print(questao1([1,2,3,4],0,0))
print(questao1([1,2,3,4],'123',1))
print(questao1([1,2,3,4],[1,2],3))
print(questao1([1,2,3,4],0,4))
print(questao1([1,2,3,4],0,5))
print('-------------------------------------------------------------------')

def questao2(lista,posicoes):
    media = 0
    soma = 0
    try:
        for indice in posicoes:
            if lista[indice] not in lista:
                raise IndexError
            elif indice!=int(indice):
                raise TypeError
            else:
                lista[indice] = float(lista[indice])
                if lista[indice]!=float(lista[indice]):
                    raise ValueError
                soma = soma+lista[indice]
    except IndexError:
        return 'Posicao nao encontrada'
    except TypeError:
        return 'Valor de posicao invalido, a posicao deveser do tipo inteiro'
    except ValueError:
        return 'A primeira lista contem um valor que nao pode ser convertido para float'
    else:
        media = media+soma/len(posicoes) 
        return media
print(questao2([10,4,10,4,10],[4,0,2]))
print(questao2(['10.5','a','9.5',4,10],[0,2]))
print(questao2(['10.5','a','9.5',4,10],[0,1,2]))
print(questao2([10,4,10,4,10],[0,2,4,5]))
print(questao2([10,4,10,4,10],[0,'2',4]))
print('-------------------------------------------------------------------')

def inserir(dicProdutos,produto):
    print('Inserindo um novo produto.')
    precoPorgrama = 0
    while True:
        try:
            preco = input('Digite o preco desse produto: ')
            preco = float(preco)
            if preco!=float(preco):
                raise ValueError
            elif preco<=0 or preco>=100:
                raise ValueError
        except ValueError:
            print('Valor invalido, digite um valor maior que 0 e menor que 100.')
        else:
            break
    while True:
        try:   
            peso = input('Digite o peso: ')
            peso = float(peso)
            if peso!=float(peso) or peso<0:
                raise ValueError
            elif peso==0:
                raise ZeroDivisionError
        except ValueError:
            print('Valor invalido, digite um numero nao negativo.')

        except ZeroDivisionError:
            print('O peso nao pode ser igual a zero')
        else:
            break
    precoPorgrama = preco/peso
    dicProdutos[produto] = [preco,peso,precoPorgrama]
    return dicProdutos


def modificar(dicProdutos,produto):
    info = 'Modificando o produto {}'.format(produto)
    print(info)
    valores = []
    if produto in dicProdutos:
        for valor in dicProdutos[produto]:
            valores = valores+[valor]
    informar = 'Valores cadastrados: preco = {:.6f}, peso = {:.6f}, preco/grama = {:.6f}'.format(valores[0],valores[1],valores[2])
    print(informar)
    precoPorgrama = 0
    while True:
        try:
            preco = input('Digite o preco desse produto: ')
            preco = float(preco)
            if preco!=float(preco):
                raise ValueError
            elif preco<=0 or preco>=100:
                raise ValueError
        except ValueError:
            print('Valor invalido, digite um valor maior que 0 e menor que 100.')
        else:
            break
    while True:
        try:   
            peso = input('Digite o peso: ')
            peso = float(peso)
            if peso!=float(peso) or peso<0:
                raise ValueError
            elif peso==0:
                raise ZeroDivisionError
        except ValueError:
            print('Valor invalido, digite um numero nao negativo.')

        except ZeroDivisionError:
            print('O peso nao pode ser igual a zero')
        else:
            break
    precoPorgrama = preco/peso
    dicProdutos[produto] = [preco,peso,precoPorgrama]
    return dicProdutos


def questao3(dicProdutos):
    new_dicProdutos = {}
    try:
        produto = input('Digite o nome do produto: ')
        if produto not in dicProdutos:
            raise KeyError
        else:
            new_dicProdutos = modificar(dicProdutos,produto)
    except KeyError:
        new_dicProdutos = inserir(dicProdutos,produto)
    return new_dicProdutos

print(questao3({'Cookie Bauducco':[3.79, 100, 0.379], 'Oreo':[3.49, 90, 0.038778]}))
print(questao3({'Cookie Bauducco':[3.79, 100, 0.379], 'Oreo':[3.49, 90, 0.038778]}))
print('-------------------------------------------------------------------')

def verificar(arquivo):
    try:
        arq = open(arquivo,'r')
    except FileNotFoundError:
        return -1


def questao4(arquivo):
    r = verificar(arquivo)
    if r == -1:
        print('Arquivo nao encontrado.')
        return -1
    else:
        ocorrencias = 0
        arq = open(arquivo,'r')
        linha = arq.readline()
        while linha!= '':
            try:
                linha = float(linha)
                if linha>37:
                    ocorrencias = ocorrencias+1
            except ValueError:
                info = 'A linha: {} nao pode ser convertida.'.format(linha)
                print(info)
            linha = arq.readline()
        return ocorrencias


print(questao4('temp0.txt'))
print(questao4('temp.txt'))
print(questao4('temp2.txt'))



    
