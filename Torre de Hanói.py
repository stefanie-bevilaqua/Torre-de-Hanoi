#_______________________Torre_de_Hanói__________________________
print("_______________________Torre_de_Hanói__________________________")
print("_"*63)
print("Para jogar basta inserir o número do pino que deseja retirar o disco do topo, e depois o número do pino que deseja colocar o disco")
print("_"*63)
#____________________Criando_as_Pilhas/Pinos____________________
pilha1 = []
pilha2 = []
pilha3 = []
mov = 0
#________________Escolhendo_o_número_de_discos__________________

escolha = int(input("Escolha o número de discos: "))
print("_"*63)
pilha1 = list(range(escolha, 0, -1))

#___Formatando_strings_para_deixar_o_jogo_mais_compreensível____

def imprime_pilhas():
    modelo = "{:^11}   {:^11}   {:^11}"
    for i in range(escolha, 0, -1):
        t1 = ""
        t2 = ""
        t3 = ""
        if len(pilha1) >= i:
            t1 = pilha1[i - 1]

        if len(pilha2) >= i:

            t2 = pilha2[i - 1]
        if len(pilha3) >= i:

            t3 = pilha3[i - 1]
        print(modelo.format(t1, t2, t3))

#_____________Entrada_de_dados_para_mover_os_discos__________________

while pilha3 != escolha:
    imprime_pilhas()
    print("_____=_____________=_____________=________")
    print ("Seu número de movimentos:",mov)
    qual = int(input("Digite o número do pino que deseja tirar o disco: "))
    onde = int(input("Digite para qual pino quer o mover: "))
    
#__________________Movimento_da_pilha_1_para_2-3_____________________

    if qual == 1:
        if (len(pilha1)) == 0:
            print ("Movimento inválido!")
        else:
            if onde == 2:
                if len(pilha2) == 0:
                    pilha2.append(pilha1.pop(-1))
                elif pilha2[-1] < pilha1[-1]:
                    print("Movimento inválido!")
                elif pilha2[-1] > pilha1[-1]:
                    pilha2.append(pilha1.pop(-1))

            elif onde == 3:
                if len(pilha3) == 0:
                    pilha3.append(pilha1.pop(-1))
                elif pilha3[-1] < pilha1[-1]:
                    print("Movimento inválido!")
                elif pilha3[-1] > pilha1[-1]:
                    pilha3.append(pilha1.pop(-1))

#_________________Movimento_da_pilha_2_para_a_1-3____________________

    elif qual == 2:
        if len(pilha2) == 0:
            print("Movimento inválido!")
        else:
            if onde == 1:
                if len(pilha1) == 0:
                    pilha1.append(pilha2.pop(-1))
                elif pilha1[-1] < pilha2[-1]:
                    print("Movimento inválido!")
                elif pilha1[-1] > pilha2[-1]:
                    pilha1.append(pilha2.pop(-1))

            elif onde == 3:
                if len(pilha3) == 0:
                    pilha3.append(pilha2.pop(-1))
                elif pilha3[-1] < pilha2[-1]:
                    print("Movimento inválido!")
                elif pilha3[-1] > pilha2[-1]:
                    pilha3.append(pilha2.pop(-1))

#________________Movimento_da_pilha_3_para_a_1-2______________________
                    
    elif qual == 3:
        if len(pilha3) == 0:
            print("Movimento inválido!")
        else:
            if onde == 1:
                if len(pilha1) == 0:
                    pilha1.append(pilha3.pop(-1))
                elif pilha1[-1] < pilha3[-1]:
                    print("Movimento inválido!")
                elif pilha1[-1] > pilha3[-1]:
                    pilha1.append(pilha3.pop(-1))

            elif onde == 2:
                if len(pilha2) == 0:
                    pilha2.append(pilha3.pop(-1))
                elif pilha2[-1] < pilha3[-1]:
                    print("Movimento inválido!")
                elif pilha2[-1] > pilha3[-1]:
                    pilha2.append(pilha3.pop(-1))

#___________________Verificando_se_teve_ganhador_______________________
    mov = mov+1
    
    if pilha3 == list(range(escolha, 0, -1)):
        print("***************************")
        print("*Parabéns, você ganhou! :D*")
        print("***************************")
        imprime_pilhas()
        print("_____=_____________=_____________=________")
        print ("Você executou ",mov," movimentos para ganhar!!!")
        break
