def inverter_string(s):
    resultado = ''
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

def main():
    string_original = input("Informe a string para inverter: ")
    string_invertida = inverter_string(string_original)
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()