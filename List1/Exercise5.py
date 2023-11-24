#Elabore um algoritmo que simule o “lápis tabuada”: o usuário informa um número inteiro qualquer, calcule e exiba os resultados das multiplicações entre 1 e 10.



def calculadora(numero_inteiro):
    for i in range (1, 11, 1):
        resultado = numero_inteiro * i
        print(f'{numero_inteiro} x {i}. O resultado é {resultado}')
        
numero_inteiro = int(input('Digite um valor inteiro qualquer:'))
lapis_tabuada = calculadora(numero_inteiro)