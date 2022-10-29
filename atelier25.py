#Écrire un programme en Python qui demande à l’utilisateur de 
# saisir deux nombres a et b et de lui afficher leur somme : a + b

# demander à l'utilisateur de saisir les valeurs de a et de b
a = input("Tapez la valeur du nombre a : ")
b = input("Tapez la valeur du nombre b : ")
# Convertir les chaines de caractères en entier
a = int(a)
b = int(b)
s = a+b
print("La somme de a et de b est a + b = " , s)
