#parte para adicionar imports
import datetime
import random

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()

random_number = random.randint(1,1000)



#tela de login ;)
usuario_correto = "admin"

senha_correta = "admin"

numero_de_tent1 = 0
numero_de_tent2 = 0

usuario_tent = str(input("digite usuario"))



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



while running == 1:

           comando = input("digite um comando")

           if (comando == "help"):
               print("duDOS versão alpha v0.0.2 2024.")
               print("comandos disponiveis")
               print("Calc: calculadora basica")
               print("date: mostra a data")
               print("time: mostra a hora")
               print("rand: gera números aleatorios")
               print("mult: mostra a tabuada de um número que é digitado pelo úsuario")

           #calculadora ultra basica

           elif (comando == "calc"):

               primeiro_número = float(input("digite o primeiro número"))

               operador = input("digite uma equação(+,-)")

               segundo_número = float(input("digite o segundo número"))

               if operador == '+':
                   resultado = primeiro_número + segundo_número

               elif operador == '-':
                   resultado = primeiro_número - segundo_número


               print(f"seu resultado é {resultado}")


           #data

           elif (comando == 'date'):
               print(f"agora é {current_date}")

           #horario

           elif (comando == 'time'):
               print(f"agora são {current_time}")

           #número aleatorio

           elif (comando == 'rand'):
               print(f"seu número é {random_number}")

           #tabuada

           elif (comando == 'mult'):

               tabuada = int(input("insira um número para checar a tabuada"))

               print(f"a tabuada do {tabuada}")

               for i in range(1,11):
                   resultado_tabuada = tabuada * i
                   print(f"{tabuada} X {i} = {resultado_tabuada}")

          #desligar

           elif (comando == 'exit'):
               print("desligando...")
               break

           else:
               print(f"{comando} não é um comando reconhecido pelo sistema")








