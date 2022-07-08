class Imovel:
    def __init__(self, valor, posicao):
        """
            posicao: posição no tabuleiro
            valor: valor do imovel
            aluguel: valor do aluguel do imovel, 20% do valor do imovel arrendodado para duas casas decimais
            proprietario: se há um proprietario ou não.
        """
        self.posicao = posicao
        self.valor = valor
        self.aluguel = round(0.2 * self.valor, 2)
        self.tem_proprietario = False
        self.proprietario = False
        
    def get_posicao(self):
        return self.posicao
    
    def get_valor(self):
        return self.valor
    
    def get_aluguel(self):
        return self.aluguel
    
    def get_tem_proprietario(self):
        return self.tem_proprietario
    
    def get_proprietario(self):
        return self.proprietario
    
    def set_valor(self, valor):
        self.valor = valor
        
    def set_aluguel(self, valor):
        self.aluguel = round(0.2 * valor, 2)
        
    def set_tem_proprietario(self, tem_proprietario):
        self.tem_proprietario = tem_proprietario
        
    def set_proprietario(self, proprietario):
        self.proprietario = proprietario
        
    def __repr__(self):
        return "pos: {}\nvalor: {}\nAluguel: {}\nTem dono: {}".format(self.posicao, self.valor, self.aluguel, self.proprietario)