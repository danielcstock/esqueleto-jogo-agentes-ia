from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, AcoesJogador

class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        for linha in percepcao_mundo:
            str_linha = ""
            for espaco in linha:
                if espaco == 0:
                    str_linha +=  "#"
                elif espaco == "x":
                    str_linha += "x"
                else:
                    str_linha += " "
            print(str_linha)
    
    def escolherProximaAcao(self):
        jogadas = []
        turno = True
        while turno:
            tecla = input()
            if tecla == "8":
                jogadas.append(AcoesJogador.CIMA)
                turno = False
            elif tecla == "4":
                jogadas.append(AcoesJogador.ESQUERDA)
                turno = False
            elif tecla == "6":
                jogadas.append(AcoesJogador.DIREITA)
                turno = False
            elif tecla == "2":
                jogadas.append(AcoesJogador.BAIXO)
                turno = False
        acao = AcaoJogador("Humano", jogadas)
        return acao
            