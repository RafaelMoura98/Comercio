#funções de cadastro
#integrar categorias do produto dentro da função e usar uma condicional para evitar que no momento
#de um novo cadastro seja criada uma nova categoria sem a vontade do usuário
import conexaobd
from datetime import datetime
from mysql.connector import Error
conbd = conexaobd.conexao()

def CadProdutos(conbd,Nome,Descricao,Preco,quantEstoque):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO produtos(Nome,Descricao,Preco) values(%s,%s,%s)"
    val = (Nome,Descricao,Preco)    
    mycursor.execute(sql,val)
    ID_Produto = mycursor.lastrowid 

    sql1 = "INSERT INTO estoque(ID_Produto,Quantidade)VALUES(%s,%s)"
    val1 = (ID_Produto,quantEstoque)
    mycursor.execute(sql1,val1)
    conbd.commit()
    print('Produto cadastrado com sucesso')
    mycursor.close()

def CadFornecedores(conbd,Nome,Contato,Endereco):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO fornecedores(Nome,Contato,Endereco) values(%s,%s,%s)"
    val = (Nome,Contato,Endereco)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Fornecedor cadastrado com sucesso')
    mycursor.close()

def CadClientes(conbd,Nome,Sobrenome,Endereco,Cidade,CodigoPostal):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO clientes(Nome,Sobrenome,Endereco,Cidade,CodigoPostal) values(%s,%s,%s,%s,%s)"
    val = (Nome,Sobrenome,Endereco,Cidade,CodigoPostal)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Cliente cadastrado com sucesso')
    mycursor.close()

def CadPromocoes(conbd,Nome,Descricao,DataInicio,DataFim):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO promocoes(Nome,Descricao,DataInicio,DataFim) values(%s,%s,%s,%s)"
    val = (Nome,Descricao,DataInicio,DataFim)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Promoção cadastrada com sucesso')
    mycursor.close()

def CadFuncionarios(conbd,Nome,Cargo,Departamento):
    
    mycursor= conbd.cursor()
    
    sql = "INSERT INTO funcionarios(Nome,Cargo,Departamento) values(%s,%s,%s)"
    val = (Nome,Cargo,Departamento)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('Funcionário cadastrado com sucesso')
    mycursor.close()

#funções de Exclusão

def DelProdutos(conbd,Nome):
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM produtos WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('O Produto ',Nome,' Foi Excluido do Banco de Dados')
    mycursor.close()
   
def DelFornecedores(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM fornecedores WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('O Fornecedor ',Nome,' Foi Excluido do Banco de Dados')
    mycursor.close()

def DelClientes(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM clientes WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('O Cliente ',Nome,' Foi Excluido do Banco de Dados')
    mycursor.close()

def DelPromocoes(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM promocoes WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('A Promoção ',Nome,' Foi Excluida do Banco de Dados')
    mycursor.close()

def DelFuncionarios(conbd,Nome):
    
    mycursor= conbd.cursor()
    
    sql = "DELETE FROM funcionarios WHERE Nome = %s"
    val = (Nome,)    
    
    mycursor.execute(sql,val)
    conbd.commit()
    
    print('O Funcionario ',Nome,' Foi Excluido do Banco de Dados')
    mycursor.close()

#Funções de Listagem

def ListarProdutos(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM produtos;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):    
        print(i)
    
    mycursor.close()

def ListarClientes(conbd):
    mycursor = conbd.cursor()

    sql = "SELECT * FROM clientes;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for l in (listagem):
        print(l)
        
    mycursor.close()

def ListarFornecedores(conbd):
    mycursor = conbd.cursor()

    sql = "SELECT * FROM fornecedores;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for l in (listagem):
        print(l)
    
    mycursor.close()

def ListarPromocoes(conbd):
    mycursor = conbd.cursor()

    sql = "SELECT * FROM promocoes;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for l in (listagem):
        print(l)
    
    mycursor.close()

def ListarFuncionarios(conbd):
    mycursor = conbd.cursor()

    sql = "SELECT * FROM funcionarios;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for l in (listagem):
        print(l)
    
    mycursor.close()

#Funções de Atualização

def AtualizarProdutos(conbd,novonome,novadescricao,novopreco,PNome):
    mycursor = conbd.cursor()
    
    sql = "UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s WHERE Nome = %s"
    val = (novonome,novadescricao,novopreco,PNome)

    mycursor.execute(sql,val)
    conbd.commit()
    print("Produto atualizado com sucesso")
    mycursor.close()

def AtualizarClientes(conbd,novonome,novosobrenome,novoendereco,novacidade,novocodpostal,CNome):
    mycursor = conbd.cursor()
    
    sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s , Cidade = %s, CodigoPostal = %s WHERE Nome = %s"
    val = (novonome,novosobrenome,novoendereco,novacidade,novocodpostal,CNome)

    mycursor.execute(sql,val)
    conbd.commit()
    print("Cliente atualizado com sucesso")
    mycursor.close()

def AtualizarFornecedores(conbd,novonome,novocontato,novoendereco,FNome):
    mycursor = conbd.cursor()
    
    sql = "UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE Nome = %s"
    val = (novonome,novocontato,novoendereco,FNome)

    mycursor.execute(sql,val)
    conbd.commit()
    print("Fornecedor atualizado com sucesso")
    mycursor.close()

def AtualizarPromocoes(conbd,novonome,descricao,novadataIN,novadataFI,PNome):
    mycursor = conbd.cursor()
    
    sql = "UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE Nome = %s"
    val = (novonome,descricao,novadataIN,novadataFI,PNome)

    mycursor.execute(sql,val)
    conbd.commit()
    print("Promoção atualizada com sucesso")
    mycursor.close()

def AtualizarFuncionarios(conbd,novonome,novocargo,novodepartamento,FUNome):
    mycursor = conbd.cursor()
    
    sql = "UPDATE funcionarios SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE Nome = %s"
    val = (novonome,novocargo,novodepartamento,FUNome)

    mycursor.execute(sql,val)
    conbd.commit()
    print("Funcionário atualizado com sucesso")
    mycursor.close()




 
   

    