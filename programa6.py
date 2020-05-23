lista = ['string', 1, 5.1, True, False, tuple()] # MUTÁVEL
tupla = ('string', 1, 5.1, True, False, list()) # IMUTÁVEL
dicionario = {'string': 'PALAVRA', 1: 2, 5.1: 6.1, True: False, False: True, 'lista': list()} # MUTÁVEL
# conjunto = set()

# print('Lista:', lista)
# print('Tupla:', tupla)
# print('Dicionário:', dicionario)

# lista.append(50)

# print('Lista:', lista)
# print('Lista:', lista[2])

# tupla.append(10) # NÃO PODE SER FEITO

# print('Tupla:', tupla[2])

dicionario['novo_valor'] = 'novo valor adicionado'

print('Dicionário:', dicionario)
print('Dicionário:', dicionario['string'])