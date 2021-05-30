import time
import sys


class Formatacao:

    def animacao(self, frase):
        self.frase = frase
        for i in list(frase):
            print(i, end='')
            sys.stdout.flush()
            time.sleep(0.06)

    def linha(self, tam=75):
        self.tam = tam
        return '-' * tam

    def cabecalho(self, txt):
        self.txt = txt
        print(self.linha())
        print(self.txt.center(80))
        print(self.linha())



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n <0 or n > 3:
                print('\033[31mEscolha uma opção válida!\033[m')
        except (ValueError, TypeError):
            print(
                '\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return None
        else:
            return n


def inicio(nome):
    if nome == '':
        nome = 'Jogador'
    formato = Formatacao()
    return formato.animacao(f'\n\033[32mOlá {nome}, você acordou as 04:30 no corpo de Nietzsche, um cientista '
                            f'\nalcoólatra de 62 anos que mora com sua família em uma cidade chamada While. '
                            f'\nDescubra o melhor caminho para voltar ao seu corpo!\033[m\n')


def menu_inicial(lista):
    formato = Formatacao()
    formato.cabecalho('\033[;1mMENU PRINCIPAL\033[m')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print('\033[33mPara sair digite 0 (zero).\033[m')
    print(formato.linha())
    opc = leiaInt('Você escolheu: ')
    return opc


def menu(lista):
    fomato = Formatacao()
    fomato.cabecalho('\033[1;30m\033[;1mEscolha uma novo caminho para sua jornada: \033[m')
    # cabecalho('Escolha uma novo caminho para sua jornada: ')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print('\033[33mPara sair digite 0 (zero).\033[m')
    print(fomato.linha())
    opc = leiaInt('Você escolheu: ')
    return opc
