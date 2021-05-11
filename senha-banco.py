print('\033[0;31mBANCO ALLEZ\033[m')
t = 3
senha = str(input('Digite sua senha: '))
senha_correta = '9999'
while not senha.isnumeric() or senha != senha_correta:
    t = t - 1
    if t == 0:
        print('Seu cartão foi bloqueado!')
        quit()
    senha = str(input('Senha incorreta! Digite novamente: (Tentativas Restantes {}) '.format(t)))
print('Acesso permitido')
