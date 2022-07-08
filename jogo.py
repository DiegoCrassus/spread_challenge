from jogador import Jogador
from imovel import Imovel
from random import uniform, randint


class Jogo:
    
    def __init__(self, num_imoveis=36):
        self.imoveis = [Imovel(valor, ind + 1) 
                        for ind, valor in enumerate([round(uniform(5, 150), 2) 
                                                     for _ in range(0, num_imoveis)])]
        
        self.max_posicao = num_imoveis        
        self.jogador_impulsivo = Jogador(tipo=0, jogador="impulsivo")
        self.jogador_exigente = Jogador(tipo=1, jogador="exigente")
        self.jogador_cauteloso = Jogador(tipo=2, jogador="cauteloso")
        self.jogador_aleatorio = Jogador(tipo=3, jogador="aleatorio")
        
    def get_imovel(self, posicao):
        return self.imoveis[posicao - 1]
    
    def get_vencedor(self):
        if self.jogador_aleatorio.get_status():
            return True, self.jogador_aleatorio
        
        elif self.jogador_exigente.get_status():
            return True, self.jogador_exigente
        
        elif self.jogador_cauteloso.get_status():
            return True, self.jogador_cauteloso
        
        elif self.jogador_aleatorio.get_status():
            return True, self.jogador_aleatorio
        
        else:
            return False, None
        
    def set_vencedor(self):   
        if self.validar_jogador(self.jogador_aleatorio, 
                                self.jogador_cauteloso,
                                self.jogador_exigente,
                                self.jogador_impulsivo):
            
            self.jogador_aleatorio.set_status(True)
            
        elif self.validar_jogador(self.jogador_cauteloso, 
                                  self.jogador_aleatorio,
                                  self.jogador_exigente,
                                  self.jogador_impulsivo):
            
            self.jogador_cauteloso.set_status(True)
            
        elif self.validar_jogador(self.jogador_exigente, 
                                  self.jogador_aleatorio,
                                  self.jogador_cauteloso,
                                  self.jogador_impulsivo):
            
            self.jogador_exigente.set_status(True)
            
        elif self.validar_jogador(self.jogador_impulsivo, 
                                  self.jogador_aleatorio,
                                  self.jogador_cauteloso,
                                  self.jogador_exigente):
            
            self.jogador_impulsivo.set_status(True)
        
        
    def validar_jogador(self, jogador1, jogador2, jogador3, jogador4):
        if jogador1.get_status() != False \
            and jogador2.get_status() == False \
            and jogador3.get_status() == False \
            and jogador4.get_status() == False:

            return True
        else:
            return False

    def alugar(self, user: Jogador, imovel: Imovel):
        valor = imovel.get_aluguel()
        posicao = user.get_posicao()
        user.set_posicao(posicao, self.max_posicao)
        user.set_saldo(-valor)
        proprietario = imovel.get_proprietario()
        proprietario.set_saldo(valor)
    
    def comprar(self, user: Jogador, imovel: Imovel):
        imovel.set_tem_proprietario(True)
        imovel.set_proprietario(user)
        user.set_imoveis(imovel)
        user.set_saldo(-imovel.get_valor())

    def derrota(self, user: Jogador):
        user.set_status(False)
        [imovel.set_proprietario(False) for imovel in user.get_imoveis()]
        
    def vitoria(self, user: Jogador):
        if user.get_status():
            return True
        else:
            return False
        
    def jogar_dado(self):
        return randint(1, 6)
    
    def jogada(self, jogador: Jogador):
        dado = self.jogar_dado()
        jogador.set_posicao(dado, self.max_posicao)       
        imovel = self.get_imovel(jogador.get_posicao())
        
        if imovel.get_proprietario():
            self.alugar(jogador, imovel)
            
        else:
            if jogador.get_logica() == 0:
                self.comprar(jogador, imovel)

            elif jogador.get_logica() == 50 and imovel.get_valor() > 50:
                self.comprar(jogador, imovel)

            elif jogador.get_logica() == 50 and (jogador.get_saldo() - imovel.get_valor()) > 80:
                self.comprar(jogador, imovel)

            elif jogador.get_logica() == 0.5 and randint(0, 1) == 0:
                self.comprar(jogador, imovel)

        if jogador.get_saldo() < 0:
            self.derrota(jogador)                
        
        return self.vitoria(jogador)
    
    @staticmethod
    def print_jogada(jogador, imovel, tipo="Alugar"):
        print("Jogador: {}\tSaldo: {}\tAção: {}\nImovel: {} \
              \tAluguel: {}\tValor: {}\tDono: {}\n".format(jogador.jogador, 
                                                         round(jogador.get_saldo(), 2),
                                                         tipo,
                                                         imovel.get_posicao(),
                                                         round(imovel.get_aluguel(), 2),
                                                         round(imovel.get_valor(), 2),
                                                         imovel.get_proprietario()))
