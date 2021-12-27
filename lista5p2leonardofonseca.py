def menu():
   print('1 - Inserir um ou mais medicos')
   print('2 - Inserir um ou mais pacientes')
   print('3 - Agendar consulta')
   print('4 - Listar consultas de um médico')
   print('5 - Listar os médicos')
   print('6 - Remover consulta')
   print('7 - Imprimir dados dos pacientes')
   print('0 - Sair do programa')
   opcao = input('Digite uma das opcoes acima: ')
   return opcao

'''RETORNA UMA TUPLAS DE TUPLAS COM O NOME DO MEDICO E SUA ESPECIALIDADE '''
def InserirMedicosEspec(tuplasmedicos):
    cond = ''
    InfoMedicos = ()
    while cond!= 'n':
        n_medico = input('Digite o nome do medico: ')
        especi_medico = input('Digite a especialidade do medico: ')
        info = (n_medico,especi_medico)
        InfoMedicos = InfoMedicos+(info,)
        cond = input('Deseja inserir outro medico? s/n: ')
    tuplasmedicos = tuplasmedicos+(InfoMedicos)
    return tuplasmedicos

'''RETORNA UMA TUPLA DE TUPLAS COM O NOME DO PACIENTE, SUA ALTURA E SUA IDADE'''
def InserirPacientes(tuplaspacientes):
    cond = ''
    InfoPacientes = ()
    while cond!= 'n':
        nome_paciente = input('Digite o nome do paciente: ')
        idade_paciente = input('Digite a idade do paciente: ')
        altura_paciente = input('Digite a altura do paciente: ')
        idade_paciente = int(idade_paciente)
        altura_paciente = float(altura_paciente)
        info = (nome_paciente,idade_paciente,altura_paciente)
        InfoPacientes = InfoPacientes+(info,)
        cond = input('Deseja inserir outro paciente? s/n: ')
    tuplaspacientes = tuplaspacientes+(InfoPacientes)
    return tuplaspacientes



def verificarmarcar(agendaref,agenda,medico,paciente):
    day = input('Digite o dia: ')
    day = int(day)
    mes = input('Digite o mes: ')
    mes = int(mes)
    ano = input('Digite o ano: ')
    ano = int(ano)
    horario = input('Digite a hora: ')
    horario = int(horario)
    desejo = (medico,paciente,day,mes,ano,horario)
    desejoref = (medico,day,mes,ano,horario)
    agendado = ()
    agendadoref = ()
    if desejoref in agendaref:
        print('O medico nao esta desponivel nesse dia e horario.')
    else:
        desejoref = (medico,day,mes,ano,horario)
        agendadoref = agendadoref+(desejoref,)
        desejo = (medico,paciente,day,mes,ano,horario)
        agendado = agendado+(desejo,)
        print('Consulta agendada com sucesso.')
    agenda = agenda+(agendado)
    agendaref = agendaref+(agendadoref)
    return agenda,agendaref


    


def agendarconsulta(listaDEpacientes,listaDEmedicos):
    nome_paciente = input('Digite o nome do paciente: ')
    pessoa = ''
    profissional = ''
    for paciente,idade,altura in listaDEpacientes:
        pessoa = pessoa+paciente
    for medico,especialidade in listaDEmedicos:
        profissional = profissional+medico
    if nome_paciente.upper() not in pessoa.upper():
        return False,False
    else:
        paciente = nome_paciente
        nome_medico = input('Digite o nome do medico: ')
        pergunta = ''
        if nome_medico.upper() not in profissional.upper():
            pergunta = input('Medico nao encontrado. Deseja sair? s/n: ')
            while pergunta!='s':
                nome_medico = input('Digite o nome do medico: ')
                if nome_medico.upper() in profissional.upper():
                    medico = nome_medico
                    break
                pergunta = input('Voce deseja sair? s/n: ')
        else:
            medico = nome_medico
        return medico,paciente
            


def medicoscadastrados(listaMedicos):
    especialidade = input('Digite a especialidade desejada (digite qualquer para listar todos): ')
    if especialidade.upper() == 'qualquer'.upper():
        for info in listaMedicos:
            informacao = 'Nome: {0}, Especialidade: {1}'.format(info[0],info[1])
            print(informacao)
    else:
        print('Nomes dos medicos encontrados: ')
        for info2 in listaMedicos:
            if especialidade.upper()==info2[1].upper():
                print(info2[0])

def pacientescadastrados(listaPacientes):
    print('Pacientes cadastrados: ')
    for tuplas in listaPacientes:
        informacao = 'Nome: {}, Idade: {}, Altura: {:.2f}'.format(tuplas[0],tuplas[1],tuplas[2])
        print(informacao)

def retirarconsulta(medico,listamarcadas,listaref):
    paciente = input('Digite o nome do paciente: ')
    day = input('Digite o dia: ')
    day=int(day)
    mes = input('Digite o mes: ')
    mes = int(mes)
    ano = input('Digite o ano: ')
    ano = int(ano)
    horario = input('Digite a hora: ')
    horario = int(horario)
    consulta = (medico,paciente,day,mes,ano,horario)
    consultaRef = (medico,day,mes,ano,horario)
    novatupla = ()
    novatuplaRef = ()
    if consulta not in listamarcadas:
        print('Consulta nao encontrada.')
    else:
        for subtuplaref in listaref:
            if consultaRef!=subtuplaref:
                novatuplaRef = novatuplaRef+(consultaRef)


        for subtupla in listamarcadas:
            if subtupla!=consulta:
                novatupla = novatupla+(subtupla,)
    return novatupla,novatuplaRef



def main1():
    tuplaspacientes = ()
    tuplasmedicos = ()
    consultasmarcadas =()
    consultasRef = ()
    while True:
        op = menu()
        if op == '1':
           tuplasmedAtualizadas = InserirMedicosEspec(tuplasmedicos)
           tuplasmedicos = tuplasmedAtualizadas
        elif op =='2':
            tuplaspacAtualizadas = InserirPacientes(tuplaspacientes)
            tuplaspacientes = tuplaspacAtualizadas  
        elif op == '3':
            medico,paciente = agendarconsulta(tuplaspacientes,tuplasmedicos)
            if medico==False and paciente==False:
                print('Paciente nao encontrado, antes de agendar a consulta, cadastre o paciente.')
            else:
                consultasAtualizadas,consultasRef_Atualizada = verificarmarcar(consultasRef,consultasmarcadas,medico,paciente)
                consultasmarcadas = consultasAtualizadas
                consultasRef = consultasRef_Atualizada
        
        elif op == '4':
            doutor = input('Digite o nome do medico: ')
            tuplaProv = ()
            for medico,especialidade in tuplasmedicos:
                medico = medico.upper()
                tuplaProv = tuplaProv+(medico,)
            if doutor.upper() not in tuplaProv:
                print('Medico nao encontrado.')
            else:
                informar = 'O medico {} possui as seguintes consultas agendadas:'.format(doutor)
                print(informar)
                for profissional,pessoa,dia,mes,ano,hora in consultasmarcadas:
                    if doutor.upper()==profissional.upper():
                        informar = 'Paciente: {}, Dia: {}/{}/{}, Hora: {}h'.format(pessoa,dia,mes,ano,hora)  
                        print(informar)
        elif op =='5':
            medicoscadastrados(tuplasmedicos)
        elif op == '6':
            NomeMedico = input('Digite o nome do medico: ')
            dr = ''
            for subtupla in consultasmarcadas:
                dr = subtupla[0]
                dr = dr.upper()
                dr = dr+dr
            if NomeMedico.upper() not in dr:
                print('O medico nao possui consultas.')
            else:
                informar = 'O medico {} possui as seguintes consultas agendadas:'.format(NomeMedico)
                print(informar)
                for profissional,pessoa,dia,mes,ano,hora in consultasmarcadas:
                    if NomeMedico.upper()==profissional.upper():
                        informar = 'Paciente: {}, Dia: {}/{}/{}, Hora: {}'.format(pessoa,dia,mes,ano,hora)  
                        print(informar)
                agendaAtualizada,consultasRef_atu = retirarconsulta(NomeMedico,consultasmarcadas,consultasRef)
                consultasmarcadas = agendaAtualizada
                consultasRef = consultasRef_atu
            
        elif op == '7':
            pacientescadastrados(tuplaspacientes)
        elif op == '0':
            return tuplasmedicos,tuplaspacientes,consultasmarcadas
        else:
            print('Opcao invalida')


print(main1())







        







