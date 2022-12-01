# def imprime_menor(a, b):
#     if a < b:
#       print(a)
#     elif a > b:
#       print(b)
#     else:
#       print("Os números são iguais.")

# imprime_menor(0, 5)
# imprime_menor(10, 3)
# imprime_menor(42, 42)

# Escreva uma função que, dado um número nota representando a nota de um estudante,
#  converte o valor de nota para um conceito (A, B, C, D, E e F).

# Função (receber um numero)
# Nota 0 a 10

# A -  >= 9.5 (maior ou igual a 9 e meio)
# B - > 8.5 < 9.5 (maior doque 8 e meio & menor doque 9 e meio)
# C - > 7.5 < 8.5 (maior doque 7 e meio & menor doque 8 e meio)
# D - > 6.5 < 7.5 (maior doque 6 e meio & menor doque 7 e meio)
# E - >= 5 < 6.5 (maior ou igual doque 5 e meio & menor doque 6 e meio)

def notas (nota):

 if nota >= 9.5: 
    print ("A")
 elif nota > 8.5 & nota < 9.5:
    print ("B")
 elif nota > 7.5 & nota < 8.5:
    print ("C") 
 elif nota > 6.5 & nota < 7.5:
    print ("D")
 elif nota > 5 & nota < 6.5:
    print ("E")
 else:
    print ("F")



