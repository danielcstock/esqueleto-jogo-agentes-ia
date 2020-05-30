from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, AcoesJogador

class AgenteBFS(AgenteAbstrato):
    
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
        
        acao = AcaoJogador("Humano", jogadas)
        return acao
            