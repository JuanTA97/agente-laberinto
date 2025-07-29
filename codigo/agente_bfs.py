from collections import deque
from laberinto import crear_laberinto, visualizar_laberinto

def bfs(laberinto, inicio, fin):
    filas, columnas = laberinto.shape
    visitado = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        x, y = camino[-1]

        if (x, y) == fin:
            return camino

        if (x, y) in visitado:
            continue

        visitado.add((x, y))

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx, ny] == 0:
                nuevo_camino = list(camino)
                nuevo_camino.append((nx, ny))
                cola.append(nuevo_camino)

    return None

if __name__ == "__main__":
    laberinto = crear_laberinto()
    inicio = (0, 0)
    fin = (4, 4)
    
    camino = bfs(laberinto, inicio, fin)
    if camino:
        print("Camino encontrado:", camino)
        visualizar_laberinto(laberinto, camino)
    else:
        print("No hay camino posible.")
