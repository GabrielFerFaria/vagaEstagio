def fibonacci(num):
    a, b = 0, 1
    
    if num == 0 or num == 1:
        return True
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False
    
num = int(input("Informe um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")