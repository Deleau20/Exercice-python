# Ecrire une fonction qui prend en parametre un tableau qui
# retourne un autre tableau contenent le carré des nombre entrée.

def carre(num):
    return num**2  

nombre =[1, 2, 3, 4]
for item in map(carre, nombre):
    list(map(carre,nombre))
    print(item)

    


