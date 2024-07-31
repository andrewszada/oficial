import caixa
import os 
import validador 
import pickle
import mainn


def limpar_tela():
 os.system('cls' if os.name == 'nt' else 'clear')


def carregar_produtos():
    try:
        with open("produtos.dat", "rb") as arq_produtos:
            return pickle.load(arq_produtos)
    except FileNotFoundError:
        return {}

carrinho = {}
try:  
  arq_carrinho = open("carrinho.dat", "rb")
  produtos = pickle.load(arq_carrinho)
except:
  arq_carrinho = open("carrinho.dat", "wb")
  arq_carrinho.close()

produtos = {}
try:  
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
  arq_produtos.close()

def modulo_produto():
    op_produto = ''
    while op_produto != '0':
        limpar_tela()
        print("_______________________________________")
        print("_______           Módulo Produto_______")
        print("_______________________________________")         
        print("____  1 - Cadastrar Produto       _____")
        print("_____ 2 - Exibir Dados do Produto _____")
        print("_____ 3 - Alterar Dados do Produto ____")
        print("_____ 4 - Excluir Produto         _____")
        print("_____ 5 - Exibir produtos         _____")
        print("_____ 6 - Adicionar ao carrinho   _____")
        print("_____ 0 - Sair                    _____")
        op_produto = input("##### Escolha sua opção: ")
        return op_produto
        

def cadastrar_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Cadastrar Produto         _____")
    print("____________________________________________")
    print()
    id = str(len(produtos) + 1)
    nome_do_produto = input("Qual é o nome do produto desejado? ")
    while not validador.validar_nome(nome_do_produto):
        print("Nome de produto inválido. Por favor, insira apenas letras e espaços.")
        nome_do_produto = input("Qual o nome do produto ")
    else:
        print("Nome válido")
    
    quantidade_do_produto = input("Qual a quantidade do produto desejada: ")
    while not validador.aceitar_apenas_digitos(quantidade_do_produto):
        print("Quantidade de produto inválido, digite novamente")
        quantidade_do_produto = input("Qual a quantidade do produto desejada? ")
    else:
        print("Quantidade de produto válido")
    
    valor_produto = input("Qual será o valor desse produto? ")
    while not validador.aceitar_apenas_digitos(valor_produto):
        print("Digite apenas números")
        valor_produto = float(input("Qual será o valor desse produto "))
    else:
        print("Valor válido")
    
    
    produtos[id] = [nome_do_produto, quantidade_do_produto, valor_produto]
    validador.salvar_arquivos_produtos(produtos)
    print("Produto cadastrado com sucesso")
    input("Aperete ENTER para continuar..")      

def exibir_produtos():
    print("|--------------------------------------------------------------------------------|")
    print("|                                    Produtos                                    |")
    print("|--------------------------------------------------------------------------------|")
    print("|   ID   |      Nome       |    Quantidade   |    Valor    |")
    print("|--------|-----------------|-----------------|-------------|")
    
    for id, info in produtos.items():
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



def adicionar_ao_carrinho():
    carrinho = []
    while True:
        exibir_produtos()
        id = input("Digite o ID do produto que deseja adicionar ao carrinho (ou 'sair' para finalizar): ")

        if id.lower() == 'sair':
            break

        if id in produtos:
            produto_selecionado = produtos[id]
            carrinho.append([id, produto_selecionado[0], int(produto_selecionado[1]), float(produto_selecionado[2])])
            print(f"{produto_selecionado[0]} adicionado ao carrinho.")

            escolha = input("Deseja ver a situação de seu carrinho? (Digite sim ou não) ")
            if escolha.lower() == "sim":
                limpar_tela()
                total = sum(item[3] for item in carrinho)  # item[3] contém o valor do produto
                print("|--------------------------------------------------------------------------------|")
                print("|                                    Carrinho                                    |")
                print("|--------------------------------------------------------------------------------|")
                print("|   ID   |      Nome       |     Valor     |")
                print("|--------|-----------------|---------------|")

                for item in carrinho:
                    linha = f'| {item[0]:<6} | {item[1]:<15} | {item[3]:<11.2f} |'
                    print(linha)

                print("|--------------------------------------------------------------------------------|")
                print(f"O total no seu carrinho é: R${total:.2f}")
                finalizar_compra = input("Deseja finalizar a compra? (S/N): ")
                if finalizar_compra.upper() == "S":
                    validador.adicionar_vendas

                    print("Compra finalizada com sucesso!")
                    carrinho.clear()
                else:
                    print("Compra não finalizada.")
                input("Pressione ENTER para continuar...")

        else:
            print("ID inválido. Por favor, tente novamente.")

    return carrinho



def alterar_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Alterar Dados do Produto  _____")
    print("____________________________________________")
    print()
    id = input("Digite o id do cliente: ")
    if id in produtos:
        print("Informe os novos dados do(a) produto: ")
        nome_do_produto = input("Nome do produto : ")
        while not validador.validar_nome(nome_do_produto):
            print("Nome inválido. Por favor, insira apenas letras e espaços.")
            nome_do_produto = input("Qual o nome do produto?")
        else:
            print("Nome válido")
        print()
        quantidade_do_produto = input("Qual a quantidade do produto desejada: ")
        while not validador.aceitar_apenas_digitos(quantidade_do_produto):
            print("Quantidade de produto inválido, digite novamente")
            quantidade_do_produto = input("Qual a quantidade do produto desejada? ")
        else:
           print("Quantidade de produto válido")

        valor_produto = input("Qual será o valor desse produto? ")
        while not validador.aceitar_apenas_digitos(valor_produto):
            print("Digite apenas números")
            valor_produto = float(input("Qual será o valor desse produto "))
        else:
            print("Valor válido")
        produtos[id] = [nome_do_produto, quantidade_do_produto, valor_produto]
        validador.salvar_arquivos_produtos(produtos)
        print ("Informações de produto alterados com sucesso ")    
        input ("Pressione ENTER para continuar..")

def excluir_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Excluir Produto           _____")
    print("____________________________________________")
    print()
    id = input("Digite o id do produto que deseja excluir: ")
    if id in produtos:
        del produtos[id]
        validador.salvar_arquivos_produtos(produtos)
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")
    input("Pressione ENTER para continuar...")   



arq_produtos = open("produtos.dat", "wb")
pickle.dump(produtos, arq_produtos)  
arq_produtos.close()

arq_carrinho = open("carrinho.dat", "wb")
pickle.dump(carrinho, arq_carrinho)
arq_carrinho.close()
