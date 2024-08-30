estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcPercentual(faturamento):
    totalFatura = sum(faturamento.values())
    percentual = {estado: (valor / totalFatura) * 100 for estado, valor in faturamento.items()}
    return percentual, totalFatura

def main():
    percentual, totalFatura = calcPercentual(estados)
    print(f"Valor total de faturamento: R${totalFatura:,.2f}")
    print("Percentual de representação por estado:")
    for estado, perc in percentual.items():
        print(f"{estado}: {perc:.2f}%")

if __name__ == "__main__":
    main()