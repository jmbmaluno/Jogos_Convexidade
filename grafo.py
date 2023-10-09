class Grafo:

    def __init__(self, v = None, e = None):
        self.V = v
        self.E = e
        self.matriz_adjacencia = []
        
        if self.V != None:
            qtde = len(self.V)
            l = [0] * qtde
            for i in range(qtde):   
                self.matriz_adjacencia.append(l)
        
        if self.E != None:
            for i in self.E:
                print(i)
                a,b = i
                self.matriz_adjacencia[0][1] = 1
                print(self.matriz_adjacencia[0])

    def __str__(self):
        r = "  "
        
        for i in self.V:
            r = r + " " + str(i)
        
        r = r + "\n"

        
        for i in range(len(self.matriz_adjacencia)):
            
            r = r + str(self.V[i]) + " "

            for j in self.matriz_adjacencia[i]:
                r = r + " " + str(j)

            r = r + "\n"

        return r
        



g = Grafo(v = [1,2,3], e = [(1,2), (2,3), (3,1)])

print(g)
