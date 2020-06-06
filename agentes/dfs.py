from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, AcoesJogador
from arvore_decisao.no import No
import time

class AgenteDFS(AgenteAbstrato):
    def __init__(self):
        self.arvore = list()
        self.jogadas = list()

    def popularGrafo(self, percepcao_mundo):
        x = 0
        y = 0
        self.grafo = list()
        for i, espaco in enumerate(percepcao_mundo[0]):
            if espaco == "x":
                y = i
        no_jogador = No(x = x, y = y)
        no_jogador.qtdLigacoes += 1
        no_jogador.ligacoes.append([x+1, y])
        self.grafo.append(no_jogador)
        for i, linha in enumerate(percepcao_mundo):
            for j, espaco in enumerate(linha):
                if espaco == "e":
                    no = No(x = i, y = j)
                    # casa da direita
                    if percepcao_mundo[i][j+1] == "e" or percepcao_mundo[i][j+1] == "s":
                        no.ligacoes.append([i, j+1])
                        no.qtdLigacoes += 1
                    # casa da esquerda
                    if percepcao_mundo[i][j-1] == "e" or percepcao_mundo[i][j-1] == "s":
                        no.ligacoes.append([i, j-1])
                        no.qtdLigacoes += 1
                    # casa de cima
                    if percepcao_mundo[i-1][j] == "e" or percepcao_mundo[i-1][j] == "s":
                        no.ligacoes.append([i-1, j])
                        no.qtdLigacoes += 1
                    # casa de baixo
                    if percepcao_mundo[i+1][j] == "e" or percepcao_mundo[i+1][j] == "s":
                        no.ligacoes.append([i+1, j])
                        no.qtdLigacoes += 1
                    if no.qtdLigacoes > 0:
                        self.grafo.append(no)
        for no in self.grafo:
            for no_atual in self.grafo:
                if no_atual.getPosicao() in no.ligacoes:
                    no.nos.append(no_atual)

    def definirSolucao(self, lista_solucoes, s):
        for solucao in lista_solucoes:
            if s in solucao:
                self.solucao = solucao
        jogador = self.solucao[0]
        for caminho in self.solucao:
            if caminho[0] > jogador[0] and caminho[1] == jogador[1]:
                self.jogadas.append(AcoesJogador.BAIXO)
            elif caminho[0] < jogador[0] and caminho[1] == jogador[1]:
                self.jogadas.append(AcoesJogador.CIMA)
            elif caminho[0] == jogador[0] and caminho[1] > jogador[1]:
                self.jogadas.append(AcoesJogador.DIREITA)
            elif caminho[0] == jogador[0] and caminho[1] < jogador[1]:
                self.jogadas.append(AcoesJogador.ESQUERDA)
            jogador = caminho

    def tracarTrajeto(self, percepcao_mundo):
        x = 0
        y = 0
        s_x = 0
        s_y = 0
        for i, espaco in enumerate(percepcao_mundo[0]):
            if espaco == "x":
                y = i
        for i, linha in enumerate(percepcao_mundo):
            for j, espaco in enumerate(linha):
                if espaco == "s":
                    s_y = j
            s_x = i
        s = [s_x, s_y]
        no_jogador = No(x = x, y = y)
        no_jogador.qtdLigacoes += 1
        no_jogador.ligacoes.append([x+1, y])
        self.popularGrafo(percepcao_mundo)
        lista_solucoes = [list()]
        lista_solucoes[0].append(self.grafo[0].getPosicao())
        no = self.grafo[0]
        bifurcacoes = [no]
        has_solution = False
        no_anterior = list()
        no_anterior.append(self.grafo[0])
        while not has_solution:
            if s in no.ligacoes:
                while no.ligacoes[0] != s:
                    no.ligacoes.pop(0)
                lista_solucoes[-1].append(no.ligacoes[0])
                has_solution = True
            elif no.qtdLigacoes == 0:
                no = bifurcacoes.pop()
                lista_solucoes.pop()
            elif no.qtdLigacoes == 0:
                no = no_anterior.pop()
                no.nos.pop(0)

            elif no.qtdLigacoes == 1:
                if no.ligacoes[0] != no.getPosicao() and no.ligacoes[0] not in lista_solucoes[-1]:
                    lista_solucoes[-1].append(no.ligacoes[0])
                    no_anterior.append(no)
                    no = no.nos[0]
                    if no_anterior[-1] != self.grafo[0] and no_anterior[-1] in no.nos:
                        no.nos.remove(no_anterior[-1])
                        no.ligacoes.remove(no_anterior[-1].getPosicao())
                        no.qtdLigacoes -= 1
                else:
                    no = no_anterior.pop()
            elif no.qtdLigacoes > 1:
                lista_solucoes.append(list())
                for p in lista_solucoes[-2]:
                    lista_solucoes[-1].append(p)
                bifurcacoes.append(no)
                lista_solucoes[-1].append(no.ligacoes[0])
                no.qtdLigacoes -= 1
                no.ligacoes.remove(lista_solucoes[-1][-1])
                no_anterior.append(no)
                no = no.nos[0]
                no.nos.remove(no_anterior[-1])
                no.ligacoes.remove(no_anterior[-1].getPosicao())
                no.qtdLigacoes -= 1
                no_anterior[-1].nos.pop(0)
                
        self.definirSolucao(lista_solucoes, s)
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        if len(self.jogadas) == 0:
            self.tracarTrajeto(percepcao_mundo)

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
        time.sleep(1)
        temp_acao = self.jogadas.pop(0)
        jogadas = []
        if temp_acao == AcoesJogador.CIMA:
            jogadas.append(AcoesJogador.CIMA)
        elif temp_acao == AcoesJogador.ESQUERDA:
                jogadas.append(AcoesJogador.ESQUERDA)
        elif temp_acao == AcoesJogador.DIREITA:
                jogadas.append(AcoesJogador.DIREITA)
        elif temp_acao == AcoesJogador.BAIXO:
                jogadas.append(AcoesJogador.BAIXO)
        
        acao = AcaoJogador("DFS", jogadas)
        return acao
            