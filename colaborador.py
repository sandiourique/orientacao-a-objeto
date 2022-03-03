class Colaborador():

    """Classe do tipo Colaborador

    Atributes:
    cod_colaborador = Int
    nome = String
    cargo = String
    """

    cod_colaborador = "" 
    nome = ""
    cargo = ""


    def get_cod_colaborador(self):
        return self.cod_colaborador

    def get_nome(self):
        return self.nome

    def get_cargo(self):
        return self.cargo

                
    def set_cod_colaborador(self, i):
        try:
            self.cod_colaborador = i
        except Exception as e:
            print("erro: ", str(e))

    def set_nome(self, i):
        try:
            self.nome = i
        except Exception as e:
            print("erro: ", str(e))


    def set_cargo(self, i):
        try:
            self.cargo = i
        except Exception as e:
            print("erro: ", str(e))
            

            

