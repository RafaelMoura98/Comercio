import bd
import conexaobd
from datetime import datetime
from mysql.connector import Error
#Menu Principal
conbd = conexaobd.conexao()

while True:
        print("Menu Atualizar")
        print("1. Atualizar Produtos")
        print("2. Atualizar Fornecedores")
        print("3. Atualizar Clientes")
        print("4. Atualizar Promoções")
        print("5. Atualizar Funcionários")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")


        if opcao == '1': 
            PNome = input("Digite o Nome do Produto: ")
            confirme = input("Você está prestes a excluir um Item " + PNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.DelProdutos(conbd,PNome)
            else:
                break