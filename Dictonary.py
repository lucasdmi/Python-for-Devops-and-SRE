notas = {'joao':8,
         'maria':7,
         'ze':5,
         'joao':5,
         'tito':7,
         'nina':8,
         'ju':6,
         'pri':6,
         'ma':9,
         'bia':9}
print(notas['maria'])
notas['maria']=7.5
print(notas['maria'])
print(notas)
notas['gustavo']=10
print(notas)


#test using for

for nome in notas:
    print(nome, notas[nome])

soma=0
for nome in notas:
  soma = soma + notas[nome]
media = soma/len(notas)
print(media)
