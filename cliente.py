import caixa
import os 
import validador
import pickle
import produto

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
contador_cliente = 0
carrinho = {}
try:
  arq_carrinho = open("carrinho.dat", "rb")
  carrinho = pickle.load(arq_carrinho)
except:
  arq_carrinho = open("carrinho.dat", "wb")
  arq_carrinho.close()

clientes = {}
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
  arq_clientes.close()

def modulo_cliente():
    limpar_tela()
    print("_______________________________________")
    print("_______        Módulo Cliente      ____")
    print("_______________________________________")         
    print("____  1 - Cadastrar Cliente       _____")
    print("_____ 2 - Exibir Dados do Cliente  ____")
    print("_____ 3 - Alterar Dados do Cliente ____")
    print("_____ 4 - Excluir Cliente         _____")
    print("_____ 0 - Sair                    _____")
    op_cliente = input("##### Escolha sua opção:  ")
    return op_cliente

def cadastrar_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Cadastrar Cliente         _____")
    print("____________________________________________")
    nome = input("Qual seria o seu nome completo? ")
    while not validador.validar_nome(nome):
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        nome = input("Qual o seu nome ")
    email = input("Qual o seu e-mail: ")
    while not validador.validar_email(email):
        print("Email inválido. Por favor, digite um email válido.")
        email = input("Qual o seu e-mail: ")
    endereço = input("Qual o seu endereço completo? ")
    while not validador.validar_endereço(endereço):
        print("Endereço inválido. Por favor, insira apenas letras e espaços.")
        endereço = input("Qual o seu endereço? ")
    telefone = input("Qual o seu número de telefone? ")
    while not validador.validar_telefone(telefone):
        print("Telefone inválido. Por favor, insira seu número corretamente (Use o travessão para separar o números)")
        telefone = input("Qual é o seu número de telefone? ")
    clientes[email] = [nome, endereço, telefone]
    validador.adicionar_cliente
    validador.salvar_arquivos_clientes(clientes)
    print(clientes)

def exibir_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____         Exibir Dados do Cliente  _____")
    print("____________________________________________")
    email = input("Digite o email do cliente: ")
    if email in clientes:
        print("Nome:", clientes[email][0])
        print("Endereço:", clientes[email][1])
        print("Telefone:", clientes[email][2])
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")

def alterar_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Alterar Dados do Cliente  _____")
    print("____________________________________________")
    email = input("Digite o email do cliente: ")
    if email in clientes:
        print("Informe os novos dados do(a) cliente: ")
        nome = input("Nome: ")
        while not validador.validar_nome(nome):
            print("Nome inválido. Por favor, insira apenas letras e espaços.")
            nome = input("Qual o seu nome ")
        endereço = input("Endereço: ")
        while not validador.validar_endereço(endereço):
            print("Endereço inválido. Por favor, insira apenas letras e espaços.")
            endereço = input("Qual o seu endereço? ")
        telefone = input("Celular: ")
        while not validador.validar_telefone(telefone):
            print("Telefone inválido. Por favor, insira seu número corretamente (Use o travessão para separar o números)")
            telefone = input("Qual é o seu número de telefone? ")
        clientes[email] = [nome, endereço, telefone]
        validador.salvar_arquivos_clientes(clientes)
        print("Cliente alterado(a) com sucesso!")
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")

def excluir_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Excluir Cliente           _____")
    print("____________________________________________")
    email = input("Digite o email do cliente que deseja excluir: ")
    if email in clientes:
        del clientes[email]
        caixa.cliente_deletado()
        validador.salvar_arquivos_clientes(clientes)
        print("Cliente excluído com sucesso.")
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")


def exibir_produtos():
    print("|--------------------------------------------------------------------------------|")
    print("|                                    Produtos                                    |")
    print("|--------------------------------------------------------------------------------|")
    print("|   ID   |      Nome       |    Quantidade   |    Valor    |")
    print("|--------|-----------------|-----------------|-------------|")
    
    for id, info in produto.produtos.items():
        try:
            # Tente converter info[2] para float
            valor = float(info[2])
            linha = f'| {id:<6} | {info[0]:<15} | {info[1]:<15} | {valor:<11.2f} |'
        except ValueError:
            # Se a conversão falhar, exiba um aviso ou trate o erro conforme necessário
            linha = f'| {id:<6} | {info[0]:<15} | {info[1]:<15} | {"Erro":<11} |'
        
        print(linha)
        input("Pressione ENTER para ver mais produtos\n")
    
    print("|--------------------------------------------------------------------------------|")

