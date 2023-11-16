#Espere... você lembra como se calcula um fatorial? Vamos voltar no tempo, na época do seu ensino fundamental, 
#quando o professor de matemática lhe pedia para calcular isso: 5! Calcular o fatorial de 5 significa multiplica-lo por todos os números menor que ele, até o número 1. 
#Sendo assim: 5! = 5 x 4 x 3 x 2 x 1 5! = 20 x 3 x 2 x 1 5! = 60 x 2 x 1 5! = 120 x 1 5! = 120 Lembrou?

#Elabore um algoritmo que simule o “lápis tabuada”: o usuário informa um número inteiro qualquer, calcule e exiba os resultados das multiplicações entre 1 e 10.



def calculadora_fatorial(numero_inteiro):
    if numero_inteiro <= 1:
        return 1
    else:
        n = numero_inteiro
        resultado = 1
        for i in range (0, n, 1):
            resultado = resultado * (n - i)
        return resultado
    

numero_inteiro = int(input('Digite um valor inteiro qualquer:'))   
fatorial = calculadora_fatorial(numero_inteiro)
print(f'O numero fatorial é:{fatorial}')