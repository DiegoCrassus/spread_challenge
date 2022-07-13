import imp
from numpy import mean, argmax
from jogo import Jogo


def run_banco():
    
    banco_imobiliario = Jogo()
    num_rodadas = 0
    max_rodadas = 1000
    while num_rodadas != max_rodadas:
        status_jogador_aleatorio = banco_imobiliario.jogador_aleatorio.get_status()
        status_jogador_cauteloso = banco_imobiliario.jogador_cauteloso.get_status()
        status_jogador_exigente = banco_imobiliario.jogador_exigente.get_status()
        status_jogador_impulsivo = banco_imobiliario.jogador_impulsivo.get_status()

        if status_jogador_aleatorio == None:
            tem_vencedor = banco_imobiliario.jogada(banco_imobiliario.jogador_aleatorio)
            if tem_vencedor:
                banco_imobiliario.jogador_aleatorio.set_status(True)

        if status_jogador_cauteloso == None:
            tem_vencedor = banco_imobiliario.jogada(banco_imobiliario.jogador_cauteloso)
            if tem_vencedor:
                banco_imobiliario.jogador_cauteloso.set_status(True)

        if status_jogador_exigente == None:
            tem_vencedor = banco_imobiliario.jogada(banco_imobiliario.jogador_exigente)
            if tem_vencedor:
                banco_imobiliario.jogador_exigente.set_status(True)

        if status_jogador_impulsivo == None:
            tem_vencedor = banco_imobiliario.jogada(banco_imobiliario.jogador_impulsivo)
            if tem_vencedor:
                banco_imobiliario.jogador_impulsivo.set_status(True)

        banco_imobiliario.set_vencedor()
        vencedor, jogador = banco_imobiliario.get_vencedor()
        if vencedor:
            break

        num_rodadas += 1
        
    return num_rodadas, jogador

def get_vitorias(list_vencedor: list):
    aleatorio = 0
    cauteloso = 0
    exigente = 0
    impulsivo = 0
    len_vencedor = len(list_vencedor)

    for jogador in list_vencedor:
        if jogador:
            if jogador.jogador == "aleatorio":
                aleatorio += 1

            elif jogador.jogador == "cauteloso":
                cauteloso += 1

            elif jogador.jogador == "exigente":
                exigente += 1
                
            elif jogador.jogador == "impulsivo":
                impulsivo += 1
    res_arg_max = argmax([aleatorio / len_vencedor, cauteloso / len_vencedor, exigente / len_vencedor, impulsivo / len_vencedor])
    sucesso = ["aleatorio", "cauteloso", "exigente", "impulsivo"]

    return aleatorio / len_vencedor, cauteloso / len_vencedor, exigente / len_vencedor, impulsivo / len_vencedor, sucesso[res_arg_max]


if __name__ == "__main__":
    num_exec = 300
    list_rodadas = []
    list_vencedor = []

    for execucao in range(num_exec):
        rodada, vencedor = run_banco()
        list_rodadas.append(rodada)
        list_vencedor.append(vencedor)

    percent_aleatorio, percent_cauteloso, percent_exigente, percent_impulsivo, venceu_mais = get_vitorias(list_vencedor)

    print("Timeout turnos: {}".format(len([x for x in list_rodadas if x == 1000])))
    print("Média de turnos: {}".format(mean(list_rodadas)))
    print("Média de vitorias\nAleatorio: {}\nCauteloso: {}\nExigente: {}\nimpulsivo: {}".format(
        percent_aleatorio, percent_cauteloso, percent_exigente, percent_impulsivo
    ))
    print("Comportamento que mais vence: {}".format(venceu_mais))

