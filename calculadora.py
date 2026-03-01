import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular(num1, num2, operacao):
    if operacao == '1':
        return num1 + num2
    elif operacao == '2':
        return num1 - num2
    elif operacao == '3':
        return num1 * num2
    elif operacao == '4':
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida!"

limpar_tela()
nome_usuario = input("Digite seu nome: ")
print(f"\nOlá, {nome_usuario}! Bem-vindo à Calculadora 🚀")

while True:
    print("\n" + "-"*30)
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("-"*30)

    operacao = input("Escolha uma opção: ")

    if operacao == '5':
        print("Encerrando programa...")
        break

    if operacao not in ['1','2','3','4']:
        print("Opção inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números válidos.")
        continue

    resultado = calcular(num1, num2, operacao)
    print(f"\nResultado: {resultado}")