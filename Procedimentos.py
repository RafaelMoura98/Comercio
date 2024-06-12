import bd
import conexaobd
from datetime import datetime
#Menu Principal
conbd = conexaobd.conexao()


while True:
        print("Menu Cadastro")
        print("1. Cadastrar Produtos")
        print("2. Cadastrar Fornecedores")
        print("3. Cadastrar Clientes")
        print("4. Cadastrar Promoções")
        print("5. Cadastrar Funcionários")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            PNome = input("Digite o Nome do Produto: ")
            PDescricao = input("Digite a Descrição do Produto: ")
            PPreco = float(input("Digite o Valor do Produto: "))
            PQuantidade = int(input("Digite a Quantidade em Estoque: "))
            bd.cadprodutos(conbd,PNome,PDescricao,PPreco,PQuantidade)

        elif opcao == '2':
            FNome = input("Digite o Nome do Fornecedor: ")
            FContato = input("Digite o Contato do Fornecedor: ")
            FEndereco = input("Digite o Endereço do Fornecedor: ")
            bd.cadfornecedores(conbd,FNome,FContato,FEndereco)
        elif opcao == '3':
            CNome = input("Digite o Nome do Cliente: ")
            CSobrenome = input("Digite o Sobrenome do Cliente: ")
            CEndereco = input("Digite o Endereço do Cliente: ")
            CCidade = input("Digite a Cidade do Cliente: ")
            CCodigoPostal = input("Digite o Codigo Postal do Cliente: ")
            bd.cadclientes(conbd,CNome,CSobrenome,CEndereco,CCidade,CCodigoPostal)
        elif opcao == '4':
            PRNome = input("Digite o Nome da Promoção: ")
            PRDescricao = input("Digite a Descrição da Promoção: ")
            PRDataInicio= input("Digite a Data Inicial da Promoção(DD-MM-AAAA): ")
            PRDataFim = input("Digite a Data Final da Promoção(DD-MM-AAAA): ")
            PRDataInicio = datetime.strptime(PRDataInicio,"%d-%m-%y").strftime('%y-%m-%d')
            
            bd.cadpromocoes(conbd,PRNome,PRDescricao,PRDataInicio,PRDataFim)
        
        
        elif opcao == '5':
            FuncNome = input("Digite o Nome do Funcionário: ")
            FuncCargo = input("Digite o Cargo do Funcionário: ")
            FuncDepartamento= input("Digite o Departamento do Funcionário: ")
            bd.cadfuncionarios(conbd,FuncNome,FuncCargo,FuncDepartamento)
        
        elif opcao == '6':
            print("Saindo do programa...")
            break
        
        elif opcao == '7':
            bd.listarProdutos(conbd)

        else:
            print("Opção inválida! Tente novamente.")