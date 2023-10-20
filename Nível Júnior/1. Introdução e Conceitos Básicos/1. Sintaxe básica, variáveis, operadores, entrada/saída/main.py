# Sintaxe Básica:
# Python é conhecido por sua sintaxe limpa e legível, o que o torna uma excelente linguagem para iniciantes. Aqui estão alguns conceitos-chave de sintaxe:

# 1.1. Variáveis:
# Uma variável é um contêiner que armazena um valor. Em Python, você pode criar variáveis atribuindo um valor a um nome:

nome = "João"
idade = 25

# 1.2. Comentários:
# omentários são usados para adicionar notas explicativas ao seu código. Em Python, os comentários começam com o símbolo #:

# Este é um comentário

# 1.3. Indentação:
# Python usa a indentação para definir blocos de código. A maioria das linguagens usa chaves {} para isso, mas em Python, você usa espaços ou tabulações:

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Operadores:
# Operadores são usados para realizar operações em variáveis e valores. Alguns operadores comuns incluem:

# 1.4. Operadores Matemáticos:
# + (adição)
# - (subtração)
# * (multiplicação)
# / (divisão)
# % (módulo, retorna o resto da divisão)
# 1.5. Operadores de Comparação:
# == (igual a)
# != (diferente de)
# < (menor que)
# > (maior que)
# <= (menor ou igual a)
# >= (maior ou igual a)
# Entrada e Saída:
# Para interagir com o usuário, você pode usar as funções input() para receber entrada e print() para exibir saída:

# 1.6. Recebendo Entrada do Usuário:

nome = input("Qual é o seu nome? ")

# 1.7. Exibindo Saída:

print("Olá, " + nome)

# Aqui está um exemplo de programa completo que combina esses conceitos:

# Solicita ao usuário seu nome e idade
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))  # Lê a idade como um número inteiro

# Realiza uma verificação de idade e exibe a mensagem apropriada
if idade >= 18:
    print("Olá, " + nome + "! Você é maior de idade.")
else:
    print("Olá, " + nome + "! Você é menor de idade.")

# Este é um exemplo simples que engloba os conceitos básicos de sintaxe, variáveis, operadores e entrada/saída em Python. Pratique escrevendo pequenos programas para consolidar seu conhecimento.