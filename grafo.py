class Grafo:

    def __init__(self, v, e = None):
        self.V = v
        self.E = e

        qtde = len(self.V)
        self.matriz_adjacencia = [] 
        
        for i in range(qtde):
           self.matriz_adjacencia.append([0] * qtde)
        
        if self.E != None:
            for i in self.E:
                a,b = i
                self.matriz_adjacencia[a-1][b-1] = 1
                self.matriz_adjacencia[b-1][a-1] = 1
        
    def __str__(self):
        r = ""

        for i in self.matriz_adjacencia:
            for j in i:
                r = r + str(j) + " "

            r = r + "\n"
        

        return r


g = Grafo(v = [1,2,3], e = [(1,2), (2,3), (3,1)])

print(g)
