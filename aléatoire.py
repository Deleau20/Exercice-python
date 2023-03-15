import random

def randomword():
    tab = ["bonjour", "salut", "bonsoir"]
    return random.choice(tab)




if __name__ == '__main__':
    nombrechance = 3
    flag = False
    stargame = True
    mot = randomword()
    motcache = ["*"]*len(mot)
    print("".join(motcache))


    

    while stargame:

        car = input("\nEntrez un caractère : ")

        for i in range(len(mot)):
            if mot[i] == car:
              motcache[i] = car
                    

        if flag:
            flag = False
            print("Bingo !!!") 
        else:    
            nombrechance -= 1
            if nombrechance <= 0:
                print("Vous n'avez plus de chance")
                stargame = False
            else:
                print(f"Vous n'avez pas trouvé le caractère il vous reste {nombrechance}")

        output = "".join(motcache)
        print(output)
        if output == mot:
            stargame = False
        


    #     if mot.count(car) > 1:
    #         print("\nLe caractère est présent plusieurs fois dans le mot.")
    #     else:
    #         print("\nLe caractère se trouve à la position", mot.count(car)+1, "dans le mot.")
    # else:
    #     print("\nLe caractère n'est pas présent dans le mot.")
