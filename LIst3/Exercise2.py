

class Calculadora:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def soma(self):
        return self.n1 + self.n2

    def subtracao(self):
        return self.n1 - self.n2

    def multiplicacao(self):
        return self.n1 * self.n2

    def divisao(self):
        return self.n1 / self.n2


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

calculadora = Calculadora(numero1, numero2)
print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"{numero1} + {numero2} = {calculadora.soma()}")
elif opcao == 2:
    print(f"{numero1} - {numero2} = {calculadora.subtracao()}")
elif opcao == 3:
    print(f"{numero1} * {numero2} = {calculadora.multiplicacao()}")
elif opcao == 4:
    print(f"{numero1} / {numero2} = {calculadora.divisao()}")
else:
    print("Opção inválida.")