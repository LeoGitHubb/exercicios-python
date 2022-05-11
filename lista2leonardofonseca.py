def questao1(x):
    if x<0:
        return 0.2*x
    elif x>=0 and x<2:
        return 4*x
    elif x>=2 and x<4:
        return -2*x**2+x+14
    elif x>=4 and x<5:
        return x**3-x**2/2-15*x-6
    else:
        return 0
print(questao1(-1))
print(questao1(1))
print(questao1(3))
print(questao1(4.5))
print(questao1(5))



def questao2(vg,vd,vs,vth):
    if (type(vg)!=int and type(vg)!=float)\
       or (type(vd)!=int and type(vd)!=float)\
       or (type(vs)!=int and type(vs)!=float)\
       or (type(vth)!=int and type(vth)!=float):
        return -1
    if vd<vs:
        return -2
    if vg<-3.3 or vg>3.3:
        return -3
    if vd<-3.3 or vd>3.3:
        return -3
    if vs<-3.3 or vs>3.3:
        return -3
    if vth<0 or vth>1:
        return -3
    if vg-vs<vth:
        return 0
    elif vg-vs>=vth and vd-vs<vg-vs-vth:
        return 1
    elif vg-vs>=vth and vd-vs>=vg-vs-vth:
        return 2

print(questao2(1j,1,2,-1))
print(questao2(1,1,4,True))
print(questao2(1,1,4,0))
print(questao2(1,1,0,0))
print(questao2(1,5,2,0.8))
print(questao2(0.3,3.3,0,0.7))
print(questao2(3.3,2,0,0.7))
print(questao2(3.3,3.3,0,0.7))



def questao3(freqrepouso,freqatual,oxiatual):
    if freqatual>3*freqrepouso or oxiatual<95:
        situacao = -1
    elif freqatual<2*freqrepouso or oxiatual>97:
        situacao = 1
    else:
        situacao = 0
    return situacao
print(questao3(60,119,98))
print(questao3(60,190,100))
print(questao3(50,190,95))
print(questao3(50,100,94))



def questao4(linha,coluna):
    if type(linha)!=int:
        linha = -3
    elif linha<0 or linha>9:
        linha = -2        
    elif linha>6:
        linha = -1
    elif linha<6:
        linha = 1
    else:
        linha = 2
    if type(coluna)!=int:
        coluna = -3  
    elif coluna<0 or coluna>9:
        coluna = -2
    elif coluna>7:
        coluna = -1
    elif coluna<7:
        coluna = 1
    else:
        coluna = 2

    return linha,coluna        
   
print(questao4(0,0))
print(questao4(8,4))
print(questao4(-1,3))
print(questao4(6,10))
print(questao4(8,8))
print(questao4(4,9))
print(questao4(7,6))
print(questao4(6,7))
print(questao4(2.2,2))



def questao5(n1,n2,n3):
    valor1=n1
    valor2=n2
    valor3=n3
    ordem=valor1,valor2,valor3
    
    if valor1>valor2>valor3:
        ordem = valor1,valor2,valor3
        
    elif valor1>valor3>valor2:
        ordem = valor1,valor3,valor2
        
    elif valor2>valor1>valor3:
        ordem = valor2,valor1,valor3
        
    elif valor3>valor1>valor2:
        ordem = valor3,valor1,valor2
        
    elif valor2>valor3>valor1:
        ordem = valor2,valor3,valor1
        
    elif valor3>valor2>valor1:
        ordem = valor3,valor2,valor1

    elif valor1==valor2>valor3:
        ordem = valor1,valor2,valor3
        
    elif valor1==valor2<valor3:
        ordem = valor3,valor1,valor2

    elif valor1==valor3>valor2:
        ordem = valor1,valor3,valor2
        
    elif valor1==valor3<valor2:
        ordem = valor2,valor1,valor3

    elif valor2==valor3>valor1:
        ordem = valor2,valor3,valor1
        
    elif valor2==valor3<valor1:
        ordem = valor1,valor2,valor3

    return ordem
print(questao5(2,2,2))
print(questao5(1,2,2))
print(questao5(1,2,1))
print(questao5(1,2,3))
print(questao5(1,3,2))


    
def questao6(n1,n2,n3,n4,n5):
    valor=n1

    if n1>n2:
        valor = valor
    elif n2>valor:
        valor = n2
    if valor>n3:
        valor = valor
    elif n3>valor:
        valor = n3
    if valor>n4:
        valor = valor
    elif n4>valor:
        valor = n4
    if valor>n5:
        valor = valor
    elif n5>valor:
        valor = n5
    return valor        
    
print(questao6(2,5,-3,0,10))
print(questao6(10,5,-3,0,2))
print(questao6(7,5,7,0,2))
print(questao6(4,5,3,8,2))



def questao7(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6):
    jogador1=0
    jogador2=0
    
    if (jogo1+jogo4)%2==0:
        jogador1 = jogador1+1
        
    elif (jogo1+jogo4)%2==1:
        jogador2 = jogador2+1
        
    if (jogo2+jogo5)%2==0:
        jogador1 = jogador1+1
        
    elif (jogo2+jogo5)%2==1:
        jogador2 = jogador2+1
        
    if (jogo3+jogo6)%2==0:
        jogador1 = jogador1+1
        
    elif (jogo3+jogo6)%2==1:
        jogador2 = jogador2+1
        
    return jogador1,jogador2        
print(questao7(1,1,1,1,1,1))
print(questao7(2,1,1,1,1,1))
print(questao7(2,1,1,1,2,1))
print(questao7(2,1,2,1,2,1))
print(questao7(0,1,0,0,1,1))

