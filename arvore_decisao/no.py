class No():
    def __init__(self, *args, **kwargs):
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")
        self.visitado = False
        self.qtdLigacoes = 0
        self.ligacoes = list()
        self.nos = list()

    def getPosicao(self):
        return [self.x, self.y]

    def isVisitado(self):
        return self.visitado
    
    def setVisitado(self):
        self.visitado = True
