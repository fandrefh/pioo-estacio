from pessoa import PessoaFisica, PessoaJuridica

pf1 = PessoaFisica("Pessoa Física Nova", "23/09/1990", "12.456.789-09")

print('Dados da PF1')
print('Nome:', pf1.nome)
print('CPF:', pf1.cpf)
print('Data nascimento:', pf1.data_nascimento)
pf1.andar()
pf1.comer()
pf1.dormir()
pf1.validar_cpf()

pj1 = PessoaJuridica("Francisco André", "22/03/1970", "123.987.675-00", "12.000.000/0001-00")

print('Dados da PJ1')
print('Nome:', pj1.nome)
print('CPF:', pj1.cpf)
print('Data nascimento:', pj1.data_nascimento)
pj1.validar_cnpj()