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
    def direita(cls):
        print("direita")
        return cls(AcoesJogador.DIREITA)

    @classmethod
    def esquerda(cls):
        return cls(AcoesJogador.ESQUERDA)

    @classmethod
    def cima(cls):
        return cls(AcoesJogador.CIMA)
        
    @classmethod
    def baixo(cls):
        return cls(AcoesJogador.BAIXO)