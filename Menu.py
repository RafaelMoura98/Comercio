import bd
import conexaobd
import FuncPedido
from datetime import datetime

#Menu Principal
conbd = conexaobd.conexao()

def MenuCadastro():
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
            bd.CadProdutos(conbd,PNome,PDescricao,PPreco,PQuantidade)

        elif opcao == '2':
            FNome = input("Digite o Nome do Fornecedor: ")
            FContato = input("Digite o Contato do Fornecedor: ")
            FEndereco = input("Digite o Endereço do Fornecedor: ")
            bd.CadFornecedores(conbd,FNome,FContato,FEndereco)
        
        elif opcao == '3':
            CNome = input("Digite o Nome do Cliente: ")
            CSobrenome = input("Digite o Sobrenome do Cliente: ")
            CEndereco = input("Digite o Endereço do Cliente: ")
            CCidade = input("Digite a Cidade do Cliente: ")
            CCodigoPostal = input("Digite o Codigo Postal do Cliente: ")
            bd.CadClientes(conbd,CNome,CSobrenome,CEndereco,CCidade,CCodigoPostal)
        
        elif opcao == '4':
            PRNome = input("Digite o Nome da Promoção: ")
            PRDescricao = input("Digite a Descrição da Promoção: ")
            PRDataInicio= input("Digite a Data Inicial da Promoção(DD-MM-AAAA): ")
            PRDataInicio = datetime.strptime(PRDataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
            PRDataFim = input("Digite a Data Final da Promoção(DD-MM-AAAA): ")
            PRDataFim = datetime.strptime(PRDataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
            bd.CadPromocoes(conbd,PRNome,PRDescricao,PRDataInicio,PRDataFim)
    
        elif opcao == '5':
            FuncNome = input("Digite o Nome do Funcionário: ")
            FuncCargo = input("Digite o Cargo do Funcionário: ")
            FuncDepartamento= input("Digite o Departamento do Funcionário: ")
            bd.CadFuncionarios(conbd,FuncNome,FuncCargo,FuncDepartamento)
        
        elif opcao == '6':
            print("Voltar ao Menu Principal")
            break
        else:
            print("Opção inválida! Tente novamente.")

def MenuDeletar():
    while True:
        print("Menu Deletar")
        print("1. Deletar Produto")
        print("2. Deletar Fornecedor")
        print("3. Deletar Cliente")
        print("4. Deletar Promoção")
        print("5. Deletar Funcionário")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            PNome = input("Digite o Nome do Produto: ")
            confirme = input("Você está prestes a excluir um Item " + PNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.delprodutos(conbd,PNome)
            else:
                break
        
        elif opcao == '2':
            FNome = input("Digite o Nome do Fornecedor: ")
            confirme = input("Você está prestes a excluir o Fornecedor " + FNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.delfornecedores(conbd,FNome)
            else:
                break
        elif opcao == '3':
            CNome = input("Digite o Nome do Cliente: ")
            confirme = input("Você está prestes a excluir o Cliente " + CNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.delclientes(conbd,CNome)
            else:
                break
        elif opcao == '4':
            PRNome = input("Digite o Nome da Promoção: ")
            confirme = input("Você está prestes a excluir a Promoção " + PRNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.delpromocoes(conbd,PRNome)
            else:
                break
        elif opcao == '5':
            FUNome = input("Digite o Nome do Funcionário: ")
            confirme = input("Você está prestes a excluir o Funcionário " +FUNome + " do Banco de Dados Deseja continuar? (sim ou não): ")
            if confirme == "sim":
                bd.delfuncionarios(conbd,FUNome)
            else:
                break
        elif opcao == '6':
            print("Voltar ao Menu Principal")
            break
        else:
            print("Opção inválida! Tente novamente.")

def MenuAtualizar():
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
            ANome = input("Digite o Novo Nome do o Produto: ")
            ADesc = input("Digite a Nova Descrição do o Produto: ")
            APreco = float(input("Digite o Novo Preço do o Produto: "))
            Nome = input("Digite o Nome do Produto que você quer Alterar: ")

            bd.AtualizarProdutos(conbd,ANome,ADesc,APreco,Nome)
            
        elif opcao == '2':
            ANome = input("Digite o Novo Nome do Fornecedor: ")
            AContato = input("Digite o Novo Contato do Fornecedor: ")
            AEndereco = input("Digite o Novo Endereço do Fornecedor: ")
            Nome = input("Digite o Nome do Fornecedor que você quer Alterar as informações: ")
            
            bd.AtualizarFornecedores(conbd,ANome,AContato,AEndereco,Nome)

        elif opcao == '3':
            ANome = input("Digite o Novo Nome do Cliente: ")
            ASobrenome = input("Digite o Novo Sobrenome do Cliente: ")
            AEndereco = input("Digite o Novo Endereço do Cliente: ")
            ACidade = input("Digite a Nova Cidade do Cliente: ")
            ACodigoPostal = input("Digite o Novo Código Postal do Cliente: ")
            Nome = input("Digite o Nome do Cliente que você quer Alterar as informações: ")

            bd.AtualizarClientes(conbd,ANome,ASobrenome,AEndereco,ACidade,ACodigoPostal,Nome)
        elif opcao == '4':
            ANome = input("Digite o Novo Nome da Promoção: ")
            ADescricao = input("Digite a Nova Descrição da Promoção: ")
            ADataInicio = input("Digite a Nova Data Inicial da Promoção(DD-MM-AAAA): ")
            ADataInicio = datetime.strptime(ADataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
            ADataFim = input("Digite a Nova Data Final da Promoção(DD-MM-AAAA): ")
            ADataFim = datetime.strptime(ADataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
            Nome = input("Digite o Nome da Promoção que você quer Alterar as informações: ")

            bd.AtualizarPromocoes(conbd,ANome,ADescricao,ADataInicio,ADataFim,Nome)
        elif opcao == '5':
            ANome = input("Digite o Novo Nome do Funcionário: ")
            ACargo = input("Digite o Novo Cargo do Funcionário: ")
            ADepartamento = input("Digite o Novo Departamento do Funcionário: ")
            Nome = input("Digite o Nome do Funcionário que você quer Alterar as informações: ")
            
            bd.AtualizarFuncionarios(conbd,ANome,ACargo,ADepartamento,Nome)
        elif opcao == '6':
            print("Voltar ao Menu Principal")
            break
        else:
            print("Opção inválida! Tente novamente.")
#ajustar Menu Abaixo:
def MenuListar():
    while True:
            print("Menu Listar")
            print("1. Listar Produtos")
            print("2. Listar Fornecedores")
            print("3. Listar Clientes")
            print("4. Listar Promoções")
            print("5. Listar Funcionários")
            print("6. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1': 
                bd.ListarProdutos(conbd)
            elif opcao == '2':
                bd.ListarFornecedores(conbd)
            elif opcao == '3':
                bd.ListarClientes(conbd)
            elif opcao == '4':
                bd.ListarPromocoes(conbd)
            elif opcao == '5':
                bd.ListarFuncionarios(conbd)
            elif opcao == '6':
                print("Voltar ao Menu Principal")
                break
            else:
                print("Opção inválida! Tente novamente.")

def MenuPedidos():
    while True:
        print("Menu Pedidos")
        print("1. Criar Pedido")
        print("2. Listar Pedidos")
        print("3. Excluir Pedido")
        print("4. Modificar Pedido")

        opcao = input("Escolha uma Opção: ")

        if opcao == '1':
            PCliente = input("Digite o Nome do Cliente: ")            
            print("Escolha algum dos Produtos da Lista")
            bd.ListarProdutos(conbd)
            PProduto = input("Digite o ID do Produto: ")
            PQuantidade = int(input("Digite a Quantidade do Produto: "))
            FuncPedido.precoproduto(conbd,PProduto,PQuantidade)
            print("Método de Pagamento")
            print("1. Cartão de Crédito")
            print("2. Cartão de Débito")
            print("3. Boleto Bancário")
            print("4. Pix")
            print("5. Dinheiro")
            print("6. Bitcoin")

            opcao2 = input("Selecione o Método de Pagamento: ")

            if opcao2 == 1:
                PMetodo = "Cartão de Crédito"
            elif opcao2 == 2:
                PMetodo = "Cartão de Débito"
            elif opcao2 == 3:
                PMetodo = "Boleto Bancário"
            elif opcao2 == 4:
                PMetodo = "Pix"
            elif opcao2 == 5:
                PMetodo = "Dinheiro"
            elif opcao2 == 6:
                PMetodo = "Bitcoin"
        
            
        
        print

MenuPedidos()
            
                

            

