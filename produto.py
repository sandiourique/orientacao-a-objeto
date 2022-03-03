class Produto:
        
    """[classe tipo Produto]

    Returns:
    [cod]: [int]
    [nome]: [String]
    [estoque]: [int]
    """

    cod = 0
    nome = ""
    estoque = 0
    
    
    def get_cod(self):
        return self.cod
    def get_nome(self):
        return self.nome
    def get_estoque(self):
        return self.estoque 
    
    def set_cod(self, cod):
        self.cod = cod
    def set_nome(self, nome):
        self.nome = nome
    def set_estoque(self, estoque):
        self.estoque  = estoque
    
    def toList(self):
        return [self.cod, self.nome, self.estoque]
    

