from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'
    AUTO_DFS_LIMIT = 'Automático DFS Limitado'
    AUTO_DFS_ITERA = 'Automático DFS Iterativo'
    AUTO_BUSCA_GULOSA = 'Automático Busca Gulos'
    AUTO_A_ESTRELA = 'Automático Busca A-estrela'

    
    # adicionar outros tipos de agentes de acordo com
    # o necessário