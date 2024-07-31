import validador
import os 
import validador
import pickle

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
contador_cliente = 0
funcionarios = {}
try:
  arq_funcionarios = open("funcionarios.dat", "rb")
  funcionarios = pickle.load(arq_funcionarios)
except:
  arq_funcionarios = open("funcionarios.dat", "wb")
  arq_funcionarios.close()


def modulo_admin():
    limpar_tela()
    print("_______________________________________    ")
    print("_______        Módulo Funcionários  _______")
    print("_______________________________________    ")         
    print("____  1 - Cadastrar Funcionário       _____")
    print("_____ 2 - Exibir Dados do Funcionário  ____")
    print("_____ 3 - Alterar Dados do Funcionário ____")
    print("_____ 4 - Demitir Funcionário         _____")
    print("_____ 0 - Sair                        _____")
    op_admin = input("##### Escolha sua opção:  ")
    return op_admin

def cadastrar_funcionarios():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Cadastrar Funcionário     _____")
    print("____________________________________________")
    print()
    nome_funcionario = input("Qual é o nome do funcionário? ")
    while not validador.validar_nome(nome_funcionario):
        print("Nome de funcionário inválido. Por favor, insira apenas letras e espaços.")
        nome_funcionario = input("Qual o nome do funcionário ")
    else:
        print("Nome válido")
    email = input ("Digite o e-mail de contato do funcionário ")
    while not validador.validar_email(email):
        print("Email inválido. Por favor, digite um email válido.")
        email = input("Qual o seu e-mail: ")
    else:
        print("E-mail válido")
        input("Pressione ENTER para continuar...")
        print()
    telefone = input("Qual é o número de telefone de contato do funcionário ")
    while not validador.validar_telefone(telefone):
        print("Número de telefone inválido, exemplo de formato aceito (55)55555-5555")
        telefone = input("Qual é o número de telefone de contato do funcionário ")
    else:
        print("Número válido")
        input("Aperte ENTER para continuar")
    funcao_funcionario = input("Qual é a função do funcionário? ")
    while not validador.validar_nome(funcao_funcionario):
        print("Função de funcionário inválido. Por favor, insira apenas letras e espaços.")
        funcao_funcionario = input("Qual é a função do funcionário? ")
    else:
        print("Função de funcionário válido")
        input("Aperte ENTER para continuar")
    funcionarios[email] = [nome_funcionario, telefone, funcao_funcionario]
    validador.salvar_arquivos_funcionarios(funcionarios)
    print("Funcionário cadastrado com sucesso")
    input("Aperte ENTER para continuar..")


def exibir_funcionarios():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____         Exibir Dados do Funcionário  _____")
    print("____________________________________________")
    print()
    email = input("Digite o email do funcionario: ")
    if email in funcionarios:
        print("Nome do funcionário:", funcionarios[email][0])
        print("Telefone do funcionário:", funcionarios[email][1])
        print("Função do funcionário", funcionarios[email][2])
        input("Pressione ENTER para continuar...")
        
    else:
        print("Funcionário não encontrado.")
    input("Pressione ENTER para continuar...")

def alterar_funcionario():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Alterar Dados do Funcionário  _____")
    print("____________________________________________")
    print()
    email = input("Digite o email do funcionário: ")
    if email in funcionarios:
        print("Informe os novos dados do funcionário: ")
        nome_funcionario = input("Qual é o nome do funcionário?")
    while not validador.validar_nome(nome_funcionario):
        print("Nome de funcionário inválido. Por favor, insira apenas letras e espaços.")
        nome_funcionario = input("Qual o nome do funcionário ")
    else:
        print("Nome válido")
    email = input ("Digite o e-mail de contato do funcionário")
    while not validador.validar_email(email):
        print("Email inválido. Por favor, digite um email válido.")
        email = input("Qual o seu e-mail: ")
    else:
        print("E-mail válido")
        input("Pressione ENTER para continuar...")
        print()
    telefone = input("Qual é o número de telefone de contato do funcionário")
    while not validador.validar_telefone(telefone):
        print("Número de telefone inválido, exemplo de formato aceito (55) 55555-5555")
        telefone = input("Qual é o número de telefone de contato do funcionário")
    else:
        print("Número válido")
        input("Aperte ENTER para continuar")
    funcao_funcionario = input("Qual é a função do funcionário?")
    while not validador.validar_nome(funcao_funcionario):
        print("Função de funcionário inválido. Por favor, insira apenas letras e espaços.")
        funcao_funcionario = input("Qual é a função do funcionário?")
    else:
        print("Função de funcionário válido")
        input("Aperte ENTER para continuar")
    funcionarios[email] = [nome_funcionario, telefone, funcao_funcionario]
    validador.salvar_arquivos_funcionarios(funcionarios)
    print("Dados de funcionário alterado com sucesso")
    input("Aperte ENTER para continuar...")

def demitir_funcionario():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Demitir Funcionário          _____")
    print("____________________________________________")
    print()
    email = input("Digite o email do funcionário que você deseja demitir: ")
    if email in funcionarios:
        del funcionarios[email]
        validador.salvar_arquivos_funcionarios(funcionarios)
        print("Funcionário demitido com sucesso.")
        input("Pressione ENTER para continuar...")
    else:
        print("Funcionário não encontrado.")
    input("Pressione ENTER para continuar...")   


arq_funcionarios = open("funcionarios.dat", "wb")
pickle.dump(funcionarios, arq_funcionarios)  
arq_funcionarios.close()