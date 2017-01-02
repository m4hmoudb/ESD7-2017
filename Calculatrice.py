#@ 01/02/2017
#@ Mahmoud
#########################################
operation = 0
nombre1 = 0
nombre2 = 0

print("Basic Calcul Mahmoud")
print("---------------------")
print("Veuillez choisir l'operation :")
print("1-Addition")
print("2-Soustraction")
print("3-Multiplication")
print("4-devision")

operation = input()
nombre1 = input ("entrer la valeur du premier nombre :")
nombre2 = input ("entrer la valeur du deuxieme nombre :")

if (operation == 1):
        print (nombre1 + nombre2)
elif operation == 2:
        print (nombre1 - nombre2)
elif operation == 3:
        print (nombre1 * nombre2)
elif operation == 4:
        print (nombre1 / nombre2)
