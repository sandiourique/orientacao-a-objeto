from modules.produto import Produto

class Venda(Produto):
    
    
    """[classe Venda]

    Returns:
    [cod_cliente]: [int]
    [quantidade]: [int]
    [cod_colaborador]: [int]
    """

    cod_cliente = 0
    quantidade = 0
    cod_colaborador = 0
    
    def get_cod_cliente(self):
            return self.cod_cliente

    def get_quantidade(self):
        return self.quantidade

    def get_cod(self):
        return self.cod
    
    def get_cod_colaborador(self):
        return self.cod_colaborador
    
    def set_cod(self, cod):
        try:
            self.cod = cod
        except Exception as e:
            print("erro: ", str(e))

    def set_quantidade(self, i):
        try:
            self.cod = i
        except Exception as e:
            print("erro: ", str(e))

    def set_cod_cliente(self, cod):
        try:
            self.cod = cod
        except Exception as e:
            print("erro: ", str(e))
            
    def set_cod_colaborador(self, cod):
        try:
            self.cod = cod
        except Exception as e:
            print("erro: ", str(e))


    
    
