from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador, AcoesJogador
from arvore_decisao.no import No

class AgenteBFS(AgenteAbstrato):
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
                        no.proximo.append([i, j+1])
                    # casa da esquerda
                    if percepcao_mundo[i][j-1] == "e":
                        no.proximo.append([i, j-1])
                    # casa de cima
                    if percepcao_mundo[i-1][j] == "e":
                        no.proximo.append([i-1, j])
                    # casa de baixo
                    if percepcao_mundo[i+1][j] == "e":
                        no.proximo.append([i+1, j])
                    estados.append(no)
        has_solution = False
        solution_list = list()
        while not has_solution:
            indice_no = 0
            while len(estados) > indice_no:
                no = estados[indice_no]
                casas_disponiveis = 0
                temp_solution = list()
                # casa de baixo
                if no.x == jogador[0]+1 and no.y == jogador[1]:
                    casas_disponiveis += 1
                    temp_solution.append([[no.x, no.y], AcoesJogador.BAIXO])
                    jogador[0] = no.x
                    jogador[1] = no.y
                # casa de cima
                if no.x == jogador[0]-1 and no.y == jogador[1]:
                    casas_disponiveis += 1
                    temp_solution.append([[no.x, no.y], AcoesJogador.CIMA])
                    jogador[0] = no.x
                    jogador[1] = no.y
                # casa da esquerda
                if no.x == jogador[0] and no.y == jogador[1]-1:
                    casas_disponiveis += 1
                    temp_solution.append([[no.x, no.y], AcoesJogador.ESQUERDA])
                    jogador[0] = no.x
                    jogador[1] = no.y
                # casa da direita
                if no.x == jogador[0] and no.y == jogador[1]+1:
                    casas_disponiveis += 1
                    temp_solution.append([[no.x, no.y], AcoesJogador.DIREITA])
                    jogador[0] = no.x
                    jogador[1] = no.y
                indice_no += 1
                for _, acao in enumerate(temp_solution):
                    solution_list.append([acao])
                
                
                if all([s[0] - 1 == no.x, s[1] == no.y]):
                    has_solution = True    
        for acao in solution_list:
            print(acao)
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
        acao = AcaoJogador("Humano", self.jogadas.pop(0))
        return acao
            