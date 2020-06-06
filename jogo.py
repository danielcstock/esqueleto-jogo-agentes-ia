#!/usr/bin/env python3
import time
from labirinto.labirinto import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=True):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()

def iniciar_jogo():
    # Ler parâmetros do usuário
    print('Escolha um tamanho para o labirinto:\n6\n10\n15')
    tamanho = int(input())
    print('Escolha o tipo de agente:\n1 - Humano\n2 - DFS\n3 - BFS\n4 - DFS Limitado\n5 - DFS Iterativo\n6 - Busca Gulosa\n7 - Busca A*')
    agente = int(input())
    if agente == 1:
        agente = TiposAgentes.PREPOSTO_HUMANO
    elif agente == 2:
        agente = TiposAgentes.AUTO_DFS
    elif agente == 3:
        agente = TiposAgentes.AUTO_BFS
    elif agente == 4:
        agente = TiposAgentes.AUTO_DFS_LIMIT
    elif agente == 5:
        agente = TiposAgentes.AUTO_DFS_ITERA
    elif agente == 6:
        agente = TiposAgentes.AUTO_BUSCA_GULOSA
    else:
        agente = TiposAgentes.AUTO_A_ESTRELA
    # Inicializar e configurar jogo
    jogo = construir_jogo(tamanho = tamanho)
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    agente_jogador = construir_agente(agente, Personagens.O_JOGADOR)
    
    tempo_de_jogo = 0

    ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
    while not jogo.isFim():
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        tempo_corrente = ler_tempo()
        jogo.atualizarEstado(tempo_corrente)
        tempo_de_jogo += tempo_corrente

if __name__ == '__main__':
    iniciar_jogo()