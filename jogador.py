class Jogador:
    def __init__(self, tipo=0, jogador=None):
        """
            tipo: tipo de jogador.
            Ex:
                Tipo 0: impulsivo - logica = 0
                Tipo 1: exigente - logica = 50
                Tipo 2: cauteloso - logica = 80
                Tipo 3: aleatório - logica = 0.5
            
            posicao: posição no tabuleiro
            saldo: saldo do jogador
            status: False para se perdeu, True para se ganhou e None se permance jogando.
            imoveis: lista de imveis
            logica: regra do jogador
        """
        self.jogador = jogador
        self.posicao = 0
        self.tipo = tipo
        self.saldo = 300
        self.status = None
        self.imoveis = []
        self.logica = Jogador.regra(self.tipo)
        
    def get_saldo(self):
        return self.saldo
    
    def get_status(self):
        return self.status
    
    def get_tipo(self):
        return self.tipo
    
    def get_logica(self):
        return self.logica
    
    def get_imoveis(self):
        return self.imoveis
    
    def get_posicao(self):
        return self.posicao
    
    def set_posicao(self, posicao, max_posicao):
        self.posicao += posicao
        if self.posicao > max_posicao:
            self.posicao -= max_posicao
    
    def set_imoveis(self, imovel):
        self.imoveis.append(imovel)
    
    def set_saldo(self, valor):
        if not self.status:
            self.saldo += valor
            
    def set_status(self, status):
        self.status = status
            
    @staticmethod
    def regra(tipo):
        if tipo == 0:
            return 0
        
        elif tipo == 1:
            return 50
            
        elif tipo == 2:
            return 80
            
        elif tipo == 3:
            return 0.5
            
        else:
            raise ValueError("Tipo invalido!")
    
    def __repr__(self):
        return "{}".format(self.jogador)
