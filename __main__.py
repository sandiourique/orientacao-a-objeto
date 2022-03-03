from modules.cadastro import Cadastro
       
def menu():
    print("-------------------------------------------------")
    print("------------MENU DE CADASTRO E VENDA-------------")
    print("-------------------------------------------------")
    print("Selecione uma das opções:")
    print("[0]-SAIR DO SISTEMA")
    print("[1]-CADASTRAR COLABORADOR")
    print("[2]-CADASTRAR CLIENTE")
    print("[3]-CADASTRAR PRODUTO")
    print("[4]-CONSULTA DE ESTOQUE")
    print("[5]-CADASTRAR VENDA")

    
    try: 
        opcao = int(input())
    except Exception as e:
        print("O valor digitado não é um número válido.")
        menu()

    if opcao == 1:
        Cadastro.cadastro_colaborador()
        menu()
    elif opcao == 2:
        Cadastro.cadastrar_cliente()
        menu()
    elif opcao ==3:
        Cadastro.cadastrar_produto()
        menu()
    elif opcao == 4:
        Cadastro.consultar_estoque()
        menu()
    elif opcao == 5:
        Cadastro.cadastrar_venda()
        menu()
    elif opcao == 0:
        exit()
    else:
        print("Opção Inválidação!")
        menu()

if __name__ == "__main__":
    
    
    menu()


#PARA ROTINA DE TESTES
# Todo os itens tem 50 em estoque, pode-se testar vender mais do que tem em estoque
# retorna uma mensagem de erro, dizendo o saldo.
# Sugestoes de venda
# [[101, 10, 1000, 10], [102, 20, 1002, 10], [103, 3, 1003, 10],
# [104, 8, 1004, 10], [105, 9, 1005, 10], [106, 45, 1006, 10],
# [107, 5, 1007, 10], [108, 50, 1008, 10], [109, 51, 1009, 10] ** vai mostrar o saldo em estoque,
# [110, 10, 1012, 10], [111, 11, 1015, 10], [112, 12, 1027, 10],
# [113, 13, 1045, 10], 14, 1018, 10], [115, 15, 1036, 10], 
# [116, 16, 1014, 10], [117, 17, 1013, 10], [118, 18, 1039, 10],
# [119, 19, 1024, 10], [120, 20, 1011, 10], [121, 30, 1042, 10]]

