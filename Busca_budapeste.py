
grafo = {
    'Arad': {'Zerind', 'Sibiu', 'Timisoara'},
    'Zerind': {'Oradea', 'Arad'},
    'Oradea': {'Zerind', 'Sibiu'},
    'Sibiu': {'Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'},
    'Timisoara': {'Arad', 'Lugoj'},
    'Lugoj': {'Timisoara', 'Mehadia'},
    'Mehadia': {'Lugoj', 'Drobeta'},
    'Drobeta': {'Mehadia', 'Craiova'},
    'Craiova': {'Drobeta', 'Rimnicu Vilcea', 'Pitesti'},
    'Rimnicu Vilcea': {'Sibiu', 'Craiova', 'Pitesti'},
    'Fagaras': {'Sibiu', 'Bucharest'},
    'Pitesti': {'Rimnicu Vilcea', 'Craiova', 'Bucharest'},
    'Bucharest': {'Fagaras', 'Pitesti'}
}

from queue import Queue

def busca_em_largura(grafo, inicio, objetivo):
    fila = Queue()
    fila.put(inicio)
    
    visitados = {}
    veio_de = {}
    
    visitados[inicio] = True
    veio_de[inicio] = None
    
    while not fila.empty():
        atual = fila.get()
        
        if atual == objetivo:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.reverse()
            return caminho
        
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados[vizinho] = True
                veio_de[vizinho] = atual
                fila.put(vizinho)
    
    return None


# Exemplo de uso
inicio = 'Arad'
objetivo = 'Bucharest'

caminho = busca_em_largura(grafo, inicio, objetivo)

if caminho:
    print("Caminho mais curto de", inicio, "até", objetivo, ":", caminho)
else:
    print("Nenhum caminho encontrado de", inicio, "até", objetivo)
