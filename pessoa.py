class Pessoa:
    
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def andar(self):
        print('A pessoa começou a caminhar...')
    
    def comer(self):
        print('A pessoa está comendo...')
    
    def dormir(self):
        print('zzzzzzzzzzzz')


class PessoaFisica(Pessoa):
    
    def __init__(self, nome, data_nascimento, cpf=None):
        self.cpf = cpf
        super().__init__(nome, data_nascimento)
    
    def validar_cpf(self):
        if len(self.cpf) == 14:
            print('CPF Válido!')
        else:
            print('CPF Inválido!')
    
    def andar(self):
        print('A pessoa está andando a partir da classe PF')


class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, data_nascimento, cpf, cnpj):
        self.cpf = cpf
        self.cnpj = cnpj
        super().__init__(nome, data_nascimento)
    
    def validar_cnpj(self):
        if len(self.cnpj) == 18:
            print('CNPJ Válido!')
        else:
            print('CNPJ Inválido!')