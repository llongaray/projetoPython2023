# Vamos aprender sobre estruturas de controle em Python, incluindo if, else, for, e while. Essas estruturas são fundamentais para tomar decisões e criar loops para repetir ações.

# Estruturas de Controle: if e else
# if e else
# A estrutura if é usada para tomar decisões condicionais em Python. O bloco de código dentro do if é executado apenas se a condição for verdadeira. O else é opcional e permite especificar um bloco de código a ser executado quando a condição é falsa.

# Exemplo:

idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# No exemplo acima, o programa verifica se idade é maior ou igual a 18. Se for verdade, ele imprime "Você é maior de idade." Se não for, ele imprime "Você é menor de idade."

# Loops: for e while
# for Loop
# O loop for é usado para iterar sobre uma sequência (por exemplo, uma lista, tupla ou string) ou qualquer # objeto iterável.

# Exemplo:

frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Este código percorrerá a lista de frutas e imprimirá cada uma delas.

# while Loop
# O loop while é usado quando você deseja repetir um bloco de código enquanto uma condição for verdadeira.

# Exemplo:

contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1

# Neste exemplo, o bloco de código é repetido enquanto a variável contador for menor que 5. A cada iteração, o valor de contador é incrementado em 1.

# Exemplo Combinando Estruturas de Controle e Loops
# Aqui está um exemplo que combina if, for, e while para criar um programa simples que conta os números pares de 1 a 10:

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "é par.")
    else:
        print(numero, "é ímpar.")

# Este código usa um loop for para iterar de 1 a 10 e um if para verificar se cada número é par ou ímpar.

# Dica:
# Certifique-se de que a indentação (espaços ou tabulações no início das linhas) seja consistente no Python, pois a indentação determina os blocos de código.
# Use : para indicar o início de um bloco if, else, for, ou while.
# A prática é essencial para se tornar confortável com essas estruturas de controle e loops em Python. Experimente criar seus próprios programas para ganhar experiência.