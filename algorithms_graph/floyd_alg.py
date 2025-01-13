import math

def get_path(P, start, end):
    path = [start]
    next_v = start
    while next_v != end:
        next_v = P[next_v][end]
        if next_v is None or next_v == path[-1]:
            return [] # Путь не существует
        path.append(next_v)
    
    return path

V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
]

N = len(V) # Число вершин в графе
P = [[v for v in range(N)] for u in range(N)] # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = P[i][k] # номер промежуточной вершины при движении от i к j

start = 0
end = 7
path = get_path(P, start, end)
print("Кратчайший путь от", start, "до", end, ":", path if path else "Нет пути")