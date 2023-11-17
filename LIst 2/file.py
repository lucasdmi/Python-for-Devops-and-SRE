
#escrita
f = open("ola.txt", "a")
f.write("Esse eh meu primeiro arquivo!" )
f.close()

#leitura
f = open("ola.txt", "r")
print(f.read())

#ou
with open('ola.txt', 'r') as f:
    print(f.read())