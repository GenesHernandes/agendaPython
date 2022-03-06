def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
    ========================================================
                        AGENDA EM PYTHON
    MENU:
        
    [1]CADASTRAR CONTATO
    [2]BUSCAR CONTATO PELO NOME
    [3]LISTAR CONTATOS
    [4]DELETAR CONTATO
    [5]SAIR
    =========================================================
    ESCOLHA UMA DAS OPÇÕES ACIMA: 
    ''')
        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            buscarContatoPeloNome()
        elif opcao == '3':
            listarContato()
        elif opcao == '4':
            deletarContato()
        else:
            print('Fim!')
            sair()
        voltarMenuPrincipal=input('Deseja voltar ao menu principal? (s/n) ').lower()

def cadastrarContato():
    nome = input('Escreva o nome do contato: ')
    telefone = input('Escreva o telefone do contato: ')
    email =  input('Escreva o email do contato: ')
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'CONTATO GRAVADO COM SUCESSO!')
    except:
        print('ERRO na gravação do contato!')

def buscarContatoPeloNome():
    nome = input('Digite um nome para busca: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[0].upper():
            print(contato)
    agenda.close()

def listarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletar = input('Digite o nome que deseja apagar: ').lower()
    agenda = open('agenda.txt', 'r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletar not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'O contato foi apagado.')
    listarContato()

def sair():
    exit()

def main():
    menu()
main()

