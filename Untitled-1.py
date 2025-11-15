
# LABERINTO CON BACKTRACKING
ENERGIA_INICIAL = 18
laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 99, 99, 99, 1, 99, 99, 99, 1],
    [1, 99, 1, 1, 1, 1, 1, 99, 1],
    [1, 99, 1, 99, 99, 99, 1, 99, 1],
    [1, 1, 1, 99, 1, 1, 1, 99, 1],
    [99, 99, 1, 99, 1, 99, 99, 99, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 99, 99, 99, 99, 99, 99, 99, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

N = len(laberinto)
INICIO = (0, 7)  
FIN    = (8, 0)  

# UTILIDADES
def dentro(i, j):
    return 0 <= i < N and 0 <= j < N

def imprimir_matriz(m):
    for fila in m:
        print(fila)

def imprimir_con_camino(lab, camino):
    ver = [fila[:] for fila in lab]

    for (i, j) in camino:
        if (i, j) not in (INICIO, FIN):
            ver[i][j] = '*'   # marca el camino

    si, sj = INICIO
    fi, fj = FIN
    ver[si][sj] = 'i'   
    ver[fi][fj] = 'F'  

    for fila in ver:
        print(fila)


MOVS = [(0, -1), (1, 0), (-1, 0), (0, 1)]


def backtracking(i, j, energia, visitado, camino):

    if (i, j) == FIN:
        return True, energia

    for di, dj in MOVS:
        ni, nj = i + di, j + dj

        if not dentro(ni, nj):
            continue
        if visitado[ni][nj]:
            continue
        if laberinto[ni][nj] == 99:
            continue  

        costo = laberinto[ni][nj]
        nueva_energia = energia

        
        if costo > 0:
            nueva_energia -= costo
        elif costo < 0:
            nueva_energia -= costo  

        
        if (ni, nj) in (INICIO, FIN):
            nueva_energia -= 1

        if nueva_energia < 0:
            continue

        visitado[ni][nj] = True
        camino.append((ni, nj))

        ok, energia_rest = backtracking(ni, nj, nueva_energia, visitado, camino)
        if ok:
            return True, energia_rest

        camino.pop()
        visitado[ni][nj] = False

    return False, energia

# PROGRAMA PRINCIPAL
def main():

    print("LABERINTO ORIGINAL:")
    imprimir_matriz(laberinto)

    energia = ENERGIA_INICIAL - 1  

    val_ini = laberinto[INICIO[0]][INICIO[1]]
    if val_ini > 0:
        energia -= val_ini
    elif val_ini < 0:
        energia -= val_ini  

    if energia < 0:
        print("\nNo hay energía suficiente para iniciar.")
        return

    visitado = [[False]*N for _ in range(N)]
    camino = [INICIO]
    visitado[INICIO[0]][INICIO[1]] = True

    exito, energia_final = backtracking(INICIO[0], INICIO[1], energia, visitado, camino)

    print("\nRESULTADO:")
    if exito:
        imprimir_con_camino(laberinto, camino)
        print(f"\n¡SALIDA ENCONTRADA! Energía restante: {energia_final}")
        print(f"Pasos: {len(camino)-1}")
    else:
        print("NO existe camino suficiente con la energía disponible.")

main()
