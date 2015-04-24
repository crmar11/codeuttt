__author__ = 'Ibrahim Kamara et Cristi Margineanu'
__date__ = "24 avril 2015"

"""Ce fichier représente le point d'entrée principal du TP3.
Il ne sert qu'à exécuter votre programme du jeu Ultimate Tic-Tac-Toe.
Il permet aussi de centrer la fenetre de jeu principale par rapport à l'ecran d'ordinateur
"""

from interface.jeu_utictactoe import Fenetre

if __name__ == '__main__':

    ma_fenetre = Fenetre()
    # Ouverture de la fenetre principale du jeu  au centre de celle de l'ordinateure
    #Fait à partir des paramètres de 1366 x768
    ma_fenetre.geometry("692x689+300+10") #  dimension et position par defaut
    ma_fenetre.minsize(400, 300) # taille minimum de la fenetre
    ma_fenetre.maxsize(689,692) # taille maximum de la fenetre
    ma_fenetre.mainloop()