grafo = {
    'Maceio':    {'Recife': 285, 'Arapiraca': 128},
    'Arapiraca': {'Maceio': 128, 'Recife': 270, 'Caruaru': 210},
    'Recife':    {'Maceio': 285, 'Arapiraca': 270, 'Caruaru': 130, 'Natal': 295},
    'Caruaru':   {'Arapiraca': 210, 'Recife': 130, 'Natal': 390, 'Campina': 185},
    'Natal':     {'Recife': 295, 'Caruaru': 390, 'Joao_Pessoa': 185, 'Campina': 170},
    'Joao_Pessoa':{'Natal': 185},
    'Campina':   {'Caruaru': 185, 'Natal': 170}
}

# Heurística: distância estimada até Campina Grande
heuristica = {
    'Maceio':     370,
    'Arapiraca':  310,
    'Recife':     130,
    'Caruaru':     70,
    'Natal':      170,
    'Joao_Pessoa':360,
    'Campina':      0
}

def busca_gulosa(inicio, objetivo):
    abertos = [inicio]
    caminho = []
    visitados = set()

    while abertos:
        atual = min(abertos, key=lambda no: heuristica[no])
        abertos.remove(atual)
        caminho.append(atual)
        visitados.add(atual)

        if atual == objetivo:
            return caminho

        for vizinho in grafo[atual]:
            if vizinho not in visitados and vizinho not in abertos:
                abertos.append(vizinho)

    return None

def busca_a_estrela(inicio, objetivo):
    abertos = [inicio]
    veio_de = {}

    g = {no: float('inf') for no in grafo}
    g[inicio] = 0

    f = {no: float('inf') for no in grafo}
    f[inicio] = heuristica[inicio]

    while abertos:
        atual = min(abertos, key=lambda no: f[no])

        if atual == objetivo:
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho

        abertos.remove(atual)

        for vizinho, custo in grafo[atual].items():
            g_temp = g[atual] + custo
            if g_temp < g[vizinho]:
                veio_de[vizinho] = atual
                g[vizinho] = g_temp
                f[vizinho] = g[vizinho] + heuristica[vizinho]
                if vizinho not in abertos:
                    abertos.append(vizinho)

    return None

print("Caminho busca gulosa:", busca_gulosa('Maceio', 'Campina'))
print("Caminho A*:",           busca_a_estrela('Maceio', 'Campina'))
