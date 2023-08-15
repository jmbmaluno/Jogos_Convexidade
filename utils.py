def trocar(conjunto,i,j):
    aux = conjunto[i]
    conjunto[i] = conjunto[j]
    conjunto[j] = aux


def particionar(conjunto, i, j):
    pivot = conjunto[j]

    k = i - 1

    for l in range(i, j):
        if(conjunto[l] <= pivot):
            k = k + 1
            trocar(conjunto, l, k)
    
    k = k + 1
    trocar(conjunto,j,k)

    return k

def quicksort(conjunto, i, j):
    if i < j:
        p = particionar(conjunto,i,j)
        quicksort(conjunto, i, p-1)
        quicksort(conjunto, p+1, j)



def mex(conjunto):
    quicksort(conjunto, 0, len(conjunto)-1)

    
    j = conjunto[0]

    for i in range(1, len(conjunto)):
        if(conjunto[i] != j and conjunto[i]!= j+1):
            return j+1
        
        j = conjunto[i]
    
    return conjunto[len(conjunto)-1] + 1

    '''
    Outra forma

        x = 0

        for n in conjunto:
            if n == x:
                x += 1
            elif n > x:
                break
        
        return x
    '''
    
