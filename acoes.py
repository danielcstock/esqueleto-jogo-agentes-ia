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
    def direita(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.DIREITA, (p1,p2,p3,p4))

    @classmethod
    def esquerda(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.ESQUERDA, (p1,p2,p3,p4))

    @classmethod
    def cima(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.CIMA, (p1,p2,p3,p4))
        
    @classmethod
    def baixo(cls, p1,p2,p3,p4):
        return cls(AcoesJogador.BAIXO, (p1,p2,p3,p4))