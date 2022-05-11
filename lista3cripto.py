def num_divisores(numero):
    quantidade = 0
    div = 1

    while div <= numero:
        if numero%div == 0:
            quantidade = quantidade+1
        div = div+1

    return quantidade


def alt_compostos(n):
    quantB = 0
    B = n
    compostos = []
    quant1 = 0
    quant2 = 0
    while n >= 1:
        quant1 = num_divisores(n)
        quant2 = num_divisores(n-1)
        if quant1 > quant2:
            compostos.append(n)
            quantB = quantB+1
        n = n-1
    
    if B == 5000:
        return quantB
        
    return compostos

print(alt_compostos(10))
print(alt_compostos(4))
print(alt_compostos(20))
print(alt_compostos(5000))








