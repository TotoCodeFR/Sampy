# https://youtube.com/@TotoCodeFR

print("Bienvenue")
print("Vous n'avez aucun nouveau message.")
print("1 : Nouveau message")
print("2 : Voir la corbeille")
print("3 : Ouvrir les paramètres")

def nouveau_message():
    pass

def corbeille():
    pass

def paramètres():
    pass

choix = int(input("Qu'est-ce que vous voulez faire?"))

# if choix == 1:
#     nouveau_message()
# elif choix == 2:
#     corbeille()
# elif choix == 3:
#     paramètres()
# else:
#     print("Choix incorrect!")


match choix:
    case 1:
        nouveau_message()
    case 2:
        corbeille()
    case 3:
        paramètres()
    case _:
        print("Choix incorrect!")