from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador

class AgenteBFS(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        pass
    
    def escolherProximaAcao(self):
        acao = AcaoJogador()
        return acao.cima()