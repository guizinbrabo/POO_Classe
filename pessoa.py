from stringprep import b1_set


class Pessoa:
    def __init__(self, nome, data_nascimento, registro, salario, trabalhando=False, estudando=True):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.registro = registro
        self.trabalhando = trabalhando
        self.estudando = estudando
        self.salario = salario

    def apresentar(self):
        print(f'Olá, sou {self.nome} meu aniversario é dia: {self.data_nascimento} ')
        print(f"Estudando: {'Sim' if self.estudando else 'Não'}")
        print(f"trabalhando: {'Sim' if self.trabalhando else 'Não'}")
        print("-" * 20)

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f"{self.nome} começou a trabalhar!")
        else:
            print(f"{self.nome} ja esta trabalhando!")

    def estudar(self):
        if not self.trabalhando:
            self.trabalhando = True
            print(f"{self.nome} começou a trabalhar!")
        elif self.estudando and self.trabalhando:
            self.salario += 1000
            print(
                f"{self.nome}"
                f"começou a estudar e aumentou seu salario para"
                f"R${self.salario:.2f}"
            )
        else:
            print(f"{self.nome} ja esta estudando!")

class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, registro, estudando=False, trabalhando=False, ):
        super().__init__(nome, data_nascimento,registro, estudando, trabalhando)
        self.fome = True
        self.chorando = True
        self.dormindo = False


    def mamar(self):
        if self.chorando:
            print(f"O bebe {self.nome} esta satisfeito")
            self.fome = False
            self.chorando = False
        else:
            print(f"O bebe {self.nome} esta cheio")



    def chorar(self):
        if self.fome:
            self.chorando = True
            print(f"O bebe {self.nome} esta chorando!")
        else:
            print(f"O bebe {self.nome} nao esta chorando!")

    def dormir(self):
        if self.fome:
            print(f"O bebe {self.nome} nao pode dormir!")
        else:
            print(f"O bebe {self.nome} esta dormindo!")
            self.dormindo = True

    def acordar(self):
        if self.dormindo:
            print(f"O bebe {self.nome} acordou !")
            self.dormindo = False
        else:
            print(f"O bebe {self.nome} ja esta acordado !")

    def trabalhar(self):
        print('O bebe nao pode trabalhar')



b1 = Bebe("Luciano", '15/02/2000', "asd123", True, True)

p1 = Pessoa('Guilherme', '15/02/2007', '1', True, True)
p1.apresentar()

