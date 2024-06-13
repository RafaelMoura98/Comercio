import conexaobd
from datetime import datetime,date
from mysql.connector import Error
conbd = conexaobd.conexao()

#Funções do Pedido

#Puxar o preço do Pedido(verificar posteriormente)
def precoproduto(conbd,IDProduto,Quantidade):

    mycursor = conbd.cursor()
    sql = "SELECT Preco FROM produtos WHERE ID_Produto = %s"
    val = (IDProduto,)
    mycursor.execute(sql,val)
    #verificar linha abaixo.
    preco = mycursor.fetchone()[0]
    float(preco)
    ValorTotal = preco * Quantidade
    conbd.commit()
    print("Valor Total do Pedido ", ValorTotal)
    mycursor.close() 
#Puxar o Id do Cliente (OK)
def IDCliente(conbd,Nome):
    mycursor = conbd.cursor()
    sql = "SELECT ID_Cliente FROM clientes WHERE Nome = %s"
    val = (Nome,)
    mycursor.execute(sql,val)
    ID = mycursor.fetchone()[0]
    conbd.commit()
    print("O ID do cliente ",Nome," é: ",ID)
    mycursor.close()
#Puxar o Id do Produto (OK)
def IDProduto(conbd,Produto):
        mycursor = conbd.cursor()
        sql = "SELECT ID_Produto FROM produtos WHERE Nome = %s"
        val = (Produto,)
        mycursor.execute(sql,val)
        ID = mycursor.fetchone()[0]
        conbd.commit()
        print("O ID do Produto ",Produto," é: ",ID)
        mycursor.close()
#Subtrair do estoque
def SubEstoque(conbd,IDProduto,Quantidade,estoque):
    mycursor = conbd.cursor()
    int(Quantidade)  
    int(estoque)
    saida = estoque - Quantidade
    
    sql1 = "UPDATE estoque SET Quantidade = %s WHERE ID_Produto = %s"
    val1 = (saida,IDProduto)
    mycursor.execute(sql1,val1)
    
    conbd.commit()
    mycursor.close() 
#Puxar Id de venda e cadastrar pagamentos
def IDVendasPagamentos(conbd,Data,IDCliente,MetodoPagamento,Total):
    mycursor = conbd.cursor
    sql = "INSERT INTO vendas(Data,ID_Cliente,MetodoPagamento,Total) values(%s,%s,%s,%s)"
    val = (Data,IDCliente,MetodoPagamento,Total)
    mycursor.execute(sql,val)
    IDVenda = mycursor.lastrowid

    sql1 = "INSERT INTO pagamentos(ID_Venda,Data,Valor) values(%s,%s,%s)"
    val1 = (IDVenda,Data,Total)
    mycursor.execute(sql1,val1)
    conbd.commit()
    mycursor.close()
#Puxar estoque atual (OK)
def estoqueatual(conbd,Produto):
    mycursor = conbd.cursor()
    sql = "SELECT Quantidade FROM estoque WHERE ID_Produto = %s"
    val = (Produto,)
    mycursor.execute(sql,val)
    Estoque = mycursor.fetchone()[0]
    conbd.commit()
    print("A Quantidade em estoque do item ",Produto," é: ",Estoque)
    mycursor.close()    

def cadastrarpedido(conbd,IDCliente,Total,IDProduto,Quantidade,MetodoPagamento):
    mycursor = conbd.cursor
    Data = date.today()
    
           
