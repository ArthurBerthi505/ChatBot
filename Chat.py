import os

mensagens = []

nome = input('Nome: ')

while True:
    os.system('cls')

    # Mostra mensagens anteriores (se houver)
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['mensagem'])
        print('________________')

    # Sempre pede nova mensagem
    texto = input('Mensagem: ')
    if texto == 'fim':
        break

    mensagens.append({
        'nome': nome,
        'mensagem': texto
    })
