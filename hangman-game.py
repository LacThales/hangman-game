print("Bem-Vindo ao Jogo da Forca")
print("|----- ")
print("|    | ")
print("|    O ")
print("|   /|\\ ")
print("|    | ")
print("|   / \\ ")
print()

p_secret = input("Digite uma palavra secreta: ")
l_sorte = [] #lista vazia para as letras que serao testadas

for x in range(0, len(p_secret)):
    l_sorte.append('_') #vai adicionar todas as letras de p_secret em l_sorte como '_'
    print(l_sorte[-1], end=' ') #vai printar a palavra secreta, mas com o '_'
    print('\n') #apenas para estética, pular linha
game_on = True # -- booleana

while game_on == True:
    l_digitar = input("\nDigite uma letra: ")

    for indice in range(0, len(p_secret)):
        if l_digitar == p_secret[indice]: # se o que a pessoa digitou estiver em algum indice da palavra secreta(ou seja o '_') vai mudar para uma letra.
            l_sorte[indice] = l_digitar
        print(l_sorte[indice])
    game_on = False #se acertou tudo, ficará False, caso contrário, continuará no loop.

    #-----------------------------------------//----------------------------------------
    #verificar se já foi descoberto todas as palavras:
    for indice_2 in range (0, len(l_sorte)):
        if l_sorte[indice_2] == '_':
            game_on = True

print("\n", "******* Acabou o jogo, você conseguiu! ********")
