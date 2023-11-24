class Pessoa:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro

    def emprestarDinheiro(self, quantia):
        if quantia > self.dinheiro:
            raise ValueError("Saldo insuficiente.")
        self.dinheiro -= quantia
        return quantia

    def receberDinheiro(self, quantia):
        self.dinheiro += quantia
        return quantia

emprestador = Pessoa("Lucas", 100)
emprestado = Pessoa("Maria", 200)

quantiaEmprestada = emprestador.emprestarDinheiro(50)
emprestado.receberDinheiro(quantiaEmprestada)

print(f"Lucas emprestou {quantiaEmprestada} para Maria.")
print(f"Saldo de Lucas: {emprestador.dinheiro}")
print(f"Saldo de Maria: {emprestado.dinheiro}")