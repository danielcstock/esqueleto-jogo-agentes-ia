from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    DIREITA = "DIREITA",
    ESQUERDA = "ESQUERDA",
    CIMA = "CIMA",
    BAIXO = "BAIXO"

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def nome_de_uma_acao_valida_no_seu_jogo(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.DIREITA, (p1,p2,p3,p4))