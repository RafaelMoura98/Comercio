import bd
import conexaobd
from datetime import datetime
from mysql.connector import Error
#Menu Principal
conbd = conexaobd.conexao()

while True:
        print("Menu Principal")
        print("Funções")
        print("1. Cadastrar ")
        print("2. Deletar ")
        print("3. Atualizar ")
        print("4. Listar ")
        print("5. Pedidos ")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")


        if opcao == '1': 
            PNome = input("Digite o Nome do Produto: ")
            confirme = input("Você está prestes a excluir um Item " + PNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.DelProdutos(conbd,PNome)
            else:
                break