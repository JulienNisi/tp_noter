import random

def entre0N(nbr):
    return random.randint(0, nbr)

def elementAuHasard(liste):
    return liste[entre0N(len(liste) - 1)]

def listeZeros(nbr):
    liste = []

    for i in range(nbr):
        liste += [0]
    return liste

def plateauZeros(lignes, colonnes):
    liste = []
    liste_tempo = []

    for y in range(lignes):
        for x in range(colonnes):
            liste_tempo += [0]
        liste += [liste_tempo]
        liste_tempo = []
    return liste

#---------------------------------------------------------------------------------#
def voisines_PI(cell):
    return ( (cell[0], cell[1] - 1), (cell[0], cell[1] + 1), (cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0] - 1, cell[1] - 1), (cell[0] - 1, cell[1] + 1), (cell[0] + 1, cell[1] - 1), (cell[0] + 1, cell[1] + 1))

def voisine_PI_alea(cell):
    return elementAuHasard(voisines_PI(cell))
    
def afficheParcoursNpas_PI(nbr, cell):
    for i in range(nbr):
        print(cell, end=" ")
        cell = voisine_PI_alea(cell)
    print(cell, end="")

#---------------------------------------------------------------------------------#

def estSurPlateau(cell, lignes, colonnes):
    voisin = voisines_PI(cell)
    new_voisin = []

    for y in range(len(voisin)):
        if (voisin[y][0] < 0) or (voisin[y][1] < 0) or (voisin[y][0] > lignes) or (voisin[y][1] > colonnes):
            pass
        else:
            new_voisin += [voisin[y]]
    return new_voisin

def parcoursNbPas_PF(cell, lignes, colonnes, nbr):
    voisin = []

    for i in range(nbr):
        print(cell)
        voisin = estSurPlateau(cell, lignes, colonnes)
        cell = elementAuHasard(voisin)

    print(cell)
    
def voisines_libres(cell, obstacle):
    voisin = estSurPlateau(cell, len(obstacle) - 1, len(obstacle[0]) - 1)
    new_voisin = []

    for y in range(len(voisin)):
        if (obstacle[voisin[y][0]][voisin[y][1]] != 1):
            new_voisin += [voisin[y]]

    return new_voisin

def voisine_libre_alea(cell, obstacle):
    if voisines_libres(cell, obstacle) == []:
        return None
    return elementAuHasard(voisines_libres(cell, obstacle))

def parcours_obst(cell, obstacle, nbr):
    voisin = []

    for i in range(nbr):
        print(cell, end=" ")
        cell = voisine_libre_alea(cell, obstacle)
        if (cell == None):
            return None
    print(cell, end="")

def serpant(cell, obstacle):
    if voisine_libre_alea(cell, obstacle) == None:
        print(cell)
        return 0
    print(cell)
    obstacle[cell[0]][cell[1]] = 1
    serpant(voisine_libre_alea(cell, obstacle), obstacle)

if __name__ == '__main__':
    obstacle = plateauZeros(7, 7)
    for y in range(len(obstacle)):
        for x in range(len(obstacle[0])):
            if (random.random() <= 0.40):
                obstacle[y][x] = 1
    #parcours_obst((6,6), obstacle, 5)
    serpant((6, 6), obstacle)