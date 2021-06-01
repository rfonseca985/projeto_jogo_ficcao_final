import time
import sys


class Formatacao:
    """
    Classe responsavel pelos elementos de formatção de texto 
    """

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


# Faz a validação da escolha e o tipo do input retornando uma excessão caso não seja int ou seja diferente das opções
def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0 or n > 3:
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
        
        
#Apresenta ao jogador a história e cada vez que o jogador escolhe a opção 2 do submenu
def inicio(nome):
    if nome == '':
        nome = 'Jogador(a)'
    formato = Formatacao()
    return formato.animacao(f'\n\033[32mOlá {nome}, você acordou as 04:30 no corpo de Nietzsche, um cientista '
                            f'\nalcoólatra de 62 anos que mora com sua família em uma cidade chamada While. '
                            f'\nDescubra o melhor caminho para voltar ao seu corpo!\033[m\n')


# Exibi as opções do menu principal cada vez que o jogador escolhe a opção 1 do submenu
def menu_inicial(lista):
    formato = Formatacao()
    formato.cabecalho('\033[;1mMENU PRINCIPAL\033[m')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print('\033[33mPara sair digite 0 (zero).\033[m')
    print(formato.linha())
    opc = leia_int('Você escolheu: ')
    return opc

# Exibi as opções dos submenus para que o jogador escolha um novo caminho para sua jornada
def menu(lista):
    fomato = Formatacao()
    fomato.cabecalho(
        '\033[1;30m\033[;1mEscolha um novo caminho para sua jornada: \033[m')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print('\033[33mPara sair digite 0 (zero).\033[m')
    print(fomato.linha())
    opc = leia_int('Você escolheu: ')
    return opc


class ContaTempo:
    """
    Classe responsavel por contabilizar o tempo das jogadas e caso ultrapasse o limite encerra o programa
    """
    def __init__(self):
        self.hora = 4
        self.minuto = 30

    def avanca_tempo(self, minutos):
        self.minuto += minutos
        while self.minuto >= 60:
            self.minuto -= 60
            self.hora += 1
        print(
            f"Agora são {self.hora}h{self.minuto}'.\nVocê tem até as 14h30' para voltar ao seu corpo")
        return self.hora, self.minuto

    def tempo_final(self):
        return (self.hora >= 14 and self.minuto >= 30) or self.hora >= 15