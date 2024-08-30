#parte para adicionar imports
import datetime
import random

#configurações iniciais

mensagem_de_desligamento = "desligando"

historico = []

data_atualização = ('29/08/2024')

quantidade_de_arquivos = 0

salvos = []

memoria0 = 0
memoria1 = 0

#criando usuario

username = input("digite seu nome do usuario")
senha = input("crie sua senha")
memoria0 = float(input("quanto de memoria deseja usar?"))
memoria1 = (memoria0 + 1)
while (memoria0 == 0):
    print("quantidade invalida")
    print("desligando...")
    break

else:
    # versão

    versão = ("0.3.9")

    # tela de login ;)
    usuario_correto = username

    senha_correta = senha

    numero_de_tent1 = 0
    numero_de_tent2 = 0

    print(f"bem-vindo ao duDOS {versão}")

    usuario_tent = str(input("digite usuario"))

    running = 0

    writting = 0

    while usuario_tent != usuario_correto:
        print("usuario incorreto, tente novamente")
        if numero_de_tent1 == 3:
            break
        usuario_tent = str(input("digite usuario"))
        numero_de_tent1 += 1

    else:
        senha_tent = str(input("digite sua senha"))

        while senha_tent != senha_correta:
            print("senha incorreta")
            if numero_de_tent2 == 3:
                break
            senha_tent = str(input("digite sua senha"))
            numero_de_tent2 += 1

        else:
            print(f"bem vindo {usuario_tent}")
            print("esse sistema é a base de linhas de codigo, digite help para mais informações ")
            running = 1

    # sistema principal
    while running == 1:

        comando = input("digite um comando")

        if (comando == "help"):
            historico.append(comando)
            print(f"duDOS {versão}  2024.")
            print("comandos disponiveis")
            print("date: mostra a data")
            print("time: mostra a hora")
            print("rand: gera números aleatorios")
            print("mult: mostra a tabuada de um número que é digitado pelo úsuario")
            print("msgd: troca a mensagem exibida na hora de desligar")
            print("hist: mostra o historico de comandos")
            print("name: troca o nome do usuario")
            print("exit: desliga o sistema")
            print("about: diz informações sobre o sistema")
            print("echo: repete uma palavra determinadas vezes")
            print("even: verifica se o número é par ou ímpar")
            print("guess: adivinhe um número com 5 chances")


        elif (comando == 'about'):
            historico.append(comando)
            print(f'duDOS {versão}')
            print(f'registrado para:{username}')
            print(f'ultima atualização{data_atualização}')
            print(f'Autor: Eduardo A ')
            print('descrição: duDOS é um sistema operacional basico feito em Python para um trabalho')
            print('email de contato:dudis8997@gmail.com')
            print('agradecimentos: meu professor BIG ROGER')

        # data

        elif (comando == 'date'):
            historico.append(comando)
            current_date = datetime.datetime.now().date()
            print(f"agora é {current_date}")

        # horario

        elif (comando == 'time'):
            historico.append(comando)
            current_time = datetime.datetime.now().time()
            round_time = current_time
            print(f"agora são {round_time}")

        # historico de comandos

        elif (comando == 'hist'):
            historico.append(comando)
            print(historico)

        # trocar o nome de usuario

        elif (comando == 'name'):
            historico.append(comando)
            username = input("digite o novo nome de usuario")
            print(f"nome mudado com sucesso para {username}")


        # número aleatorio

        elif (comando == 'rand'):
            historico.append(comando)
            random_number = random.randint(1, 1000)
            print(f"seu número é {random_number}")

        # tabuada

        elif (comando == 'mult'):
            historico.append(comando)

            tabuada = int(input("insira um número para checar a tabuada"))

            print(f"a tabuada do {tabuada}")

            for i in range(1, 11):
                resultado_tabuada = tabuada * i
                print(f"{tabuada} X {i} = {resultado_tabuada}")


        # desligar

        elif (comando == 'exit'):
            print(f"{mensagem_de_desligamento}...")
            running = 0
            break

        # trocar a mensagem de desligamento

        elif (comando == 'msgd'):
            historico.append(comando)
            mensagem_de_desligamento = input("qual mensagem deseja exibir ao desligar?")
            print(f"mensagem alterada com sucesso para {mensagem_de_desligamento}")

        elif (comando == 'even'):
            par = float(input("digite um numero para ver se é par ou ímpar"))

            if par % 3:
                print("esse número é par")
            else:
                print("esse número é ímpar")
            historico.append(comando)

        elif (comando == 'guess'):
            historico.append(comando)
            adivinhe = random.randint(1, 20)

            respostas = float(input("chute um número"))

            tentativas_guess = 0

            while respostas != adivinhe:
                if tentativas_guess == 5:
                    print(adivinhe)
                    break
                if adivinhe > respostas:
                    print("tente um número maior")
                    respostas = float(input("chute um número"))
                    tentativas_guess += 1

                else:
                    print("tente um número menor")
                    respostas = float(input("chute um número"))
                    tentativas_guess += 1

            else:
                print("você acertou!!!")

        elif (comando == 'cdown'):
            historico.append(comando)
            contagem = float(input("digite um número"))
            while contagem > -1:
                print(round(contagem))
                contagem -= 1


            else:
                print("fim")


        elif (comando == 'echo'):
            historico.append(comando)
            palavra = input("digite uma palavra")
            quantidade = float(input("quantas vezes?"))
            quantidade_de_palavras = 0

            while quantidade_de_palavras != quantidade:
                print(palavra)
                quantidade_de_palavras += 1


        elif (comando == 'clear'):

            decisao_apagar = input("deseja apagar todos os arquivos salvos?(S/N)")
            if (decisao_apagar == "S"):
                quantidade_de_arquivos = 0
                print("arquivos apagados com sucesso")

            elif (decisao_apagar == "n"):
                print("saindo...")


            else:
                print("comando não identificado")


        elif (comando == 'used'):
            print(f"{quantidade_de_arquivos} usado de {memoria1}")



        elif (comando == 'word'):
            historico.append(comando)
            print("intruções:")
            print("open: abre um arquivo salvo")
            print("new: cria um arquivo novo")
            print(f"{quantidade_de_arquivos} arquivo(s) usado(s) de {memoria1}")
            writting = 1

            while writting == 1:

                while quantidade_de_arquivos > memoria0:

                    print("memoria insuficiente")
                    print("saindo...")
                    writting = 0
                    break


                else:
                    modo = input("oque deseja fazer?")
                    if (modo == 'new'):
                        write = input()
                        salvar = input("salvar? (S/N)")
                        if (salvar == "S"):
                            salvos.insert(0, write)
                            quantidade_de_arquivos += 1
                        else:
                            print("arquivo apagado")


                    elif (modo == "open"):
                        print("arquivos salvos")
                        print(salvos)

                    elif (modo == 'exit'):
                        writting = 0
                        break

                    else:
                        print(f"comando não reconhecido {modo}")

        elif (comando == 'debug'):
            print(running, writting, quantidade_de_arquivos,salvos )











        else:
            print(f"{comando} não é um comando reconhecido pelo sistema")


    else:
        print("tentativas execedida")
        print(f"{mensagem_de_desligamento}...")


