# Manipulação de Strings em Python
# As strings são sequências de caracteres e são amplamente utilizadas em Python. Você pode realizar várias operações de manipulação de strings. Aqui estão algumas das operações comuns:

# Criando uma string
minha_string = "Olá, Mundo!"

# Acessando caracteres em uma string
primeiro_caractere = minha_string[0]  # Obtém o primeiro caractere (O)
segundo_caractere = minha_string[1]  # Obtém o segundo caractere (l)

# Concatenação de strings
string1 = "Olá,"
string2 = " Mundo!"
mensagem = string1 + string2  # Concatena as duas strings em uma única string ("Olá, Mundo!")

# Comprimento de uma string
tamanho = len(minha_string)  # Retorna o tamanho da string (12)

# Divisão de uma string em partes
minha_string = "Python é uma linguagem de programação"
palavras = minha_string.split(" ")  # Divide a string em palavras com base no espaço em branco

# Substituição de substrings
frase = "Eu gosto de cães."
nova_frase = frase.replace("cães", "gatos")  # Substitui "cães" por "gatos"

# Busca em strings
procurar = "gatos" in nova_frase  # Verifica se "gatos" está na nova_frase

# Maiúsculas e minúsculas
maiusculas = minha_string.upper()  # Converte para maiúsculas
minusculas = minha_string.lower()  # Converte para minúsculas

# Formatação de strings
nome = "Alice"
idade = 30
mensagem_formatada = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)

# Fatiamento de strings
parte_da_string = minha_string[7:12]  # Obtém os caracteres da posição 7 à 12 ("uma l")

# Remoção de espaços em branco
texto_com_espacos = "   Isso é um exemplo   "
texto_sem_espacos = texto_com_espacos.strip()  # Remove espaços em branco do início e do final

# Verificando o início e o fim de uma string
comeca_com = minha_string.startswith("Python")  # Verifica se a string começa com "Python"
termina_com = minha_string.endswith("programação")  # Verifica se a string termina com "programação"

# Indexação reversa
ultimo_caractere = minha_string[-1]  # Obtém o último caractere

# Unindo strings de uma lista
lista_de_strings = ["Python", "é", "uma", "linguagem"]
frase_unida = " ".join(lista_de_strings)  # Une as strings com espaços

# Remoção de caracteres indesejados
frase_com_espacos = "   Isso é um exemplo   "
frase_sem_espacos = frase_com_espacos.strip()  # Remove espaços em branco

# Quebra de linha
quebra_de_linha = "Isso é uma linha.\nE esta é outra linha."  # \n representa uma quebra de linha

# Caracteres de escape
caracter_escape = "Isso é um exemplo de caractere de escape: \\"

# Formatação de strings f-strings (Python 3.6+)
nome = "Alice"
idade = 30
mensagem_formatada = f"Olá, meu nome é {nome} e eu tenho {idade} anos."

# Unicode e caracteres especiais
caractere_especial = "\u0394"  # Exemplo de caractere grego delta (Δ)

# Existem muitas outras operações que você pode realizar com strings em Python, mas essas são algumas das mais comuns.
