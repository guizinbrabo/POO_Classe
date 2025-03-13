class Eletronico():
    def __init__(self, nome, marca, bateria, processador, camera, nome_da_loja,  a_venda=True):
        self.nome = nome
        self.marca = marca
        self.bateria = bateria
        self.processador = processador
        self.camera = camera
        self.a_venda = a_venda
        self.nome_da_loja = nome_da_loja

    def get_nome(self):
        return self.nome
    def get_marca(self):
        return self.marca
    def get_bateria(self):
        return self.bateria
    def get_processador(self):
        return self.processador
    def get_camera(self):
        return self.camera
    def get_nome_da_loja(self):
        return self.nome_da_loja

    def status(self):
        print(f'nome do eletronico: {self.nome}')
        print(f'marca do eletronico: {self.marca}')
        print(f'bateria do eletronico: {self.bateria}')
        print(f'processador do eletronico: {self.processador}')
        print(f'camera do eletronico: {self.camera}')
        if self.a_venda:
            print(f'O eletronico está a venda')
        else:
            print(f'O eletronico não está a venda')
        print(f'A loja {self.nome_da_loja} está vendendo o {self.nome}')


    def vender(self):
        if self.a_venda:
            print(f' o eletronico {self.nome} já está a venda')
        else:
            self.a_venda = True
            print(f'O eletronico {self.nome} está a venda agora')
    def parar_venda(self):
        if self.a_venda:
            self.a_venda = False
            print(f'O eletronico saiu de venda')
        else:
            print(f' o eletronico não está a venda')

class Celular(Eletronico):
    def __init__(self, nome, marca, bateria, processador, camera):
        super().__init__(nome, marca,bateria, processador, camera,nome_da_loja='', a_venda=False)
        self.nome = nome
        self.marca = marca
        self.bateria = bateria
        self.processador = processador
        self.camera = camera
        self.ligado = False
        self.jogar = False

    def ligar(self):
        if self.ligado:
            print(f'O {self.nome} já está ligado')
        else:
            self.ligado = True
            print(f'o {self.nome} está ligado agora')
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O celular está desligado agora')
        else:
            print(f'O celular já está ligado')
    def jogar(self):
        if self.ligado:
            if self.jogar:
                print(f'O celular já está em um jogo')
            else:
                self.jogar = True
                print(f'O celular abriu um jogo')
        else:
            print(f'o celular está desligado')
    def status(self):
        print(f'nome do eletronico: {self.nome}')
        if self.ligado:
            print(f'o celular está ligado')
        else:
            print(f'celular está desligado')
        if self.jogar:
            print(f'O celular está com um jogo em aberto')
        else:
            print(f'celular não está com nenhum jogo rodando')

    def vender(self):
        print(f'O celular não pertence a nenhuma loja, não pode estar a venda')
    def parar_venda(self):
        print(f'celular não está em um nenhuma loja')


tronico1 = Eletronico('galaxy s9', 'Samsung', 4500, 'snapdragon g3', '4 cameras', 'magazine Luiza',True)
radin1 = Celular('galaxy s9','samsung','4500','snapdragon g3','4 cameras')
radin1.status()


