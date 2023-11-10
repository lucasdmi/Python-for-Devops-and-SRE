#Vector exercise
#4) Encontre a maior nota da turma com notas: 7, 6, 9, 9, 8, 8, 10, 5, 6 e 7



vetor_nota = [7, 6, 9, 9, 8,8,10,6,7]

maior = vetor_nota[0]
indice_maior = 0


for i in range (0, 9, 1):
    valor = vetor_nota[i]
    if valor > maior:
        maior = valor
        indice_maior = i
       

print(f"O maior valor é: {maior}, Ele está na posicao {indice_maior} do vetor." )


