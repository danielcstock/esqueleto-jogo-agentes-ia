from agentes.abstrato import AgenteAbstrato
from agentes.dfs import AgenteDFS
from acoes import AcaoJogador, AcoesJogador
from arvore_decisao.no import No
import time

class AgenteDFSLimitado(AgenteDFS):
    def tracarTrajeto(self, percepcao_mundo):
        limite = int(len(percepcao_mundo)**2/2)
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
            if limite >= len(lista_solucoes):
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
            else:
                lista_solucoes.pop()      
        self.definirSolucao(lista_solucoes, s)
    
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
        
        acao = AcaoJogador("DFS Limitado", jogadas)
        return acao
            