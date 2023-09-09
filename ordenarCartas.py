
def ordenar_cartas(entrada):
    saida = [float('inf')]
    while len(entrada) > 0:
        carta_atual = entrada.pop(0)
        for i in range(len(saida)):
            if carta_atual < saida[i]:
                saida.insert(i, carta_atual)
                break
    saida.pop(0)
    return saida
def ordenar_cartas(entrada):
    resultado = sorted(entrada)
    return resultado
entrada = [1,15,13,2,5,13,43,64,24,14]
resultado = ordenar_cartas(entrada)
print(', '.join(map(str, resultado))) # 1, 2, 5, 13, 13, 14, 15, 24, 43, 64 

