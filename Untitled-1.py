# class array():
#     items = []
#     def __init__(self, *args):
#         for item in args:
#             self.items.append(item)
#     def at(self, index):
#         if index > self.at:
#           return  none

class Player():

    def __init__ (self,nom,point_de_vie,point_attaque,arme):
        if type(nom) is not str:
            raise TypeError("Entrer une chaine de caractère pour le nom ")
        if type(point_de_vie) is not int:
            raise TypeError("Entrer un nombre")
        if type(point_attaque) is not int:
            raise TypeError("Entrer un  nombre")
        if type(arme) is not Weapon:
            raise TypeError("L'arme n'est pas une arme Abaigraiiii")
        self.nom = nom
        self.arme = arme
        self.point_de_vie = point_de_vie
        self.point_attaque = point_attaque

    def presenter(self):
        print(f"Joueur : {self.nom}\nPoint de vie : {self.point_de_vie}\nPoint d'attaque : {self.point_attaque}\nLe type de l'arme choisi est : {self.arme.type_de_arme}")
    def faceToFace(self,joueur2):
        joueur2.point_de_vie -= 1
        print(f"J'attaque : {joueur2.nom}\n il lui reste : {joueur2.point_de_vie}")



class Weapon():

    def __init__ (self,nom,degats,type_a):
        self.type_de_arme = type_a
        self.nomArme = nom
        self.degatsDeArme = degats
    
    def presenteArme(self):
        print(f"Le nom de l'arme est : {self.nomArme}\nDegats de l'arme est : {self.degatsDeArme}")

    def attaquer():
        pass


arme1 = Weapon("couteau",5,"raproché")
jeu = Player("fred",5,3,arme1)
jean = Player("AZERTY",4,5,arme1)

jeu.presenter()
jean.presenter()

    











# joueur = Player("fred",10,5)
# joueur2 = Player("Josias",8,3)

# print(joueur.presenter())
# print(joueur2.attaque())

# def add(a,b):
#     resultat = a+b
#     print(resultat)

# add(2,5)

# def inverse(tab, tailleTableau, i1, i2):
#     if i1 >tailleTableau or i2 > tailleTableau:
#         return -1
#     else:
#         tab[i1], tab[i2] = tab[i2], tab[i1]
#         return tab



# def inverse(tab, taille, i, j):
#     if i >= taille or j >= taille:
#         return -1 # indices invalides
#     else:
#         tab[i], tab[j] = tab[j], tab[i] # échange des éléments
#         return tab











          



          

    

