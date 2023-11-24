class CalculadoraFesta:
    custo_comida_por_pessoa = 25 #custo fixo

    def __init__(self, numero_de_convidados):
        self.numero_de_convidados = numero_de_convidados

    def custo_comida(self):
        return self.custo_comida_por_pessoa * self.numero_de_convidados

    def custo_bebida(self, tipo_bebida):
        if tipo_bebida.lower() == "suco":
            custo_bebida_por_pessoa = 5
            desconto = 0.05
            return (custo_bebida_por_pessoa * self.numero_de_convidados) * (1 - desconto)
        else:
            custo_bebida_por_pessoa = 20
            return custo_bebida_por_pessoa * self.numero_de_convidados

    def custo_decoracao(self, tipo_decoracao):
        if tipo_decoracao.lower() == "normal":
            custo_base = 30
            custo_decoracao_por_pessoa = 7.5
            return custo_base + (custo_decoracao_por_pessoa * self.numero_de_convidados)
        else:
            custo_base = 50
            custo_decoracao_por_pessoa = 10
            return custo_base + (custo_decoracao_por_pessoa * self.numero_de_convidados)

    def custo_total(self, tipo_bebida, tipo_decoracao):
        return self.custo_comida() + self.custo_bebida(tipo_bebida) + self.custo_decoracao(tipo_decoracao)


numero_de_convidados = int(input("Informe o número de convidados: "))
tipo_bebida = input("Informe o tipo de bebida (suco ou alcoólica): ")
tipo_decoracao = input("Informe o tipo de decoração (normal ou diferenciada): ")

calculadora = CalculadoraFesta(numero_de_convidados)

print(f"O custo da comida é de R$ {calculadora.custo_comida()}")
print(f"O custo da bebida é de R$ {calculadora.custo_bebida(tipo_bebida)}")
print(f"O custo da decoração é de R$ {calculadora.custo_decoracao(tipo_decoracao)}")
print(f"O custo total da festa é de R$ {calculadora.custo_total(tipo_bebida, tipo_decoracao)}")
