liste = ["a","b","c","d","e"]

mot = input("Saisissez la lettre : ")

chaine = str()

def test(chaine,mot):
    if chaine ==mot:
        print("Vous avez trouvé")


for l in liste:
    chaine = l
    test(chaine,mot)
    