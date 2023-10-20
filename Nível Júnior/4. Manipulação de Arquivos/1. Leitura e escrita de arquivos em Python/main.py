# Manipulação de Arquivos em Python
# Python oferece recursos para ler e escrever arquivos de forma fácil e flexível. Aqui estão exemplos de como realizar essas operações:

# Leitura de um arquivo
# Suponha que você tenha um arquivo de texto chamado "exemplo.txt" com o seguinte conteúdo:

# Olá, mundo!
# Este é um arquivo de exemplo.

# Abrindo um arquivo para leitura (modo "r" para leitura)
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Isso abrirá o arquivo "exemplo.txt", lerá seu conteúdo e o armazenará na variável "conteudo".

# Escrita em um arquivo
# Para escrever em um arquivo, você pode abrir o arquivo no modo "w" (escrita) ou "a" (anexação). Vejamos um exemplo de escrita:

# Abrindo um arquivo para escrita (modo "w" para escrita)
with open("novo_arquivo.txt", "w") as arquivo:
    arquivo.write("Este é um novo arquivo.\n")
    arquivo.write("Python é uma linguagem poderosa!")

# Isso criará um novo arquivo chamado "novo_arquivo.txt" (ou substituirá um arquivo existente) e escreverá o conteúdo fornecido nele.

# Anexação em um arquivo
# Se você deseja adicionar conteúdo a um arquivo existente, pode usar o modo "a" (anexação). Veja um exemplo:

# Abrindo um arquivo para anexação (modo "a" para anexação)
with open("novo_arquivo.txt", "a") as arquivo:
    arquivo.write("\nEste é um novo parágrafo!")

# Isso adicionará o texto fornecido ao final do arquivo existente.

# Leitura de linhas de um arquivo
# Você também pode ler o arquivo linha por linha. Aqui está um exemplo:

# Abrindo um arquivo para leitura (modo "r" para leitura)
with open("exemplo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)

# Isso lerá o arquivo linha por linha e imprimirá cada linha individualmente.

# Tratamento de exceções
# É importante lidar com exceções ao trabalhar com arquivos, pois podem ocorrer erros (por exemplo, o arquivo não existe). Aqui está um exemplo:

try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

# Nesse exemplo, tratamos a exceção FileNotFoundError, que é lançada quando o arquivo não existe.

# Lembre-se de fechar o arquivo após a leitura ou escrita usando "with". Isso garante que o arquivo seja fechado adequadamente e os recursos sejam liberados.

# Existem muitas outras operações que você pode realizar ao trabalhar com arquivos em Python, como manipulação de diretórios, leitura de arquivos CSV, JSON, XML, etc. Esses são os conceitos básicos para começar a trabalhar com arquivos.
