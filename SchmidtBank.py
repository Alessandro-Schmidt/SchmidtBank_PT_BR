def linha(a=70):
    print('-'*a)


def title(*k):
    linha(len(k[0])*2)
    for c in range(0,len(k)):
        print(k[c].center(len(k[0]*2)))
    linha(len(k[0]) * 2)


def calcul_juros(valor, rentabil, vezes):
    import matplotlib.pyplot as plt
    evolucao = [valor]
    contador = [0]
    y = valor
    x = (rentabil/100)+1
    for c in range(1,vezes+1):
        y*=x
        linha(len(f'{c}ª operação: R$ {y:.0f},00'))
        print(f'{c}ª operação: R$ {y:.0f},00')
        evolucao.append(y)
        contador.append(c)
    lucro = y - valor
    if lucro>0:
        color = 32
    else:
        color = 31
    linha(len(f'{c}ª operação: R$ {y:.0f},00'))
    print(f'Estatísticas:\nValor inicial: R$ {valor:.0f},00\nValor Final: R$ {y:.0f},00'
          f'\n\033[{color}mPerformance: R$ {lucro:.0f},00\033[m')
    while True:
        opt = str(input('Deseja criar um gráfico do seu investimento?\n[S/N]: ')).upper()[0]
        if opt in 'N':
            break
        if opt in 'S':
            plt.figure(figsize=(14, 7))
            plt.plot(contador, evolucao, label='Valor do Investimento', color="green")
            plt.title(
                f'Exemplo de juros compostos\nInvestimento de R$ {valor:.0f},00 | Rentabilidade de {rentabil}%/Trade')
            plt.xlabel("\nTrades Realizados")
            plt.ylabel("Valor em R$\n")
            plt.xlim((0, vezes + 1))
            o = max(evolucao)
            plt.ylim(valor, o + (o / 10))
            plt.legend()
            plt.grid(True, which='both')
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')
            plt.annotate(
                f'Estatísticas:\nValor inicial: R$ {valor:.2f}\nValor final: R$ {y:.2f}\nLucro: R$ {y - valor:.2f}',
                (vezes / 10, y * 0.9), bbox={"boxstyle": "sawtooth", "color": "goldenrod"}, color="black")
            plt.annotate(f'Valor final: R$ {y:.0f},00', (vezes - (vezes / 9), y),
                         bbox={"boxstyle": "square", "color": "darkorange"}, color="white")
            plt.annotate('Um projeto de Alessandro Maciel Schmidt\n2º Período - Engenharia de Software PUCPR',
                         (vezes * 0.6, valor * 1.05), bbox={"boxstyle": "square", "color": "royalblue"}, color="black")
            plt.show()
            break
            

def calc_vaciacao_ativo(nome,aporte,price_in, price_out):
    import matplotlib.pyplot as plt
    from math import floor
    shares = aporte/price_in
    floor(shares)
    valor_final = shares*price_out
    performance = valor_final - aporte
    rentabil = ((valor_final*100)/aporte)/100
    if performance>0:
        type = f'\033[32mLucro: R$ {performance:.2f}\033[m\n'
    else:
        type = f'\033[31mPrejuízo: R$ {performance:.2f}\033[m\n'
    print(f'\nEstatísticas de investimento em {nome}:\nValor inicial: R${aporte:.0f},00\nCotas: {floor(shares)} ações\n'
          f'Valor final: R$ {valor_final:.2f}\n{type}')
    while True:
        try:
            opt = str(input('Deseja uma opção gráfica?\n[S/N]: ')).upper()[0]
            if opt in 'N':
                break
            elif opt in 'S':
                plt.figure(figsize=(14,7))
                plt.plot()
                plt.title(f'Investimento em {nome}\nPreço de entrada: {price_in} | Preço de saída: {price_out}')
                plt.xlabel('\nPreço do ativo')
                plt.ylabel('Valor em R$\n')
                plt.grid(True,which='both')
                plt.axhline(y=aporte,color='k')
                plt.axvline(x=price_in,color="k")
                if performance>0:
                    color = '--g'
                    coorde_label_me = ((price_in + price_out) / 2, aporte * 1.005)
                    coorde_label_price_final = (price_out-1, valor_final-performance/2)
                    coorde_stats = (price_in, valor_final - (performance / 10))
                    colores = "green"
                else:
                    color= '--r'
                    coorde_label_me = (price_out, aporte * 0.998)
                    coorde_label_price_final = (price_out+1, ( (valor_final - (performance/2) )))
                    coorde_stats = (price_in-1,valor_final-(performance/10))
                    colores = "red"
                    
                plt.plot([price_in, price_out], [aporte, valor_final], f"{color}")
                """
                Na linha 88, você teve vontade de se matar. 
                plt.plot([x_inicial, x_final], [y_inicial, y_final], "tipo de flecha e cor")
                """
                plt.plot(price_in, aporte, "ro")
                plt.plot(price_out, valor_final, "ro")
                plt.annotate('Um projeto de Alessandro Maciel Schmidt\n2º Período - Engenharia de Software PUCPR',
                             coorde_label_me, bbox={"boxstyle": "square", "color": "royalblue"},
                             color="black")
                plt.annotate(f'Estatísticas\nInvestimento inicial: R$ {aporte:.2f}\nPerformance: R${performance:.2f}\nRentabilidade: {rentabil:.2f}%',coorde_stats, bbox={"boxstyle":"circle", "color":colores}, color="white")
                plt.annotate(f'Valor final: R$ {valor_final:.2f}', (price_out,valor_final), coorde_label_price_final, arrowprops={"arrowstyle":"-|>"}, bbox={"boxstyle":"round4", "color":"navy"},color="white")
                plt.show()
                break
        except:
            print('\n\033[31mDigite uma opção válida no menu!\033[m\n')
            


# Programa principal:

while True:
    linha(70)
    print('SCHMIDTBANK'.center(70))
    print('Um projeto SchmidTech'.center(70))
    linha(70)
    try:
        opt = int(input('Qual serviço deseja?\n[1] - Investimento e Juros compostos\n'
                        '[2] - Variação de preço de Ativo\n[3] - '
                        'Fechar programa\nDesejo: '))
        if opt ==3:
            break
        elif opt>3 or opt<0:
            print('\033[31mDigite apenas [1], [2] ou [3]\033[m')
        elif opt ==2:
                while True:
                    title('Variação de preço de ativo', 'Opção gráfica', 'Rentabilidade')
                    try:
                        nome = str(input('Digite o nome do ativo: '))
                        try:
                            aporte = float(input('Qual o aporte inicial: R$ '))
                            try:
                                price_dentro = float(input(f'Qual o preço [mˆ2, valor de ação] de {nome}:\nR$ '))
                                try:
                                    price_fora = float(input(f'Qual o preço de venda provisionado de {nome}? R$ '))
                                    calc_vaciacao_ativo(nome, aporte, price_dentro, price_fora)
                                    while True:
                                        try:
                                            choice = int(input('[1] - Voltar ao menu principal\n[2] - Nova aplicação\nOpção: '))
                                            break
                                        except:
                                            print('\n\033[31mDigite uma opção válida no menu!\033[m\n')
                                    if choice == 1:
                                        break
                                except:
                                    print('\n\033[31mDigite um preço de venda válido!!\033[m\n')
                            except:
                                print('\n\033[31mDigite um preço de entrada válido!\033[m\n')
                        except:
                            print('\n\033[31mDigite um aporte válido!\033[m\n')
                    except:
                        print('\n\033[31mDigite algo válido!\033[m\n')
        elif opt ==1:
            while True:
                title('Investimentos com Juros compostos', 'Opção gráfica',)
                try:
                    valor = float(input('Digite o valor da aplicação: R$ '))
                    try:
                        rent = float(input('Digite a rentabilidade em %: '))
                        try:
                            vezes = int(input(f'Quantas operações com rentabilidade de {rent}%: '))
                            calcul_juros(valor,rent,vezes)
                            while True:
                                try:
                                    choice = int(input('[1] - Voltar ao menu principal\n[2] - Nova aplicação\nOpção: '))
                                    break
                                except:
                                    print('\n\033[31mDigite uma opção válida no menu!\033[m\n')
                            if choice ==1:
                                break
                        except:
                            print('\n\033[31mDigite um número de vezes válido [número inteiro]!\033[m\n')
                    except:
                        print('\n\033[31mDigite uma rentabilidade válida!\033[m\n ')
                except:
                    print('\n\033[31mDigite um valor de aplicação válido!\033[m\n')
    except:
        print('\n\033[31mDigite um valor válido no menu!\033[m\n')
title('Este projeto foi desenvolvido por Alessandro Maciel Schmidt', 'Engenharia de Software - PUCPR',
      '2º Período')