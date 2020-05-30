from regras_jogo.regras_abstratas import AbstractRegrasJogo
from regras_jogo.personagens import Personagens
from acoes import AcoesJogador
import random

class Labirinto(AbstractRegrasJogo):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tempo = 0
        self.mapa = []
        for _ in range(0, tamanho):
            linha = [0 for j in range(0, tamanho)]
            self.mapa.append(linha)
        # Posicionamento do jogador
        self.x = [0, random.randrange(1, tamanho-1)]
        self.mapa[self.x[0]][self.x[1]] = "x"
        # Posicionamento da saída
        self.s = [tamanho-1, random.randrange(1, tamanho-1)]
        self.mapa[self.s[0]][self.s[1]] = "s"
        # Definição do caminho solução
        i, j = 1, self.x[1]
        alternador = True
        while i != self.s[0]-1 or j != self.s[1]:
            self.mapa[i][j] = "e"
            if alternador:
                if i < self.s[0] - 1:
                    i = i + 1
                alternador = False
            else:
                if j < self.s[1]:
                    j = j + 1
                elif j > self.s[1]:
                    j = j - 1
                alternador = True
        self.mapa[i][j] = "e"
        # Definição dos caminhos extras
        for _ in range(0, tamanho*10):
            i = random.randrange(1, tamanho - 2)
            j = random.randrange(1, tamanho - 2)
            if self.mapa[i + 1][j] == "e" and self.mapa[i - 1][j] == 0 and self.mapa[i][j + 1] == 0 and self.mapa[i][j-1] == 0:
                self.mapa[i][j] = "e"
            elif self.mapa[i + 1][j] == 0 and self.mapa[i - 1][j] == "e" and self.mapa[i][j + 1] == 0 and self.mapa[i][j-1] == 0:
                self.mapa[i][j] = "e"    
            elif self.mapa[i + 1][j] == 0 and self.mapa[i - 1][j] == 0 and self.mapa[i][j + 1] == "e" and self.mapa[i][j-1] == 0:
                self.mapa[i][j] = "e"    
            elif self.mapa[i + 1][j] == 0 and self.mapa[i - 1][j] == 0 and self.mapa[i][j + 1] == 0 and self.mapa[i][j-1] == "e":
                self.mapa[i][j] = "e" 
            elif self.mapa[i + 1][j] == 0 and self.mapa[i - 1][j] == 0 and self.mapa[i][j + 1] == 0 and self.mapa[i][j-1] == 0:   
                self.mapa[i][j] = "e" 

    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        self.agente = personagem
        return self.agente
    
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        if self.x == self.s:
            self.terminarJogo()
            return True
        return False

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        if self.agente == id_agente:
            return self.mapa

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        if self.agente == id_agente:
            self.proximaAcao = acao
    
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
        if self.proximaAcao.parametros[0] == AcoesJogador.BAIXO:
            if self.mapa[self.x[0]+1][self.x[1]] == "e" or self.mapa[self.x[0]+1][self.x[1]] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[0] += 1
                self.mapa[self.x[0]][self.x[1]] = "x"
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.CIMA:
            if self.mapa[self.x[0]-1][self.x[1]] == "e" or self.mapa[self.x[0]-1][self.x[1]] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[0] -= 1
                self.mapa[self.x[0]][self.x[1]] = "x"
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.DIREITA:
            if self.mapa[self.x[0]][self.x[1]+1] == "e" or self.mapa[self.x[0]][self.x[1]+1] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[1] += 1
                self.mapa[self.x[0]][self.x[1]] = "x"
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.ESQUERDA:
            if self.mapa[self.x[0]][self.x[1]-1] == "e" or self.mapa[self.x[0]][self.x[1]-1] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[1] -= 1
                self.mapa[self.x[0]][self.x[1]] = "x"
            else:
                print("Jogada inválida.")
            
        self.tempo += diferencial_tempo
    
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """ 
        print(self.tempo)
    


def construir_jogo(*args,**kwargs):
    labirinto = Labirinto(kwargs.get("tamanho"))
    return labirinto