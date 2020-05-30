from regras_jogo.regras_abstratas import AbstractRegrasJogo
from regras_jogo.personagens import Personagens
import random

class Labirinto(AbstractRegrasJogo):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.mapa = []
        for _ in range(0, tamanho):
            linha = [0 for j in range(0, tamanho)]
            self.mapa.append(linha)
        # Posicionamento do jogador
        x = [0, random.randrange(1, tamanho-1)]
        self.mapa[x[0]][x[1]] = "x"
        # Posicionamento da saída
        s = [tamanho-1, random.randrange(1, tamanho-1)]
        self.mapa[s[0]][s[1]] = "s"
        # Definição do caminho solução
        i, j = 1, x[1]
        while i != s[0]-1 or j != s[1]:
            self.mapa[i][j] = "e"
            if i < s[0] - 1:
                i = i + 1
            elif j < s[1]:
                j = j + 1
            elif j > s[1]:
                j = j - 1
        self.mapa[i][j] = "e"
        # Definição dos caminhos extras
        for linha in self.mapa:
            print(linha)

    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return Personagens.O_JOGADOR
    
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return False

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return 1

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        return 1
    
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        return 1
    
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """ 
        return 1
    


def construir_jogo(*args,**kwargs):
    labirinto = Labirinto(kwargs.get("tamanho"))
    # labirinto.registrarAgentePersonagem(kwargs.get("jogador"))
    return labirinto