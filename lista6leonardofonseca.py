def questao1(NumInt):
    marco = ''
    dicioMarco = {1500: 'Pedro Alvares Cabral chega ao Brasil', 1501: 'Expedicao exploratoria com Americo Vespucio',
    1546: 'Fundacao da cidade de Salvador', 1557: 'Nomeacao de Mem de Sa como governador-geral',
    1693: 'Primeiras descobertas de ouro em Minas Gerais', 1708: 'Guerra dos Emboabas', 1750: 'Assinatura do Tratado de Madrid',
    1789: 'Inconfidência Mineira'}
    if NumInt in dicioMarco:
        for chave in dicioMarco:
            if NumInt==chave:
                marco = dicioMarco[NumInt]
                return marco   
    else:
        return marco
    print('I am your father')
print(questao1(1501))
print(questao1(1750))
print(questao1(0))

def questao2(dicionario,selecao):
    n_vitoria = 0
    n_empates = 0
    pontuacao = 0
    for jogo in dicionario:
        if selecao in jogo:
            if dicionario[jogo]=='Empate':
                n_empates = n_empates+1
    for jogo in dicionario:
        if selecao in jogo:
            if dicionario[jogo]==selecao:
                n_vitoria = n_vitoria+1
    pontuacao = 3*n_vitoria+n_empates 
    return pontuacao
print(questao2({'Brasil X Mexico': 'Brasil', 'Alemanha X Argentina': 'Alemanha', 'Argentina X Mexico': 'Empate', 'Inglaterra X Brasil': 'Brasil', 'Alemanha X Brasil': 'Brasil', 'Uruguai X Brasil': 'Uruguai'},'Alemanha'))
print(questao2({'Brasil X Alemanha': 'Empate','Brasil X Mexico': 'Brasil', 'Argentina X Mexico': 'Empate', 'Inglaterra X Brasil': 'Empate', 'Alemanha X Brasil': 'Brasil', 'Uruguai X Brasil': 'Uruguai'},'Brasil'))
print(questao2({'Brasil X Alemanha': 'Empate','Brasil X Mexico': 'Empate', 'Argentina X Mexico': 'Empate', 'Inglaterra X Brasil': 'Empate', 'Alemanha X Brasil': 'Empate', 'Uruguai X Mexico': 'Empate'},'Mexico'))
print(questao2({'Brasil X Alemanha': 'Empate','Brasil X Mexico': 'Brasil', 'Argentina X Mexico': 'Argentina', 'Uruguai X Mexico': 'Uruguai'},'Mexico'))
print(questao2({'Brasil X Alemanha': 'Empate','Brasil X Mexico': 'Brasil', 'Argentina X Mexico': 'Argentina', 'Uruguai X Mexico': 'Uruguai'},'Inglaterra'))



import random as rnd
def questao3(dicionario):
    premio1 = rnd.randint(0,20)
    print(premio1)
    premio2 = rnd.randint(0,20)
    print(premio2)
    premio3 = rnd.randint(0,20)
    print(premio3)
    vencedor1 = ''
    vencedor2 = ''
    vencedor3 = ''
    vencedores = ()
    if premio1 not in dicionario:
        vencedor1 = vencedor1
    else:
        vencedor1 = dicionario[premio1]
    if premio2 not in dicionario:
        vencedor2 = vencedor2
    else:
        vencedor2 = dicionario[premio2]
    if premio3 not in dicionario:
        vencedor3 = vencedor3
    else:
        vencedor3 = dicionario[premio3]
    vencedores = vencedores+(vencedor1,vencedor2,vencedor3,)
    return vencedores
rnd.seed(0)
print(questao3({1:'Ana', 2:'Nina', 3:'Yuri', 4:'Renan', 5:'Antonio', 6:'Luiza', 7:'Luiz', 8:'Pedro', 9:'Alice', 10:'Gustavo'}))
print(questao3({1:'Ana', 2:'Nina', 3:'Yuri', 4:'Renan', 5:'Antonio', 6:'Luiza', 7:'Luiz', 8:'Pedro', 9:'Alice', 10:'Gustavo', 11:'Fernanda', 12:'Andre', 13:'Aline', 14:'Joao', 15:'Augusto', 16:'Maria', 17:'Jose', 18:'Joaquim', 19: 'Jaqueline', 20: 'Cristina'}))
print(questao3({1:'Ana', 2:'Nina', 3:'Nina', 4:'Nina', 5:'Antonio', 6:'Luiza', 7:'Luiz', 8:'Pedro', 9:'Augusto', 10:'Gustavo', 11:'Andre', 12:'Andre', 13:'Andre', 14:'Joao', 15:'Augusto', 16:'Augusto'}))




def questao4(alunos,notas):
    i = 0
    d = {}
    media = 0
    for nome in alunos:
        if nome in d:
            media = (d[nome]+notas[i])/2
            d[nome] = media
        else:
            d[nome] = notas[i]
        i = i+1
    return d
print(questao4(['Fernanda','Pedro','Joao','Ana','Alice'],[9,8,7,9.5,10]))
print(questao4(['Fernanda','Pedro','Joao','Ana','Alice','Fernanda'],[9,8,7,9.5,10,10]))
print(questao4(['Fernanda', 'Luiz', 'Pedro', 'Luiz', 'Joao', 'Ana', 'Alice', 'Fernanda'], [9, 5, 8, 9.5, 7, 9.5, 10, 10]))

def questao5(dicionario,alturaMin):
    Maiores = []
    for pessoa in dicionario:
        if dicionario[pessoa]>alturaMin:
            Maiores = Maiores+[pessoa]
        else:
            Maiores = Maiores
    return Maiores
print(questao5({'Fernanda': 1.6, 'Luiz': 1.7, 'Pedro': 1.61, 'Joao': 1.82, 'Ana': 1.5, 'Alice':1.67},1.6))
print(questao5({'Fernanda': 1.6, 'Luiz': 1.7, 'Carla':1.66, 'Pedro': 1.61, 'Joao': 1.82, 'Ana': 1.5, 'Alice': 1.67}, 1.65))
print(questao5({'Carlos':1.45, 'Fernanda': 1.6, 'Luiz': 1.7, 'Carla':1.66, 'Pedro': 1.61, 'Joao': 1.82, 'Ana': 1.5, 'Alice': 1.67}, 1.4))

def questao6(escalada,esgrima,remo):
    esc = set()
    esg = set()
    rem = set()
    totalsocios = (escalada.union(esgrima).union(remo))
    totalsocios = len(totalsocios)
    esc = escalada-esgrima
    esc = esc-remo
    esg = esgrima-escalada
    esg = esg-remo
    rem = remo-escalada
    rem = rem-esgrima
    a = escalada.intersection(remo)-esgrima
    b = escalada.intersection(esgrima)-remo
    c = esgrima.intersection(remo)-escalada
    d = esgrima.intersection(escalada)-remo
    e = remo.intersection(esgrima)-escalada
    f = remo.intersection(escalada)-esgrima
    doisEsportes = (a.union(b).union(c).union(d).union(e).union(f))
    resultado = ()
    resultado = resultado+(totalsocios,)+(doisEsportes,)+(esc,)+(esg,)+(rem,)
    return resultado
print(questao6({'Andre','Ana','Luiz',},{'Luiz'},set()))
print(questao6({'Andre','Ana','Luiz'},{'Andre','Ana','Luiz'},{'Andre','Ana','Luiz'}))
print(questao6({'Andre', 'Ana', 'Luiz', 'Maria'}, {'Andre', 'Ana', 'Alice'}, {'Andre', 'Luiz', 'Jose'}))





