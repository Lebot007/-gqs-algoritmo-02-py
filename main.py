def calcular(num1, num2, operacao):
    """Recebe dois números e um operador, e retorna o resultado da operação."""
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: divisão por zero não é permitida"
        return num1 / num2
    else:
        return "Erro: operação inválida"


if __name__ == "__main__":
    print("=== Calculadora Básica ===")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    resultado = calcular(num1, num2, operacao)
    print(f"Resultado: {resultado}")
