class Cliente():
    """Classe do tipo Cliente

    Atributes:
        cod_cliente: int
        nome: String
        CPF = String
    """
       
    cod_cliente = 0
    nome = ""
    cpf = ""

    def get_cod_cliente(self):
        return self.cod_cliente
 
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf
            
    def set_cod_cliente(self, i):
        try:
            self.cod_cliente = i
        except Exception as e:
            print("erro: ", str(e))

    def set_nome(self, i):
        try:
            self.nome = i
        except Exception as e:
            print("erro: ", str(e))
  
    def set_cpf(self, i):
        try:
            self.cpf = i
        except Exception as e:
            print("erro: ", str(e))
    


