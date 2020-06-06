from abc import ABC, abstractmethod
from agentes.tipos import TiposAgentes


class AgenteAbstrato(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    if args[0] == TiposAgentes.PREPOSTO_HUMANO:
        print("Utilize as setas do teclado numérico para mover o jogador.")
        print("Cima: 8\nBaixo: 2\nEsquerda: 4\nDireita: 6\n")
        from agentes.humano import AgentePrepostoESHumano
        return AgentePrepostoESHumano()
    elif args[0] == TiposAgentes.AUTO_BFS:
        from agentes.bfs import AgenteBFS
        return AgenteBFS()
    elif args[0] == TiposAgentes.AUTO_DFS:
        from agentes.dfs import AgenteDFS
        return AgenteDFS()
    elif args[0] == TiposAgentes.AUTO_DFS_LIMIT:
        from agentes.dfs_limitado import AgenteDFSLimitado
        return AgenteDFSLimitado()
    elif args[0] == TiposAgentes.AUTO_DFS_ITERA:
        from agentes.dfs_iterativo import AgenteDFSIterativo
        return AgenteDFSIterativo()