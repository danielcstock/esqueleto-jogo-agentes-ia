from regras_jogo.regras_abstratas import AbstractRegrasJogo
from regras_jogo.personagens import Personagens
from acoes import AcoesJogador
import random

class Labirinto(AbstractRegrasJogo):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tempo = 0
        self.mapa = []
        if tamanho == 6:
            self.mapa.append([0,0,0,0,'x',0])
            self.mapa.append([0,'e','e','e','e',0])
            self.mapa.append([0,'e',0,0,'e',0])
            self.mapa.append([0,0,'e','e','e',0])
            self.mapa.append([0,'e','e',0,'e',0])
            self.mapa.append([0,0,'s',0,0,0])
            self.x = [0, 4]
            self.s = [5, 2]
        else:
            self.tamanho = 20
            self.mapa.append([0,0,0,0,'x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
            self.mapa.append([0,'e','e','e','e','e',0,0,0,0,'e',0,0,0,'e','e','e',0,'e',0,])
            self.mapa.append([0,'e',0,0,0,'e',0,'e','e','e','e','e','e','e',0,0,'e','e','e',0,])
            self.mapa.append([0,'e','e',0,'e','e','e','e',0,0,'e',0,0,'e',0,0,'e',0,'e',0,])
            self.mapa.append([0,0,'e',0,0,0,0,'e',0,0,'e','e','e','e','e','e','e',0,'e',0,])
            self.mapa.append([0,0,'e','e','e','e',0,'e','e','e','e',0,0,0,'e',0,'e',0,'e',0,])
            self.mapa.append([0,'e',0,0,0,'e',0,0,'e',0,0,0,'e','e','e',0,'e','e','e',0,])
            self.mapa.append([0,'e','e','e','e','e',0,'e','e','e','e','e','e',0,'e',0,0,'e',0,0,])
            self.mapa.append([0,0,0,'e',0,0,0,0,0,'e',0,0,0,0,'e','e','e','e','e',0,])
            self.mapa.append([0,'e','e','e','e','e','e','e','e','e','e','e','e','e','e',0,0,0,'e',0,])
            self.mapa.append([0,'e',0,0,'e',0,0,0,'e',0,0,0,0,0,0,0,'e','e','e',0,])
            self.mapa.append([0,'e','e',0,'e',0,'e','e','e','e','e','e','e','e','e','e','e',0,0,0,])
            self.mapa.append([0,0,'e',0,'e',0,'e',0,0,0,0,0,'e',0,0,0,'e',0,0,0,])
            self.mapa.append([0,0,'e','e','e','e','e','e','e','e','e',0,'e',0,0,0,'e','e','e',0,])
            self.mapa.append([0,0,'e',0,0,0,0,0,'e',0,'e',0,'e','e','e',0,0,0,0,0,])
            self.mapa.append([0,0,'e','e','e','e','e',0,'e',0,'e','e',0,0,'e',0,0,0,0,0,])
            self.mapa.append([0,0,0,0,0,0,'e',0,'e',0,0,'e',0,0,'e','e','e','e',0,0,])
            self.mapa.append([0,0,0,'e','e','e','e','e','e',0,0,'e','e','e','e',0,0,'e',0,0,])
            self.mapa.append([0,'e','e','e',0,0,0,0,'e',0,'e','e',0,0,0,0,0,'e','e',0,])
            self.mapa.append([0,0,0,0,0,0,0,0,'s',0,0,0,0,0,0,0,0,0,0,0,])
            self.x = [0, 4]
            self.s = [19, 8]

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
                print("\n")
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.CIMA:
            if self.mapa[self.x[0]-1][self.x[1]] == "e" or self.mapa[self.x[0]-1][self.x[1]] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[0] -= 1
                self.mapa[self.x[0]][self.x[1]] = "x"
                print("\n")
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.DIREITA:
            if self.mapa[self.x[0]][self.x[1]+1] == "e" or self.mapa[self.x[0]][self.x[1]+1] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[1] += 1
                self.mapa[self.x[0]][self.x[1]] = "x"
                print("\n")
            else:
                print("Jogada inválida.")
        if self.proximaAcao.parametros[0] == AcoesJogador.ESQUERDA:
            if self.mapa[self.x[0]][self.x[1]-1] == "e" or self.mapa[self.x[0]][self.x[1]-1] == "s":
                self.mapa[self.x[0]][self.x[1]] = "e"
                self.x[1] -= 1
                self.mapa[self.x[0]][self.x[1]] = "x"
                print("\n")
            else:
                print("Jogada inválida.")
            
        self.tempo += diferencial_tempo
    
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """ 
        print("Fim. Total de {0} jogadas.".format(self.tempo))
    


def construir_jogo(*args,**kwargs):
    labirinto = Labirinto(kwargs.get("tamanho"))
    return labirinto