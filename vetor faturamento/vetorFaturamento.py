import json

with open('vetor faturamento/faturamento.json', 'r') as file:
    faturaDiaria = json.load(file)

faturamentoValido = [dia['faturamento'] for dia in faturaDiaria if dia['faturamento'] > 0]
minFaturamento = min(faturamentoValido)
maxFaturamento = max(faturamentoValido)
medFaturamento = sum(faturamentoValido) / len(faturamentoValido)
diasAcima = len([faturamento for faturamento in faturamentoValido if faturamento > medFaturamento])
print(f"Menor faturamento diário: R$ {minFaturamento}")
print(f"Maior faturamento diário: R$ {maxFaturamento}")
print(f"Dias com faturamento acima da média: {diasAcima}")