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
v1 -> t3
v2 -> t2
v1 -> t2
v3 -> t3 
v1 -> t1
v2 -> t3
v1 -> t3
v4 -> t2 8
v1 -> t2
v2 -> t1
v1 -> t1
v3 -> t2 
v1 -> t3
v2 -> t2
v1 -> t2
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

blocos = 3 #int(input("Digite quantos blocos são: "))
passos = (2**blocos) - 1
#cont = 0
v1 = 3 # Primeiro movimento do Bloco 1
v2 = 2 # Primeiro movimento do Bloco 2
v3 = 3 # Primeiro movimento do Bloco 3

for c in range(0,passos):
    if c % 2 == 0:
        print(c) 
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
    #cont += 1
    

