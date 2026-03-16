
grafo = {
    'A': {'C': 14, 'B': 12},
    'B': {'A': 12, 'C': 9, 'D': 38},
    'C': {'A': 14, 'B': 9, 'D': 24, 'E': 7},
    'D': {'B': 38, 'C': 24, 'E': 13, 'G': 9},
    'E': {'C': 7, 'D': 13, 'F': 9, 'G': 29},
    'F': {'E': 9},
    'G': {'D': 9, 'E': 29}
}

# Heurística
heuristica = {
    'A': 30,
    'B': 26,
    'C': 21,
    'D': 7,
    'E': 22,
    'F': 36,
    'G': 0
}


def busca_gulosa(inicio, objetivo):

    abertos = [inicio] #Lista de nós que ainda podem ser explorados.
    caminho = [] # Lista para guardar o caminho percorrido.
    visitados = set() # quais já foram visitados

    while abertos:

        atual = min(abertos, key=lambda no: heuristica[no])
        abertos.remove(atual) # O nó escolhido sai da lista de candidatos.

        caminho.append(atual) # e vai para o de caminho percorrido
        visitados.add(atual)

        if atual == objetivo:
            return caminho

        for vizinho in grafo[atual]:
            if vizinho not in visitados and vizinho not in abertos: # Evita repetir nós.
                abertos.append(vizinho)

    return None


def busca_a_estrela(inicio, objetivo):

    abertos = [inicio]
    veio_de = {} #mapa de caminhos

    g = {no: float('inf') for no in grafo}
    g[inicio] = 0

    f = {no: float('inf') for no in grafo}
    f[inicio] = heuristica[inicio] 

    while abertos:

        atual = min(abertos, key=lambda no: f[no]) #Escolhe o nó com menor f(n).

        if atual == objetivo: 

            caminho = []
            while atual in veio_de: # quando encontra o objetivo ele vai voltando
                caminho.append(atual)
                atual = veio_de[atual]

            caminho.append(inicio)
            caminho.reverse() # depois inverte

            return caminho

        abertos.remove(atual)

        for vizinho, custo in grafo[atual].items(): # aqui pega o vizinho e ver o custo
            #custo até agora + custo da nova aresta
            g_temp = g[atual] + custo #calcula o g temporario

            if g_temp < g[vizinho]: # faz a verificação se encontrou o menor caminho que custa menos

                veio_de[vizinho] = atual
                g[vizinho] = g_temp
                f[vizinho] = g[vizinho] + heuristica[vizinho]

                if vizinho not in abertos:
                    abertos.append(vizinho)

    return None


print("Caminho busca gulosa:", busca_gulosa('A', 'G'))
print("Caminho A*:", busca_a_estrela('A', 'G'))