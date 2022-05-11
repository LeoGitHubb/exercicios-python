def questao1(num):
    div = 1
    n = 1
    while n<num:
        if num%n == 0:
            div = div+1
        n = n+1
    return div      
        
print(questao1(2))
print(questao1(6))
print(questao1(10))
print(questao1(11))
print(questao1(30))


def questao2a(num):
    fatorial = 1
    n = 1
    while n <=num:
        fatorial = fatorial*n
        n = n+1
    return fatorial

print(questao2a(0))
print(questao2a(3))
print(questao2a(8))


def questao2b(x):
    n = 0
    arcseno = 0
    while n<=5:
        f = questao2a
        arcseno = arcseno+(f(2*n)*(x**(2*n+1)))/((4**n)*f(n)**2*(2*n+1))
        n = n +1
    return arcseno

print(questao2b(-0.1))
print(questao2b(0.5))
print(questao2b(0.8))


def questao3a(x):
    q = x//10
    r = x%10
    return q, r
print(questao3a(1))
print(questao3a(11010))
print(questao3a(12345))


def questao3b(inteiro):
    n = 0
    c = 0
    dec = inteiro//10
    while n<=dec:
        a, b = questao3a(inteiro)
        inteiro = a
        n = n+1
        if b == 1:
            c = c+1
    return c

print(questao3b(1000001))
print(questao3b(1000000))
print(questao3b(101101))
print(questao3b(1111))


def questao4(x,y):
    d = 1
    z = y/2
    while z<x:
        y = y+(y*0.2)
        z = (z+y)/2
        d = d+1
    return d

print(questao4(2,1))
print(questao4(2,0.5))
print(questao4(3,2))
print(questao4(100,10))


        


        
        
    
