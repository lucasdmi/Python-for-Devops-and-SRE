


def valida(nota):
    try:
        if nota > 10 or nota < 1:
            raise ValueError("Nota invalida")
        else:
            return nota
    except ValueError:
        print("A nota digitada é invalida, digite novamente.")
        return valida(float(input("Digite a nota novamente: ")))

def inserir_dados_alunos(quantidade_alunos):
    for i in range(quantidade_alunos):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota1 = valida(float(input(f"Digite a primeira nota do aluno {i + 1}: ")))
        nota2 = valida(float(input(f"Digite a segunda nota do aluno {i + 1}: ")))
        nota3 = valida(float(input(f"Digite a terceira nota do aluno {i + 1}: ")))
        alunos[nome] = {
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
        }
#Dicionario
alunos = {}
#qtt de alunos que eu desejo inserir a nota
quantidade_alunos = int(input("Digite a quantidade de alunos: "))
#Preenche o dicionario
preencher_dicionario = inserir_dados_alunos(quantidade_alunos)

for nome, dados in alunos.items():
    nota_final = (dados["nota1"] + dados["nota2"] + dados["nota3"]) / 3
    alunos[nome]["nota_final"] = nota_final

# Imprime os dados do cadastro
for nome, dados in alunos.items():
    print(f"Nome: {nome}")
    print(f"Nota 1: {dados['nota1']}")
    print(f"Nota 2: {dados['nota2']}")
    print(f"Nota 3: {dados['nota3']}")
    print(f"Nota final: {dados['nota_final']}")
    if(dados['nota_final'] < 7):
        print("Este aluno foi reprovado!")
    else:
        print('Aluno aprovado.')



    