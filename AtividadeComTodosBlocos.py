'''
3 Blocos
v1 -> t3
v2 -> t2
v1 -> t2
v3 -> t3
v1 -> t1
v2 -> t3
v1 -> t3
=-=--=-=-
4 Blocos
v1 -> t3 0      1
v2 -> t2 1      2
v1 -> t2 2      3
v3 -> t3 3  8      4 %% 
v1 -> t1 4      5
v2 -> t3 5       6
v1 -> t3 6      7
v4 -> t2 7      8 %%%
v1 -> t2 8      9
v2 -> t1 9      10
v1 -> t1 10     11
v3 -> t2 11 16    12  %%%
v1 -> t3 12     13 
v2 -> t2 13     14
v1 -> t2 14     15
                            Potencial_v5    15     16
'''


#3 Blocos
#v1 -> t3
#v2 -> t2
#v1 -> t2
#v3 -> t3
#v1 -> t1
#v2 -> t3
#v1 -> t3
# Fazer com que input (2^n) - 1
print("As opções são 1, 2, 3, 4, 5, 6 e 7")
blocos = 0
while blocos > 7 or blocos < 1:
    blocos = int(input("Digite quantos blocos são: "))
    if blocos > 7 or blocos < 1:
        print("Opção Inválida, tente novamente!")

passos = (2**blocos) - 1
#cont = 0
v1 = 3 # Primeiro movimento do Bloco 1
v2 = 2 # Primeiro movimento do Bloco 2
v3 = 3 # Primeiro movimento do Bloco 3
v4 = 2 # Primeiro movimento do Bloco 4
v5 = 3 # Talvez?
v6 = 2
v7 = 3
for c in range(0,passos):
    #print(f"{c}")
    #print(f"{c}" ,end=' ' )

    if c % 2 == 0:  
        print(f"Bloco 1 -> Torre {v1}")
        v1 = v1 - 1
        if v1 == 0:
            v1 = 3


    if (c - 1) % 4 == 0:
        print(f"Bloco 2 -> Torre {v2}")
        v2 = v2 + 1
        if v2 == 4:
            v2 = 1


    if (c + 5) % 8 == 0:
        print(f"Bloco 3 -> Torre {v3}")
        v3 = v3 - 1
        if v3 == 0:
            v3 = 3


    if (c + 2) % 9 == 0 and c != 16 and c != 25 and c != 34 and c != 43 and c != 52 and c != 61 and c!= 70 and c != 79 and c != 88 and c != 97 and c != 106 and c != 115 and c != 124: 
        print(f"Bloco 4 -> Torre {v4}")
        v4 = v4 + 1
        if v4 == 4:
            v4 = 1


    if  c == 23 or c == 39 or c == 55 or c == 71 or c == 87 or c == 103 or c == 119:
        print(f"Bloco 4 -> Torre {v4}")
        v4 = v4 + 1
        if v4 == 4:
            v4 = 1



    if (c + 5) % 20 == 0 and c != 35 and c != 55 and c != 75 and c != 95 and c != 115:
        print(f"Bloco 5 -> Torre {v5}")
        v5 = v5 - 1
        if v5 == 0:
            v5 = 3

    if c == 47 or c == 79 or c == 111:
        print(f"Bloco 5 -> Torre {v5}")
        v5 = v5 - 1
        if v5 == 0:
            v5 = 3


    if (c + 1) % 32 == 0 and c != 63:
        print(f"Bloco 6 -> Torre {v6}")
        v6 = v6 + 1
        if v6 == 4:
            v6 = 1


    if c % 63 == 0 and c != 0 and c != 126:
        print(f"Bloco 7 -> Torre {v7}")
        v7 = v7 - 1
        if v7 == 0:
            v7 = 3
    

    #cont += 1
    

