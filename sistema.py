from projeto.lib.interface import *

if __name__ == "__main__":
    jogador = input("Digite seu nome: ")
    inicio(jogador)
    formato = Formatacao()

    while True:

        resposta = menu_inicial(['Revirar a casa atrás de respostas.',
                                 'Pegar a Pistola de portais.', 'Buscar uma fórmula científica.'])
        if resposta == 1:
            formato.cabecalho(
                '\033[;1mRevirar a casa atrás de respostas\033[m')
            respostaA = menu(
                ['Abrir portas.', 'Abrir frigobar.', 'Ir para o laboratório.'])
            if respostaA == 1:
                formato.cabecalho('\033[;1mAbrir portas\033[m')
                formato.animacao(
                    '\033[31mVocê encontrou um alienígena que te aprisionou!\nRetornando ao início...\033[m\n')
                inicio(jogador)
            elif respostaA == 2:
                formato.cabecalho('\033[;1mAbrir frigobar\033[m')
                formato.animacao(
                    '\033[31mNenhuma resposta, só latinhas de cerveja vazias!\nRetornando ao menu principal...\033[m\n')
                continue
            elif respostaA == 3:
                formato.cabecalho('\033[;1mIr para o laboratório\033[m')
                formato.animacao('\033[36mOpa, você está no caminho certo!\033[m\n')
                respostaA1 = menu(['Pegar a Pistola de portais.',
                                   'Misturar líquido azul com marrom.', 'Ler bloco de anotações.'])
                if respostaA1 == 0:
                    formato.animacao('\033[31mAté a próxima!\033[m\n')
                    break
                elif respostaA1 == 1:
                    formato.cabecalho(
                        '\033[;1mPegar a Pistola de portais\033[m')
                    formato.animacao(
                        '\033[31mAi meu deus, você caiu na boca de uma Python e foi devorado!\nRetornando ao '
                        'início...\033[m\n')
                    inicio(jogador)

                elif respostaA1 == 2:
                    formato.cabecalho(
                        '\033[;1mMisturar líquido azul com marrom\033[m')
                    formato.animacao(
                        '\033[31mEi, você não tem conhecimentos para isso, sua fórmula explodiu!\nRetornando ao menu '
                        'principal...\033[m\n')
                    continue
                elif respostaA1 == 3:
                    formato.cabecalho('\033[;1mLer bloco de anotações\033[m')
                    formato.animacao(
                        '\033[36mBingo! No bloco de anotações você encontrou possíveis respostas!\033[m\n')
                    respostaA2 = menu(['Tentar experimento da página 48.',
                                       'Tentar experimento da página 62.', 'Tentar experimento da página 221.'])
                    if respostaA2 == 0:
                        formato.animacao('\033[31mAté a próxima!\033[m\n')
                        break
                    elif respostaA2 == 1:
                        formato.cabecalho(
                            '\033[;1mTentar experimento da página 48\033[m')
                        formato.animacao(
                            '\33[31mPutz, o experimento foi um fracasso e seu corpo desintegrou!\nRetornando ao '
                            'início...\033[m\n')
                        inicio(jogador)
                    elif respostaA2 == 2:
                        formato.cabecalho(
                            '\033[;1mTentar experimento da página 62\033[m')
                        formato.animacao(
                            '\033[31mParabéns! você conseguiu, mas, calma aí esse experimento é para se transformar: '
                            'em PICLES!\nRetornando ao menu principal...\033[m\n')
                        continue
                    elif respostaA2 == 3:
                        formato.cabecalho(
                            '\033[;1mTentar experimento da página 221\033[m')
                        formato.animacao(
                            '\033[36mEste foi o experimento realizado por Nietzsche as 04:20, pouco antes de você'
                            '\nacordar no corpo dele. Poxa, esse cientista bêbado só faz maluquice!'
                            '\nParabéns! Você encontrou o caminho certo e voltará ao seu corpo!\033[m\n')
                        break
        elif resposta == 2:
            formato.cabecalho('\033[;1mPegar a Pistola de portais\033[m')
            respostaB = menu(['Ir para uma praia alienígena.',
                              'Achar minha mãe.', 'Ir ao bar.'])
            if respostaB == 0:
                formato.animacao('\033[31mAté a próxima!\033[m\n')
                break
            elif respostaB == 1:
                formato.cabecalho(
                    '\033[;1mIr para uma praia alienígena\033[;1m')
                formato.animacao(
                    '\033[31mAi meu deus, você caiu na boca de uma Python e foi devorado!\nRetornando ao '
                    'início...\033[m\n')
                inicio(jogador)
            elif respostaB == 2:
                formato.cabecalho('\033[;1mAchar minha mãe\033[m')
                formato.animacao(
                    '\033[31mVocê acordou no colo da sua mãe e ela te disse três coisas:\nRetornando ao menu '
                    'principal...\033[m\n')
                continue
            elif respostaB == 3:
                formato.cabecalho('\033[;1mIr ao bar\033[m')
                formato.animacao('\033[36mVocê encontrou o amigo de Nietzsche: Swift, cientista de 55 anos!\033[m\n')
                respostaB1 = menu(
                    ['Beber com seu amigo.', 'Conversar sobre sua situação.', 'Chamar para jogar.'])
                if respostaB1 == 0:
                    formato.animacao('\033[31mAté a próxima.\033[m\n')
                    break
                if respostaB1 == 1:
                    formato.cabecalho('\033[;1mBeber com seu amigo\033[m')
                    formato.animacao(
                        '\033[31mVocê bebeu até entrar em coma alcoólico \nRetornando ao início...\033[m\n')
                    inicio(jogador)
                elif respostaB1 == 2:
                    formato.cabecalho(
                        '\033[;1mConversar sobre sua situação\033[m')
                    formato.animacao(
                        '\033[31mSeu amigo era um impostor, e na verdade era um alienígena que te roubou!\nRetornando '
                        'ao menu principal...\033[m\n')
                    continue
                elif respostaB1 == 3:
                    formato.cabecalho('\033[;1mChamar para jogar\033[m')
                    formato.animacao('\033[36mOpa, Swift não te reconheceu!\033[m\n')

                    respostaB2 = menu(
                        ['Dizer seu nome a ele.', 'Pedir socorro gritando.', 'Tentar beber e conversar com Swift.'])
                    if respostaB2 == 0:
                        formato.animacao('\033[31mAté a próxima!\033[m\n')
                        break
                    elif respostaB2 == 1:
                        formato.cabecalho('\033[;1mDizer seu nome a ele\033[m')
                        formato.animacao(
                            '\033[31mSwift acha que você é um impostor e te mata!\nRetornando ao início..\033[m\n')
                        inicio(jogador)
                    elif respostaB2 == 2:
                        formato.cabecalho(
                            '\033[;1mPedir socorro gritando\033[m')
                        formato.animacao(
                            '\033[31mSwift ficou confuso e fugiu!\nRetornando ao menu principal...\033[m\n')
                        continue
                    elif respostaB2 == 3:
                        formato.cabecalho(
                            '\033[;1mTentar beber e conversar com Swift\033[m')
                        formato.animacao(
                            '\033[36mVocê bebeu até cair e bater a cabeça.\nAcordou em seu quarto e viu que era '
                            'apenas um sonho!\033[m\n')
                        break
        elif resposta == 3:
            formato.cabecalho('\033[;1mBuscar uma fórmula científica\033[m')
            respostaC = menu(['Misturar líquido azul com marrom.',
                              'Pedir socorro ao seu neto.', 'Ler bloco de anotações.'])
            if respostaC == 0:
                formato.animacao('\033[31mAté a próxima.\033[m\n')
                break
            elif respostaC == 1:
                formato.cabecalho(
                    '\033[;1mMisturar líquido azul com marrom\033[m')
                formato.animacao(
                    '\033[31mEi, você não tem conhecimentos para isso, sua fórmula explodiu!\nRetornando ao '
                    'início...\033[m')
                inicio(jogador)
            elif respostaC == 2:
                formato.cabecalho('\033[;1mPedir socorro ao seu neto\033[m')
                formato.animacao(
                    '\033[31mSeu neto ficou com medo e fugiu \nRetornando ao menu principal...\033[m\n')
                continue
            elif respostaC == 3:
                formato.cabecalho('\033[;1mLer bloco de anotações\033[m')
                formato.animacao(
                    '\033[36mBingo! No bloco de anotações você encontrou possíveis respostas.\033[m\n')

                respostaC1 = menu(
                    ['Anotações página 1.', 'Anotações página 30.', 'Anotações página 221.'])
                if respostaC1 == 0:
                    formato.animacao('\033[31mAté a próxima!\033[m\n')
                    break
                elif respostaC1 == 1:
                    formato.cabecalho('\033[;1mAnotações página 1\033[m')
                    formato.animacao(
                        '\033[31mOpa, nessa anotação só tem receitas de cervejas!\nRetornando ao início...\033[m\n')
                    inicio(jogador)
                elif respostaC1 == 2:
                    formato.cabecalho('\033[;1mAnotações página 30\033[m')
                    formato.animacao(
                        '\033[31mVocê conseguiu abrir um portal, mas caiu em um universo paralelo!\nRetornando ao '
                        'menu principal...\033[m\n')
                    continue
                elif respostaC1 == 3:
                    formato.cabecalho(
                        '\033[;1mNossa, mas que língua é essa?\033[m')
                    formato.animacao(
                        '\033[31m({++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++++++++.>+++++.++++.\n'
                        '+++.----.-------.++++++++++++++.<<++.>>--------------.<<.>>++++++++.----\n'
                        '----.+++++++.----.++++++++++.<<.>>-.++++.----------------.<<.>>--.+++++++\n'
                        '+++++.--.+++.----.-------.+++++++++++++++++++.---------.<<<++++++++++.})\033[m\n')
                    respostaC2 = menu(
                        ['Tentar decifrar.', 'Ver a próxima página.', 'Olhar no marcador de páginas.'])
                    if respostaC2 == 0:
                        formato.animacao('\033[31mAté a próxima!\033[m\n')
                        break
                    elif respostaC2 == 1:
                        formato.cabecalho('\033[;1mTentar decifrar\033[m')
                        formato.animacao(
                            '\033[31mÉ uma linguagem muito complexa!\nRetornando ao início...\033[m\n')
                        inicio(jogador)
                    elif respostaC2 == 2:
                        formato.cabecalho('\033[;1mVer a próxima página\033[m')
                        formato.animacao(
                            '\033[31mSão só receitas de cerveja!Retornando ao menu principal...\033[m\n')
                        continue
                    elif respostaC2 == 3:
                        formato.cabecalho(
                            '\033[;1mOlhar no marcador de páginas\033[m')
                        formato.animacao('\033[36mOlha só isso! É uma linguagem em código BrainFuck.'
                                         '\nA tradução é: "Simples é melhor que complexo"!'
                                         '\nTudo isso foi uma alucinação Nietzsche, o efeito do picles radioativo '
                                         'passou!\033[m\n')
                        break
        if resposta == 0:
            formato.animacao('\033[31mAté a próxima!\033[m\n')
            break