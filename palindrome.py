def palindrome(v):
    reverse = v[::-1]
    if v==reverse:
        return True
    return False

mot = input("Entrer un mot : ")
if palindrome(mot):
    print("Ce mot un un palindrome")

else:
    print("Ce mot n'est pas un palindrome")

