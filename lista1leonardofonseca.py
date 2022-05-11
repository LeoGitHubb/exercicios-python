def questao1(r1,r2,r3,r4,r5):
    '''Funcao que calcula a req a partir de cinco resistores por argumento.
r1,r2,r3,r4,r5 -> floats
valor do retorno -> float'''
    req = 1/(1/r1+1/r2+1/r3+1/r4+1/r5)
    return req
print (questao1(r1,r2,r3,r4,r5))


def questao2(x):
    '''funcao que recebe um valor x por argumento e retorna um y
x->float
valor retornado->floats'''
    return (x**(1/3)-8*x)/5-2*(10*x**2-8*x**3-10)+1/(2*x)
print(questao2(1,2,3,4,5))


def questao3(valorconsumido,porcentagem,pessoas):
    '''funcao retorna o valor a ser pago por cada pessoa em um restaurante.
valorconsumido, porcentagem -> floats
valor retornado -> float'''
    valorpessoa = (valorconsumido+valorconsumido*(porcentagem/100))/pessoas
    return valorpessoa
print(questao3(valorconsumido,porcentagem,pessoas))


def questao4(real,txcambio):
    '''funcao de conversao entre um valor em real para um valor em dolar.
real,txcambio -> floats'''
    dolar = real*1/txcambio
    return dolar
print(questao4(real,txcambio))


def questao5(D,L):
    '''funcao que calcula o perimetro de um retangulo utilizando como
argumento sua diagonal e um dos lados'''
    return 2*L+2*(D**2-L**2)**(1/2)
print(questao5(D,L))


def questao6(x1,x2,x3,x4):
    '''funcao que recebe quatro numeros por argumento, calcula e retorna
    a variancia'''
    m = (x1+x2+x3+x4)/4
    '''media arirmetica simples 'm' dos argumentos'''
    return ((x1-m)**2+(x2-m)**2+(x3-m)**2+(x4-m)**2)/4
print(questao6(x1,x2,x3,x4))


def questao7(vi,vf,a,t1,t2):
    '''funcao para calcular a distancia total percorrida por um veiculo
    usando como argumento sua veloc. final e inicial, aceleração e
    variacao do tempo.
    vi,vf,a,t1,t2 -> floats
    valor retornado ->float'''
    return (vf**2-vi**2)/(2*a)+vf*(t2-t1)
    print(questao7(vi,vf,a,t1,t2))


def questao8(x):
    '''funcao que recebe o numero x por argumento e retorna o valor
    da sua exponencial'''
    return 1+(x**1)/1+(x**2)/2+(x**3)/6+(x**4)/24+(x**5)/120
print(questao8(x))









