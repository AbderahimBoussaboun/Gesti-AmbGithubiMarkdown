

numero = int(input("Introdueix un valor enter entre 0 i 20: "))
while numero <= 0 or numero >= 20:
    numero = int(input("ERROR El valor ha d'estar comprès entre 0 i 20: "))

i = 1
factorial = 1
numeroF = 0
while i < numero:
    resultat = factorial*(i+1)
    factorial = +resultat
    i = i+1

print("El factorial de ", numero, " és ", resultat)
