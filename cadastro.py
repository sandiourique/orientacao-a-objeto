from modules.produto import Produto
from modules.venda import Venda
from modules.colaborador import Colaborador
from modules.cliente import Cliente
import __main__


"""
    Nesta classe faço todos os cadastros e atualização de estoque
c_produto = Lista  --> salva todas as listas de cadastro de produto
c_vendas = Lista --> salva todas as listas de cadastro de vendas
c_colaboradores = Lista --> salva todas as listas de cadastro de colaborador

"""

class Cadastro:
        
    c_produtos = [[101, 'Aipim', 50], [102, 'Alcool', 50], [103, 'Alcool em Gel', 50], [104, 'Arroz', 50], [105, 'Arroz Agulha', 50], [106, 'Arroz Carreteiro', 50], [107, 'Arroz Tipo 2', 50], [108, 'Batata', 50], [109, 'Batata doce', 50], [110, 'Biscoito', 50], [111, 'Bolacha', 50], [112, 'Cebola', 50], [113, 'Copo', 50], [114, 'Detergente', 50], [115, 'Esponja', 50], [116, 'Farinha', 50], [117, 'Feijao', 50], [118, 'Katchup', 50], [119, 'Macarrao', 50], [120, 'Maionese', 50], [121, 'Massa De Lasanha', 50], [122, 'Mostarda', 50], [124, 'Piment‹o Amarelo', 50], [125, 'Pimentao Verde', 50], [126, 'Pimentao Vermelho', 50], [127, 'Talher', 50], [128, 'Tomate', 50], [129, 'Brocolis', 50], [130, 'Rucula', 50], [131, 'Alface', 50], [132, 'Salsa', 50], [133, 'Alho', 50], [134, 'Alho poro', 50], [135, 'Tomilho', 50], [136, 'Cominho', 50], [137, 'Pimenta do Reino', 50], [138, 'Cebolinha verde', 50], [139, 'Curry', 50], [140, 'Cafe', 50]] 
 
    def cadastrar_produto():
        print("-------------------------------------------------")
        print("-------------Cadastro de Produtos----------------")
        print("-------------------------------------------------")
        
        cadastrando = int(input("Informe quantos produtos deseja cadastrar: "))
        cont = 0
        try:
            while cadastrando > cont:
                lista = []
                cadastro_prod = Produto()
                cadastro_prod.cod = int(input("Informe o código: "))
                cadastro_prod.nome = input("Nome do produto: ")
                cadastro_prod.estoque = int(input("Quantidade para ser cadastrada: "))
                lista.append(cadastro_prod.cod)
                lista.append(cadastro_prod.nome)
                lista.append(cadastro_prod.estoque)
                Cadastro.c_produtos.append(lista)
                cont += 1     
                print("Cadastro realizado com sucesso!")   
            for i in Cadastro.c_produtos:
                print("Código: ", i[0], "Nome: ", i[1], "Estoque: ", i[2])
        
        except Exception as e:
            print("O valor digitado não é um número válido")
            print("Escolha uma opção válida do menu.")
            __main__.menu() 


    c_vendas = []
    def cadastrar_venda():
        print("-------------------------------------------------")
        print("--------------Cadastro de Vendas-----------------")
        print("-------------------------------------------------")
        try:
            while True:
                vendas = input("Deseja cadastrar uma venda: S ou N ").upper()
                if vendas == 'S':
                    lista = []
                    cadastroV = Venda()
                    cadastroV.cod = int(input("Informe o código do produto: "))
                    cadastroV.quantidade = int(input("Quantidade da venda: "))
                    cadastroV.cod_cliente = int(input("Informe o código do cliente: "))
                    cadastroV.cod_colaborador = int(input("Informe o código do colaborador: "))
                    lista.append(cadastroV.cod)
                    lista.append(cadastroV.quantidade)
                    lista.append(cadastroV.cod_cliente)
                    lista.append(cadastroV.cod_colaborador)
                    Cadastro.c_vendas.append(lista)
                    Cadastro.atualizar_estoque(cadastroV.cod, cadastroV.quantidade)
                    print("-- Resumo -- ")
                    print(lista)
                elif vendas == 'N':
                    break
        
        except Exception as e:
            print("O valor digitado não é um número válido")
            print("Escolha uma opção válida do menu.")
            __main__.menu() 


    try:
        def atualizar_estoque(x, y):
            for i in Cadastro.c_produtos:
                if x == i[0]:
                    if i[2] >= y:
                        i[2] = i[2] - y
                    else:
                        print("Estoque insuficiente, apenas {} unidades: ".format(i[2]))
                else:
                    continue
                
    except Exception as e:
        print("O valor digitado não é um número válido")
        print("Escolha uma opção válida do menu.")
        __main__.menu()


    try:
        def consultar_estoque():
            for i in Cadastro.c_produtos:
                print("Código: ", i[0], "Produto: ", i[1], "Estoque: ", i[2])
                
    except Exception as e:
        print("O valor digitado não é um número válido")
        print("Escolha uma opção válida do menu.")
        __main__.menu() 


    c_clientes = [[1000,'Ana', 12345678978], [1001,'Alessadra',12345678979], [1002,'Antonia',12345678980], [1003,'Amatilde',12345678981], [1004,'Aline',12345678982], [1005, 'Anderson', 12345678983], [1006,'Amilton',12345678984], [1007,'Amadeu',12345678985], [1008, 'Antonio', 12345678986], [1009,'Bruno',12345678987], [1010,'Bernardo',12345678988], [1011,'Breno',12345678989], [1012,'Amanda',12345678990], [1013,'Andressa',12345678991], [1014,'Bruna',12345678992], [1015,'Bremilda',12345678993], [1018,'Camila',12345678996], [1024,'Danilo',12345679002], [1027,'Danubia',12345679005], [1030,'Edinei',12345679008], [1033,'Elena',12345679011], [1036,'Evaniza',12345679014], [1039,'Fernanda',12345679017], [1042,'Felipe',12345679020], [1045,'Francisco',12345679023], [1048,'Gael',12345679026]]  
 
    def cadastrar_cliente():
        print("-------------------------------------------------")
        print("-------------Cadastro de Clientes----------------")
        print("-------------------------------------------------")
        try:
            cadastrando = int(input("Informe quantos clientes deseja cadastrar: "))
            cont = 0
            while cadastrando > cont:
                lista = []
                cadastro_cliente = Cliente()
                cadastro_cliente.cod_cliente = int(input("Informe o código do cliente: "))
                cadastro_cliente.nome = input("Nome do cliente: ")
                cadastro_cliente.cpf = input("Informe o CPF: ")
                lista.append(cadastro_cliente.cod_cliente)
                lista.append(cadastro_cliente.nome)
                lista.append(cadastro_cliente.cpf)
                Cadastro.c_clientes.append(lista)
                cont += 1
                print("Cadastro realizado com sucesso!") 
            for i in Cadastro.c_clientes:
                print("Código: ", i[0], "Nome: ", i[1], "CPF: ", i[2])
        except Exception as e:
            print("O valor digitado não é um número válido")
            print("Escolha uma opção válida do menu.")
            __main__.menu() 
        
    c_colaboradores = [[10,'Ana', 'caixa'], [11,'Alessadra', 'caixa'], [12,'Antonia','caixa'], [13,'Amatilde', 'caixa'], [14,'Aline', 'caixa'], [15, 'Anderson', 'caixa'], [16,'Amilton', 'caixa'], [17,'Amadeu', 'caixa'], [18, 'Antonio', 'caixa'], [19,'Bruno', 'caixa'], [20,'Bernardo', 'caixa'], [21,'Breno', 'caixa'], [22,'Amanda', 'caixa'], [23,'Andressa','caixa'], [24,'Bruna', 'caixa'], [25,'Bremilda', 'caixa'], [26,'Camila', 'caixa'], [27,'Danilo','caixa'], [28,'Danubia', 'caixa'], [29,'Edinei','caixa'], [30,'Elena','caixa'], [31,'Evaniza', 'caixa'], [32,'Fernanda','caixa'], [33,'Felipe','caixa'], [34,'Francisco', 'caixa'], [35,'Gael', 'caixa']]   
    
    def cadastro_colaborador():
        print("-------------------------------------------------")
        print("------------Cadastro de Colaborador--------------")
        print("-------------------------------------------------")
        try:
            cadastrando = int(input("Informe quantos colaboradores deseja cadastrar: "))
            cont = 0
            while cadastrando > cont:
                lista = []
                cadastro_colaborador = Colaborador()
                cadastro_colaborador.cod_colaborador = int(input("Informe o código do colaborador: "))
                cadastro_colaborador.nome = input("Nome do colaborador: ")
                cadastro_colaborador.cargo = input("Informe o cargo: ")
                lista.append(cadastro_colaborador.cod_colaborador)
                lista.append(cadastro_colaborador.nome)
                lista.append(cadastro_colaborador.cargo)
                Cadastro.c_colaboradores.append(lista)
                cont += 1
                print("Cadastro realizado com sucesso!") 
            for i in Cadastro.c_colaboradores:
                print("Código: ", i[0], "Nome: ", i[1], "Cargo: ", i[2])
        except Exception as e:
            print("O valor digitado não é um número válido")
            print("Escolha uma opção válida do menu.")
            __main__.menu() 


