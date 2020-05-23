'''variavel = False

if variavel:
    print('A variável é verdadeira...')
else:
    print('A variável NÃO é verdadeira...')
'''
idade = 50
tem_ingresso = False

if idade >= 18 or tem_ingresso:
    print('Pode entrar no show')
elif idade >= 16 and tem_ingresso: # else if
    print('Pode entrar no show acompanhado')
else:
    print('Vai pra casa dormir')