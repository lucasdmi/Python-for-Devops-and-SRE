#Crie uma função de Valor Futuro, que calcula o valor de rendimento de
#uma aplicação financeira, dado um aporte inicial VP e parcelas mensais
#PGTO por N períodos a uma taxa i.

#VP(Inicial) 50
#PGTO(Mensal) 10
#n(Mês) = 5
#taxa = 0.01 x mẽs

#Função valor futuro de excel.


def valor_futuro(aporte_inicial, aporte_mensal, qtd_aportes, taxa):
    saldo = aporte_inicial
    for i in range(qtd_aportes):
        valor_futuro_parcela = aporte_mensal * (1 + taxa)**(i)
        saldo += valor_futuro_parcela
    return saldo


# Exemplo de uso

taxa = 0.1
aporte_inicial = int(input('Inserir aporte inicial: '))
aporte_mensal = int(input('Inserir aporte mensal: '))
qtd_aportes = int(input('Inserir a quantidade de aporte: '))


valor_futuro = valor_futuro(aporte_inicial, aporte_mensal, qtd_aportes, taxa)

print(f'O valor total investido será de: {valor_futuro:.2f}')