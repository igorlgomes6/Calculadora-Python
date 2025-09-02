# Calculadora simples em Python
# O usuário digita a operação no formato: primeiroNumero operador segundoNumero
# Exemplo: 10 + 5

# Entrada do usuário
operacao = input("Digite a operação: ")

# Divide a string em partes (primeiroNumero, operador, segundoNumero)
partes = operacao.split()

# Conversão dos números para float
primeiroNumero = float(partes[0])
operador = partes[1]
segundoNumero = float(partes[2])

# Verificação do operador e cálculo
if operador == "+":
    resultado = primeiroNumero + segundoNumero
elif operador == "-":
    resultado = primeiroNumero - segundoNumero
elif operador == "x" or "*":
    resultado = primeiroNumero * segundoNumero
elif operador == "/" or ":":
    resultado = primeiroNumero / segundoNumero
else:
    print("Operador inválido.")
    exit()

# Exibe o resultado
# Se o resultado for inteiro (ex: 10.0), mostra apenas como inteiro
if resultado == int(resultado):
    print("O resultado é: ", int(resultado))
else:
    # Caso contrário, exibe com uma casa decimal
    print(f"O resultado é: {resultado:.2f}")
