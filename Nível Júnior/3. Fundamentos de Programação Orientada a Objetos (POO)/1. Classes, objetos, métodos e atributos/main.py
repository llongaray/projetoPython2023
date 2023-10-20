# Fundamentos de Programação Orientada a Objetos (POO) em Python
# POO é um paradigma de programação que se baseia no conceito de "objetos". Em Python, você pode criar classes para representar objetos e definir métodos e atributos para essas classes. Aqui estão os conceitos básicos:

# Definindo uma classe
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} {self.ano}, estado: {estado}")

# Criando objetos (instâncias) da classe Carro
carro1 = Carro("Ford", "Focus", 2020)
carro2 = Carro("Toyota", "Corolla", 2021)

# Acessando atributos
marca_carro1 = carro1.marca
modelo_carro2 = carro2.modelo

# Chamando métodos
carro1.ligar()
carro2.desligar()

# Exibindo informações
carro1.info()
carro2.info()

# Herança em POO
# A herança permite criar uma nova classe que herda propriedades e métodos de uma classe existente. Por exemplo:

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, autonomia):
        super().__init__(marca, modelo, ano)
        self.autonomia = autonomia

    def info(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} {self.ano}, estado: {estado}, autonomia: {self.autonomia} km")

# Criando um objeto da classe CarroEletrico
carro_eletrico = CarroEletrico("Tesla", "Model S", 2022, 300)

# Chamando o método info da classe CarroEletrico
carro_eletrico.info()

# Encapsulamento e propriedades
# O encapsulamento permite restringir o acesso a determinados atributos ou métodos de uma classe. Você pode usar o decorador @property para criar propriedades.

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

# Criando um objeto da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Acessando propriedades
nome_pessoa = pessoa.nome
idade_pessoa = pessoa.idade

# Alterando propriedades (não permitido diretamente)
# pessoa.nome = "Bob"  # Isso resultaria em um erro

# Existem muitos outros conceitos e recursos na POO, como encapsulamento, polimorfismo, herança múltipla e interfaces. Esses são os conceitos básicos para começar a trabalhar com POO em Python.
