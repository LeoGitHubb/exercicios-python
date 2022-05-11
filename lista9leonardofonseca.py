
def questao1(N):
    if N==1:
        X1 = 0
        X2 = 2
        Xn = 2*(X1)-(-1)*(X2)
    elif N ==0:
        Xn = 2
    else:
        X1 = questao1(N-1)
        X2 = questao1(N-2)
        Xn = 2*(X1)-(-1)*(X2)
    return Xn
print(questao1(1))
print(questao1(2))
print(questao1(3))
print(questao1(4))
print(questao1(5))

def questao2(capital,juros,meses):
    if meses == 0:
        return capital
    else:
        montante = capital*(1+juros/100)
        montante = questao2(montante,juros,meses-1)
        return montante
print(questao2(1000,1,3))
print(questao2(1010,1,2))
print(questao2(1020.1,1,1))
print(questao2(200,4,4))
print(questao2(208,4,3))
print(questao2(216.32,4,2))
print(questao2(224.9728,4,1))
print(questao2(400,5,2))
print(questao2(400,5,3))
print(questao2(400,5,4))


def questao3(lista,num):
    resultado = []
    if num not in lista:
        return lista
    else:
        if lista[0]!=num:
            resultado = resultado+[lista[0]]
            resultado = resultado+questao3(lista[1:],num)
        else:
            resultado = resultado+questao3(lista[1:],num)
        return resultado
print(questao3([],1))
print(questao3([1,3],1))
print(questao3([1,1,1],1))
print(questao3([1,2,1,2],1))
print(questao3([2,2,2,2],1))

def inverter(string): 
    if len(string) == 0: 
        return string 
    else: 
        return inverter(string[1:]) + string[0]

def questao4(string):
    palindromo = inverter(string)
    if len(string)==0 or len(string)==1:
        return True
    if palindromo==string:
        return True
    else:
        return False

print(questao4('a'))
print(questao4('aba'))
print(questao4('abba'))
print(questao4('a ba'))
print(questao4('abb'))
print(questao4('abca'))
print(questao4('abbc'))


def questao5(lista,numero):
    if len(lista) == 0:
        return False
    elif numero != lista[len(lista)//2]:
        return questao5(lista[:len(lista)//2]+lista[len(lista)//2+1:],numero)
    else:
        return True
    

print(questao5([2,1],0))
print(questao5([2,1],1))
print(questao5([2,1],2))
print(questao5([2,1],3))
print(questao5([3,2,1],1))
print(questao5([3,2,1],2))
print(questao5([3,2,1],3))
print(questao5([3,2,1,1],1.0))
print(questao5([3,2,1,1],1.5))


def questao6(lista):
    for n in range(1, len(lista)): 
        posicao = n-1 
        numero = lista[n]
        while posicao >= 0 and numero < lista[posicao]: 
            lista[posicao + 1] = lista[posicao] 
            posicao = posicao - 1 
            lista[posicao + 1] = numero
    return lista 

print(questao6([1]))
print(questao6([4,5,1,2]))
print(questao6([5,4,3,2,1]))
print(questao6([5,1,3,2,4,1]))




