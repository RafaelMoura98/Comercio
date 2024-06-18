import conexaobd
import FuncPedido
import bd
conbd = conexaobd.conexao()

IDproduto = input("Digite o Id do Produto: ")
Quantidade = input("Digite a Quantidade: ")

FuncPedido.precoproduto(conbd,IDproduto,Quantidade)
FuncPedido.SubEstoque(conbd)
FuncPedido.estoqueatual(conbd,IDproduto)

