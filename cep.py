# Consumindo API com Python e consultando endereço pelo CEP

import requests
def cep():
    print('-----------------------------------')
    print('\033[1;33;40m>>>>>>>>>> CONSULTAR CEP <<<<<<<<<< \033[m')
    print('-----------------------------------')
    print()
    cep_valido = input('Digite CEP: ')
    if len(cep_valido)  != 8 :
        print('CEP INVALIDO!')
        exit()
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_valido))
    endereço = request.json()
    if 'erro' not in endereço:
        print('CEP VALIDO')
        print('CEP: {}'.format(endereço['cep']))
        print('LOGRADOURO: {}'.format(endereço['logradouro']))
        print('BAIRRO: {}'.format(endereço['bairro']))
        print('LOCALIDADE: {}'.format(endereço['localidade']))
        print('UF:{}'.format(endereço['uf']))
    else:
        print('{} : CEP INVALIDO!'.format(cep_valido))
    
    print('---------------------------------------------------------------')
    opçao = int(input('\033[1;31mDeseja realizar uma nova consulta?\n1.Sim\n2.Não\033[m\n'))
    
    if opçao == 1 :
        cep()
    else:
        print('Saindo...')
if __name__ == '__main__' :
    cep()

    
