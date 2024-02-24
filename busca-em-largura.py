cidades = {
    'Ceilandia': ['Psul', 'Taguatinga'],
    'Psul': ['Sol Nascente'],
    'Taguatinga': ['Taguatinga Sul'],
    'Sol Nascente': [],
    'Taguatinga Sul': []
}

visitado = []  # lista para acompanhar os nós (nodes) visitados.
fila = []      # inicializa a fila

def bfs(visitado, cidades, node):
    visitado.append(node)
    fila.append(node)

    while fila:
        s = fila.pop(0)
        print(s)

        for vizinho in cidades[s]:
            if vizinho not in visitado:
                visitado.append(vizinho)
                fila.append(vizinho)

# busca em largura - breadth-first search
bfs(visitado, cidades, 'Ceilandia')

