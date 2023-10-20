# Encapsulamento, Herança e Polimorfismo Básico em Python
# Estes são conceitos avançados em Programação Orientada a Objetos (POO) que permitem criar código mais modular e flexível.

# Encapsulamento
# O encapsulamento é o conceito de limitar o acesso a certos componentes internos de um objeto. Em Python, você pode definir atributos como privados usando um sublinhado duplo (__).

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

# Criando um objeto da classe Animal
animal = Animal("Leão")

# Acessando um atributo encapsulado
nome_do_animal = animal.get_nome()

# Tentativa de acesso direto a um atributo encapsulado (gera um erro)
# nome = animal.__nome

# Herança
# A herança permite que uma classe derive atributos e métodos de outra classe, permitindo a reutilização de código. Aqui está um exemplo:

class Mamifero(Animal):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo

    def info(self):
        print(f"{self.get_nome()} é um mamífero do tipo {self.tipo}.")

# Criando um objeto da classe Mamifero
mamifero = Mamifero("Girafa", "Herbívoro")

# Chamando o método da classe base (Animal)
nome_do_mamifero = mamifero.get_nome()

# Chamando um método da classe derivada (Mamifero)
mamifero.info()

# Polimorfismo
# O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme. Aqui está um exemplo de polimorfismo básico:

class Pato(Animal):
    def __init__(self, nome, cor_bico):
        super().__init__(nome)
        self.cor_bico = cor_bico

    def info(self):
        print(f"{self.get_nome()} é um pato com bico {self.cor_bico}.")

# Criando objetos de diferentes classes
leao = Animal("Leão")
girafa = Mamifero("Girafa", "Herbívoro")
pato = Pato("Pato", "Laranja")

# Usando uma lista polimórfica
animais = [leao, girafa, pato]

# Iterando pela lista de animais e chamando o método info
for animal in animais:
    animal.info()

# O polimorfismo permite que você chame o método info em objetos de diferentes classes e cada objeto executa a versão apropriada do método.

# Estes são conceitos fundamentais em POO em Python e fornecem flexibilidade e reutilização de código.
