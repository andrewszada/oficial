import re
import os
import pickle

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))


def validar_nome(nome):
    # Esta função verifica se o nome contém apenas letras e espaços
    if nome.replace(" ", "").isalpha():
        return True
    else:
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_endereço(endereço):
    # Esta função verifica se o nome contém apenas letras e espaços
    if endereço.replace(" ", "").isalpha():
        return True
    else:
        print("Endereço inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_telefone(numero):
    # Define o padrão para o número de telefone
    padrao = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')
    
    # Verifica se o número corresponde ao padrão
    if padrao.match(numero):
        return True
    else:
        return False
    
def aceitar_apenas_digitos(*args):
    for arg in args:
        if not isinstance(arg, str) or not arg.isdigit():
            return False
    return True

    
def acesso_admin():
    login = input("Qual é o login? ")
    senha = input("Qual é a senha? ")
    if login == 'andrews' and senha == 'projeto':
        return True
    else:
        return False


def salvar_arquivos_clientes(clientes):
    with open("clientes.dat", "wb") as arq_clientes:
            pickle.dump(clientes, arq_clientes)
        

def salvar_arquivos_produtos(produtos):
    with open("produtos.dat", "wb") as arq_produtos:
            pickle.dump(produtos, arq_produtos)

def salvar_arquivos_funcionarios(funcionarios):
    with open("funcionarios.dat", "wb") as arq_funcionarios:
            pickle.dump(funcionarios, arq_funcionarios)


#'contador dos clientes'''

    
def carregar_clientes():
    try:
        with open("clientes.dat", "rb") as arq_clientes:
            return pickle.load(arq_clientes)
    except FileNotFoundError:
        return {}



# Função para carregar contador do arquivo
def carregar_contador():
    try:
        with open("contador.dat", "rb") as arq_contador:
            return pickle.load(arq_contador)
    except FileNotFoundError:
        return 0

# Função para salvar contador no arquivo
def salvar_contador(contador):
    with open("contador.dat", "wb") as arq_contador:
        pickle.dump(contador, arq_contador)

# Função para incrementar o contador de clientes
def incrementar_contador():
    contador = carregar_contador()
    contador += 1
    salvar_contador(contador)
    return contador




# Exemplo de função para adicionar cliente
def adicionar_cliente(email, nome, endereço, telefone):
    clientes = carregar_clientes()
    clientes[email] = [nome, endereço, telefone]
    salvar_arquivos_clientes()
    contador = incrementar_contador()
    return contador
  
 
 
  #contador  das vendas'''

def carregar_vendas():
    try:
        with open("vendas.dat", "rb") as arq_vendas:
            return pickle.load(arq_vendas)
    except FileNotFoundError:
        return {}



# Função para carregar contador do arquivo
def carregar_contador1():
    try:
        with open("contador1.dat", "rb") as arq_contador1:
            return pickle.load(arq_contador1)
    except FileNotFoundError:
        return 0

# Função para salvar contador no arquivo
def salvar_contador1(contador1):
    with open("contador.dat", "wb") as arq_contador1:
        pickle.dump(contador1, arq_contador1)

# Função para incrementar o contador de clientes
def incrementar_contador1():
    contador1 = carregar_contador1()
    contador1 += 1
    salvar_contador1(contador1)
    return contador1

# Exemplo de função para adicionar cliente
def adicionar_vendas(id, nome_do_produto, quantidade_do_produto, valor_produto):
    produtos = carregar_vendas()
    produtos[id] = [nome_do_produto, quantidade_do_produto, valor_produto]
    salvar_arquivos_produtos()
    contador1 = incrementar_contador1()
    return contador1