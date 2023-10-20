# Funções em Python
# Em Python, as funções são blocos de código que realizam tarefas específicas e podem ser reutilizadas em diferentes partes do programa. 
# Aqui está como você pode definir uma função em um arquivo .py:

# Definindo uma função simples
def saudacao():
    print("Olá, seja bem-vindo!")

# Chamando a função
saudacao()

# Neste exemplo, criamos uma função chamada saudacao(), que imprime uma saudação. 
# Para chamar a função e executar o código dentro dela, usamos saudacao().

# Passagem de Argumentos para Funções
# Funções podem aceitar argumentos que permitem personalizar seu comportamento. 
# Aqui está um exemplo de função que aceita um argumento:

def saudar(nome):
    print("Olá, " + nome + "! Seja bem-vindo!")

saudar("Alice")

# Neste caso, a função saudar() aceita um argumento nome e o utiliza para criar a saudação personalizada.

# Escopo de Variáveis
# Em Python, o escopo de uma variável se refere à parte do código onde a variável é acessível. 
# Existem duas categorias principais de escopo: escopo global e escopo local.

# Escopo Global
# Variáveis definidas fora de qualquer função têm escopo global e podem ser acessadas em qualquer lugar do código. 
# Por exemplo:

mensagem = "Olá, mundo!"

def saudacao():
    print(mensagem)

saudacao()

# Neste caso, a variável mensagem está no escopo global e pode ser usada dentro da função saudacao().

# Escopo Local
# Variáveis definidas dentro de uma função têm escopo local e só podem ser acessadas dentro dessa função. 
# Por exemplo:

def saudacao():
    mensagem_local = "Olá, mundo!"
    print(mensagem_local)

saudacao()

# A tentativa de acessar a variável mensagem_local fora da função resultaria em um erro, pois ela é uma variável local.

# Retorno de Valores de Funções
# Funções podem retornar valores usando a instrução return. Isso é útil quando você deseja obter um resultado específico da função.

def adicionar(a, b):
    resultado = a + b
    return resultado

soma = adicionar(3, 4)
print(soma)  # Isso imprimirá 7

# Neste exemplo, a função adicionar() retorna o resultado da soma de a e b, que é então atribuído à variável soma.

# Lembre-se de que variáveis locais só são acessíveis dentro da função onde foram definidas, enquanto variáveis globais são acessíveis em todo o código. 
# O uso apropriado de funções e variáveis é essencial para estruturar e modular seu código em Python.
