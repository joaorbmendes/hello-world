from random import shuffle
codigo = list(range(1, 10))
codigox = shuffle(codigo)
secreto = str(codigo[0]) + str(codigo[1]) + str(codigo[2]) + str(codigo[3])
secreto = str(secreto)
cont = 0
winner = 0

while cont < 11 or winner < 1:
    num = input("Adivinha os 4 numeros:")
    num = str(num)
    cont = cont + 1
    if num[0] == secreto[0]:
        print ("verde")
    if num[1] == secreto[1]:
        print ("verde")
    if num[2] == secreto[2]:
        print ("verde")
    if num[3] == secreto[3]:
        print ("verde")


    if (num[0] == secreto[1] or num[0] == secreto[2] or num[0] == secreto[3]):
        print ("amarelo")
    if (num[1] == secreto[0] or num[1] == secreto[2] or num[1] == secreto[3]):
        print ("amarelo")
    if (num[2] == secreto[1] or num[2] == secreto[0] or num[2] == secreto[3]):
        print ("amarelo")
    if (num[3] == secreto[1] or num[3] == secreto[2] or num[3] == secreto[0]):
        print ("amarelo")

    if cont > 10:
        print "Perdeste!"
        break        

    print "Restam " + str(10 - cont) + " tentativas"
    if (num[0] == secreto[0] and num[1] == secreto[1] and num[2] == secreto[2] and num[3] == secreto[3]):
        winner = 1;
        print ("Ganhaste!!")
        break

