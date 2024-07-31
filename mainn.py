import cliente
import produto
import caixa
import utils
import os
import funcionarios

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    limpar_tela()
    print("_______________________________________")
    print("__ Sistema de Gestão de Loja para Bebês _____")
    print("_______________________________________")
    print("____   1 - Módulo Cliente         _____")
    print("_____  2 - Módulo Produto/Vendas  _____")    
    print("_____  3 - Módulo Caixa           _____")
    print("_____  4 - Módulo Carrinho        _____")
    print("_____  5 - Módulo Administração   _____")
    print("_____  0 - Sair                   _____")
    op_princ = input("##### Escolha sua opção: ")
    return op_princ

if __name__ == "__main__":
    op_princ = ''
    while op_princ != '0':
        op_princ = menu_principal()

        if op_princ == '1':
            op_cliente = ''
            while op_cliente != '0':
                op_cliente = cliente.modulo_cliente()
                if op_cliente == '1':
                    cliente.cadastrar_cliente()
                elif op_cliente == '2':
                    cliente.exibir_cliente()
                elif op_cliente == '3':
                    cliente.alterar_cliente()
                elif op_cliente == '4':
                    cliente.excluir_cliente()
                
        elif op_princ == '2':
            op_produto = ''
            while op_produto != '0':
                op_produto = produto.modulo_produto()
                if op_produto == '1':
                    produto.cadastrar_produtos()
                elif op_produto == '2':
                    produto.exibir_produtos()   
                elif op_produto == '3':
                    produto.alterar_produtos()
                elif op_produto == '4':
                    produto.excluir_produtos()
                elif op_produto == '5':
                    produto.exibir_produtos()
                elif op_produto == '6':
                    produto.adicionar_ao_carrinho()
                
        elif op_princ == '3':
            op_caixa = ''
            while op_caixa != '0':
                op_caixa = caixa.modulo_caixa()
                if op_caixa == '1':
                    caixa.caixa_estoque()
                elif op_caixa == '2':
                    caixa.caixa_comprar()
                elif op_caixa == '3':
                    caixa.gerar_relatorio()
        
        elif op_princ == '4':
            op_admin = ''
            while op_admin != '0':
                op_admin = funcionarios.modulo_admin()
                if op_admin == '1':
                    funcionarios.cadastrar_funcionarios()
                elif op_admin == '2':
                    funcionarios.exibir_funcionarios()
                elif op_admin == '3':
                    funcionarios.alterar_funcionario()
                elif op_admin == '4':
                    funcionarios.demitir_funcionario()
