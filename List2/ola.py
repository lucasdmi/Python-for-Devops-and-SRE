import sys
if len(sys.argv)<=1: #verifica se foi inserido algum argumento
    print("necessita argumento" )
else:
    print("ola", sys.argv) #pegar argumento inserido e printar na tela


tamanho = len(sys.argv)
for i in int(tamanho):
    print(sys.argv[i])