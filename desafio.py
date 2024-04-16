def distancia_edicao(a, b):

    operacoes = 0

    matriz = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    
    for i in range(len(a) + 1):
        matriz[i][0] = i
    for j in range(len(b) + 1):
        matriz[0][j] = j
        
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            
            if a[i - 1] == b[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
            
                matriz[i][j] = 1 + min(matriz[i - 1][j],       
                                        matriz[i][j - 1],       
                                        matriz[i - 1][j - 1])   

    
    palavra_resultante = ""
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            palavra_resultante = a[i - 1] + palavra_resultante
            i -= 1
            j -= 1
        elif matriz[i][j] == matriz[i - 1][j - 1] + 1:
            
            palavra_resultante = b[j - 1] + palavra_resultante
            i -= 1
            j -= 1
        elif matriz[i][j] == matriz[i - 1][j] + 1:

            i -= 1
        else:
            
            palavra_resultante = b[j - 1] + palavra_resultante
            j -= 1


    while j > 0:
        palavra_resultante = b[j - 1] + palavra_resultante
        j -= 1

    
    return palavra_resultante, matriz[len(a)][len(b)]

# Testando a função
a = "asar"
b = "casa"
palavra_resultante, custo = distancia_edicao(a, b)
print("Palavra resultante:", palavra_resultante)  # Saída: casa
print("Custo de edição:", custo)  # Saída: 2

a = "inserir"
b = "inserção"
palavra_resultante, custo = distancia_edicao(a, b)
print("Palavra resultante:", palavra_resultante)  # Saída: inserção
print("Custo de edição:", custo)  # Saída: 3







