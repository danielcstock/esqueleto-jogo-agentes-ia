from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, AcoesJogador
from arvore_decisao.no import No

class AgenteDFS(AgenteAbstrato):
    def __init__(self):
        self.arvore = list()
        self.jogadas = list()

    def avaliarNos(self, inicio, solucao, estados):
        self.arvore.append(inicio)
        # for elemento in estados:
            

    def tracarTrajeto(self, percepcao_mundo):
        x = 0
        y = 0
        s_x = 0
        s_y = 0
        estados = list()
        for i, espaco in enumerate(percepcao_mundo[0]):
            if espaco == "x":
                y = i
        for i, linha in enumerate(percepcao_mundo):
            for j, espaco in enumerate(linha):
                if espaco == "s":
                    s_y = j
            s_x = i
        s = [s_x, s_y]
        jogador = [x, y]
        for i, linha in enumerate(percepcao_mundo):
            for j, espaco in enumerate(linha):
                if espaco == "e":
                    no = No(x = i, y = j)
                    # casa da direita
                    if percepcao_mundo[i][j+1] == "e":
                        no.ligacoes.append([i, j+1])
                        no.qtdLigacoes += 1
                    # casa da esquerda
                    if percepcao_mundo[i][j-1] == "e":
                        no.ligacoes.append([i, j-1])
                        no.qtdLigacoes += 1
                    # casa de cima
                    if percepcao_mundo[i-1][j] == "e":
                        no.ligacoes.append([i-1, j])
                        no.qtdLigacoes += 1
                    # casa de baixo
                    if percepcao_mundo[i+1][j] == "e":
                        no.ligacoes.append([i+1, j])
                        no.qtdLigacoes += 1
                    estados.append(no)
           
        for no in estados:
            print(no.getPosicao())
        return 
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
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
        acao = AcaoJogador("DFS", self.jogadas.pop(0))
        return acao
            