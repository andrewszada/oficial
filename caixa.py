from utils import limpar_tela
import produto
import validador 
import cliente


contador = validador.carregar_clientes
contador1 = validador.carregar_vendas

def modulo_caixa():
    op_caixa = ''
    while op_caixa != '0':
        limpar_tela()
        print("_______________________________________")
        print("_______           Módulo Caixa   ______")
        print("_______________________________________")
        print("____  1 - Controle de Estoque     _____")
        print("____  2 - Comprar produtos        _____")
        print("____  3 - Relatório de vendas     _____")
        print("_____ 0 - Sair                    _____")
        op_caixa = input("##### Escolha sua opção: ")
        return op_caixa
        


def caixa_estoque():
    print("|--------------------------------------------------------------------------------|")
    print("|                                    Produtos                                    |")
    print("|--------------------------------------------------------------------------------|")
    print("|   ID   |      Nome       |    Quantidade   |    Valor    |")
    print("|--------|-----------------|-----------------|-------------|")
    
    #info ta interando os valores e a chaves do dicionário produtos 
    for id, info in produto.produtos.items():
        try:
            # Tente converter info[2] para float
            valor = float(info[2])
            linha = f'| {id:<6} | {info[0]:<15} | {info[1]:<15} | {valor:<11.2f} |'
        except ValueError:
            # Se a conversão falhar, exiba um aviso ou trate o erro conforme necessário
            linha = f'| {id:<6} | {info[0]:<15} | {info[1]:<15} | {"Erro":<11} |'
        
        print(linha)
        
    
    print("|--------------------------------------------------------------------------------|")
    input("Pressione ENTER para continuar")

def caixa_comprar():
    print()
    print("____________________________________________")
    print("_____        Comprar produtos         _____ ")
    print("____________________________________________")
    print()
    produto.carregar_produtos()
    id = int(input("Qual é o ID de verificação de estoque desejado? "))

    if id in produto.produtos.items():
        produtos = produto.produtos[id]
        quantidade = int(input(f"Você deseja adicionar quantas unidades do produto {produtos[0]}? "))
        quantidade += produto.produtos[id][1]  
        print(f"Foram adicionadas {quantidade} unidades do produto {produtos[0]} ao seu estoque.")
        input("Aperte ENTER para continuar")
    else:
        print("ID de produto não encontrado no estoque.")
        input("Pressione ENTER para continuar...")



def gerar_relatorio():
    
    print("|--------------------------------------------------------------------------------|")
    print("|                             Relatório de Clientes                              |")
    print("|--------------------------------------------------------------------------------|")
    print("|   Nome do Cliente        |  Endereço                |  E-mail                  |")
    print("|--------------------------|--------------------------|--------------------------|")
    
    for email, dados in cliente.clientes.items():
        nome = dados[0]
        endereço = dados[1]
        linha = f'| {email:<25} | {dados[0]:<24} | {dados[1]:<24} |'
        print(linha)
    
    print("|-------------------------------------------------------------------------------|")
    input("Pressione ENTER para continuar...")


