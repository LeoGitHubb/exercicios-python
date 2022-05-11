import random
class personagem():
    def __init__(self,nome,x=0,y=0,experiencia=2,pokemons=[]):
        self.nome = nome
        self.x = x
        self.y = y
        self.experiencia = experiencia
        self.pokemons = pokemons

    def questao2(self,string):
        if string == 'cima':
            self.y = self.y+1
        elif string == 'baixo':
            self.y = self.y-1
        elif string == 'esquerda':
            self.x = self.x-1
        elif string == 'direita':
            self.x = self.x+1
        else:
            self.x = self.x
            self.y = self.y
        return self.x,self.y

    def questao3(self):
        n = random.randint(0,5)
        if n+self.experiencia >100:
            pass
        else:
            self.experiencia = self.experiencia+n
        return self.experiencia
    
    def questao4(self,npokemon,qntdefesa):
        forca_personagem = random.randint(-1,3)
        if self.experiencia+forca_personagem > qntdefesa:
            self.pokemons = self.pokemons+[npokemon]
            return 1
        else:
            return 0

    def questao5(self,nomepokemon,qntdefesa,x_pokemon,y_pokemon):
        if (self.x-x_pokemon >=-1 and self.x-x_pokemon <= 1) and (self.y-y_pokemon >=-1 and self.y-y_pokemon <=1):
            self.questao4(nomepokemon,qntdefesa)
            return self.x-x_pokemon,self.y-y_pokemon
        else:
            return self.x-x_pokemon,self.y-y_pokemon

class personagem2(personagem):
    def questao7(self,nome_pokemon):
        ocorrencias = 0
        for persona in self.pokemons:
            if persona == nome_pokemon:
                ocorrencias = ocorrencias+1
        return ocorrencias

    def questao4(self,nome,defesa):
        forca = random.randint(1,self.experiencia)
        qntdefesa = random.randint(1,defesa)
        if forca > qntdefesa:
            self.pokemons = self.pokemons+[nome]
            return 1
        else:
            return 0

random.seed(0)
print('--- Questao 1 ---')
meuPersonagem = personagem('Fernanda')
print('Atributos definidos no construtor: ')
print('Nome: ',meuPersonagem.nome)
print('Posicao x: ',meuPersonagem.x)
print('Posicao y:',meuPersonagem.y)
print('Experiencia: ',meuPersonagem.experiencia)
print('Lista de Pokemons: ',meuPersonagem.pokemons)

print('--- Questao 2 ---')
print('Andando para cima: ')
print(meuPersonagem.questao2('cima'))
print('Posicao: ',meuPersonagem.x,meuPersonagem.y)
print('Andando para a direita: ')
print(meuPersonagem.questao2('direita'))
print('Posicao: ',meuPersonagem.x,meuPersonagem.y)

print('--- Questao 3 ---')
print('Adquirindo experiencia: ')
print(meuPersonagem.questao3())
print('Experiencia: ',meuPersonagem.experiencia)
print('Adquirindo experiencia: ')
print(meuPersonagem.questao3())
print('Experiencia: ',meuPersonagem.experiencia)
        
print('--- Questao 4 ---')
print('Tentando capturar um Charmander: ')
print(meuPersonagem.questao4('Charmander',4))
print('Lista de Pokemons: ',meuPersonagem.pokemons)
print('Tentando capturar um Venusaur: ')
print(meuPersonagem.questao4('Venusaur',20))
print('Lista de Pokemons: ',meuPersonagem.pokemons)

print('--- Questao 5 ---')
print('Tentando capturar um Bulbasar: ')
print(meuPersonagem.questao5('Bulbasar',4,2,4))

print('Lista de Pokemons: ',meuPersonagem.pokemons)
print('Tentando capturar um Squirtle: ')
print(meuPersonagem.questao5('Squirtle',4,1,0))
print('Lista de Pokemons: ',meuPersonagem.pokemons)

print('--- Questao 6 ---')
meuNovoPersonagem = personagem2('Felipe')
print('Atributos definidos no construtor: ')
print('Nome: ',meuNovoPersonagem.nome)
print('Posicao x:',meuNovoPersonagem.x)
print('Posicao y:',meuNovoPersonagem.y)
print('Experiencia: ',meuNovoPersonagem.experiencia)
print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)

print('--- Questoes 7 e 8 ---')
print('Quantidade de Charmanders na lista: ')
print(meuNovoPersonagem.questao7('Charmander'))
print('Tentando capturar uma Caterpillar: ')
print(meuNovoPersonagem.questao4('Caterpillar',1))
print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
print('Tentando capturar uma outra Caterpillar: ')
print(meuNovoPersonagem.questao5('Caterpillar',1,0,0))
print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
print('Tentando capturar um Pigeon: ')
print(meuNovoPersonagem.questao4('Pigeon',2))
print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
print('Quantidade de Caterpillars na lista: ')
print(meuNovoPersonagem.questao7('Caterpillar'))
print('Quantidade de Pigeons na lista: ')
print(meuNovoPersonagem.questao7('Pigeon'))











