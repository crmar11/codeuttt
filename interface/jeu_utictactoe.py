__authors__ = "Cristi Margineanu et Ibrahim Kamara"
__date__ = "19 avril 2015"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from tkinter import Tk, Canvas, Label, Frame, GROOVE, messagebox, Button
from tictactoe.partie import Partie
from tictactoe.joueur import Joueur
from _datetime import time

class ErreurCase(Exception):
    pass

class CanvasPlateau(Canvas):
    """
        À completer !.
    """

    def __init__(self, parent, plateau, taille_case=60):

        # Une instance d'un des 9 plateaux du jeu ultimate Tic-Tac-Toe.
        self.plateau = plateau

        # Nombre de pixels par case.
        self.taille_case = taille_case

        # Appel du constructeur de la classe de base (Canvas).
        super().__init__(parent, width=self.plateau.n_lignes * taille_case,
                         height=self.plateau.n_colonnes * self.taille_case)

        # Dessiner le plateau du jeu ultimate Tic-Tac-Toe.
        self.dessiner_plateau()


    def dessiner_plateau(self):
        """
            À completer !.
        """
        for i in range(self.plateau.n_lignes):
            for j in range(self.plateau.n_colonnes):
                debut_ligne = i * self.taille_case
                fin_ligne = debut_ligne + self.taille_case
                debut_colonne = j * self.taille_case
                fin_colonne = debut_colonne + self.taille_case
                # On dessine le rectangle représentant une case!
                self.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne,
                                      fill='#e1e1e1', width=2, outline="white")


class Fenetre(Tk):
    """
        À completer !.
    """

    def __init__(self):
        """
            À completer !.
        """
        super().__init__()

        # Nom de la fenêtre.
        self.title("Ultimate Tic-Tac-Toe")

        # La partie de ultimate Tic-Tac-Toe
        self.partie = Partie()

        # Un ditionnaire contenant les 9 canvas des 9 plateaux du jeu
        self.canvas_uplateau = {}

        # Création des frames et des canvas du jeu
        for i in range(0, 3):
            for j in range(0, 3):
                cadre = Frame(self, borderwidth=5, relief=GROOVE, background = '#e1e1e1')
                cadre.grid(row=i, column=j, padx=5, pady=5)
                cadre.columnconfigure(0, weight=1)
                cadre.rowconfigure(0, weight=1)
                cadre.columnconfigure(1, weight=1)
                cadre.rowconfigure(1, weight=1)
                cadre.columnconfigure(2, weight=1)
                cadre.rowconfigure(2, weight=1)
                #cadre.columnconfigure(j, weight=1)
                #cadre.rowconfigure(i, weight=1)

                #Dessiner le cadre en jaune si la sourie entre dans le cadre
                cadre.bind('<Enter>', self.entrer_frame)
                cadre.bind('<Leave>', self.sortir_frame)

                self.canvas_uplateau[i, j] = CanvasPlateau(cadre, self.partie.uplateau[i, j])
                self.canvas_uplateau[i, j].grid()
                self.canvas_uplateau[i, j].columnconfigure(0, weight=1)
                self.canvas_uplateau[i, j].rowconfigure(0, weight=1)
                self.canvas_uplateau[i, j].columnconfigure(1, weight=1)
                self.canvas_uplateau[i, j].rowconfigure(1, weight=1)
                self.canvas_uplateau[i, j].columnconfigure(2, weight=1)
                self.canvas_uplateau[i, j].rowconfigure(2, weight=1)
                # On lie un clic sur le Canvas à une méthode.
                self.canvas_uplateau[i, j].bind('<Button-1>', self.selectionner)


        #Pour redimensionner automatiquement la fenêtre principale

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid(columnspan=3)
        # Ajout d'une étiquette pour le nom des joueurs.
        self.Noms = Label(self)
        self.Noms.grid(column=4, row=0, rowspan=2)
        # Ajout d'une étoquette pour la date et le chronometre.
        self.Date = Label(self)
        self.Date.grid(column=4, row=1, columnspan=2)

        # Création de deux joueurs.
        self.JoueursDuJeux()

        # Les bouttons en dessous
        B1 = Button(self, text='Règles', width=12, command=self.regles).grid(row=5,column=0)
        B2 = Button(self, text='Recommancer', width=12, command=self.recommancer).grid(row=5, column=1)
        B3 = Button(self, text='Statistiques', width=12, command=self.regles).grid(row=5, column=2)
        B4 = Button(self, text='Historique', width=12, command=self.regles).grid(row=6, column=1)
        B5 = Button(self, text='Quitter', width=5, command=self.quitter).grid(row=6, column=2)
        B5 = Button(self, text='Rien', width=12, command=self.regles).grid(row=6, column=0)

    #def DateEtChrono(self):
    #    print(str(time.tzinfo))

    def JoueursDuJeux(self):

        p1 = Joueur("VotreNom", "Personne", 'X')
        p2 = Joueur("Colosse", "Ordinateur", 'O')

        # MessageBox pour savoir si le deuxieme joueur est une personne ou un ordinateur
        p2Type = messagebox.askyesno("Type de joueur", "Jouez-vous avec un deuxième joueur ? \nSi non l'ordinateur Colosse le remplacera.")

        if p2Type == True:
            p2.type = "Personne"
        else:
            p2.type = "Ordinateur"

        self.partie.joueurs = [p1, p2]
        self.partie.joueur_courant = p1

    def quitter(self):
        quitter_r = messagebox.askyesno("Fermer ?", message="Voullez vous vraiment quitter?",)
        if quitter_r == True:
            self.quit()

    def recommancer(self):
        """
            Permet d'effacer le dictionnaire des 9 plateau et d'effacer
            les tags 'pion' de chaque canvas, pour ainsi recommancer le jeux.
        """
        for i in range(0, 3):
            for j in range(0, 3):
                self.partie.uplateau[i, j].initialiser()
                self.canvas_uplateau[i, j].delete('pion')
                self.afficher_message("")

    def regles(self):
        """
            Permet de faire apparaitre une MessageBox avec les règles.
        """
        messagebox.showinfo('Règles du jeux', reglesdujeux)

    def selectionner(self, event):
        """
            À completer !.
        """
        try:
            # On trouve le numéro de ligne/colonne en divisant par le nombre de pixels par case.
            # event.widget représente ici un des 9 canvas !
            ligne = event.y // event.widget.taille_case
            colonne = event.x // event.widget.taille_case

            # On verifie si la case est gagnante
            if self.partie.uplateau[event.widget.plateau.cordonnees_parent].est_gagnant("X")\
                    or self.partie.uplateau[event.widget.plateau.cordonnees_parent].est_gagnant("O"):
                raise ErreurCase("Le plateau est déja gagnant")

            # On verifie si la case clicé est vide
            if not self.partie.uplateau[event.widget.plateau.cordonnees_parent].cases[ligne, colonne].est_vide():
                raise ErreurCase("La case est déjà prise !")

            # On verifie si la position est valide
            if not self.partie.uplateau[event.widget.plateau.cordonnees_parent].position_valide(ligne, colonne):
                raise ErreurCase("La position n'est pas valide !")

            # On verifie si on clic dans la bonne prochaine case
            if not self.partie.uplateau[event.widget.plateau.cordonnees_parent].position_valide(ligne, colonne):
                raise ErreurCase("Ce tour doit être joué dans la case en rouge !")


            self.afficher_message("Case sélectionnée à la position (({},{}),({},{}))."
                                  .format(event.widget.plateau.cordonnees_parent[0],
                                          event.widget.plateau.cordonnees_parent[1],
                                          ligne, colonne))

            # On dessine le pion dans le canvas, au centre de la case.
            # On utilise l'attribut "tags" pour être en mesure de récupérer
            # les éléments dans le canvas afin de les effacer par exemple.
            coordonnee_y = ligne * event.widget.taille_case + event.widget.taille_case // 2
            coordonnee_x = colonne * event.widget.taille_case + event.widget.taille_case // 2
            event.widget.create_text(coordonnee_x, coordonnee_y, text=self.partie.joueur_courant.pion,
                                     font=('Helvetica', event.widget.taille_case // 2), tags='pion')

            # Mettre à jour la case sélectionnée
            self.partie.uplateau[event.widget.plateau.cordonnees_parent] \
                .selectionner_case(ligne, colonne, self.partie.joueur_courant.pion)

            # Changer le joueur courant.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if self.partie.joueur_courant == self.partie.joueurs[0]:
                self.partie.joueur_courant = self.partie.joueurs[1]
            else:
                self.partie.joueur_courant = self.partie.joueurs[0]

            # Effacer le contenu du widget (canvas) et du plateau (dictionnaire) quand ce dernier devient plein.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if not event.widget.plateau.non_plein() and not event.widget.plateau.est_gagnant("X") \
                    and not event.widget.plateau.est_gagnant("O"):
                event.widget.delete('pion')
                event.widget.plateau.initialiser()
                # Afficher label de partie nule
                self.afficher_message("Partie nule dans la case({},{})."
                                  .format(event.widget.plateau.cordonnees_parent[0],
                                          event.widget.plateau.cordonnees_parent[1]))

                # Augmenter le nombre de parties nules de 1
                self.partie.nb_parties_nulles += 1

        except ErreurCase as e:
            self.afficher_message(str(e), color='red')

    def afficher_message(self, message, color='black'):
        """
            Permet d'afficher un message (en bas de page)
        """
        self.messages['foreground'] = color
        self.messages['text'] = message

    def entrer_frame(self, event):
        event.widget['background'] = 'yellow'
    def sortir_frame(self, event):
        event.widget['background'] = '#e1e1e1'




# Regles du jeux en chaine de caractères
reglesdujeux = (str("Règles du jeu:\
    \n1. Le premier joueur peut faire un pas dans n'importe quelle cellule.\
    \n\n2. La position de la cellule sélectionnée au sein de ce mini carré correspond \
à la position mini-carré sein de la grande place, où le second joueur doit alors placer un «O». \
    \n\n3. Par la suite, les deux joueurs se relaient placer leur marque dans n'importe quelle cellule \
vacants au sein de la mini-carré dictée par la position de la cellule marquée par le joueur précédent.\
    \n\n4. Le premier gagnant de tic-tac-toe dans un carré mini-demeure le gagnant dans cette mini-carré pour \
le reste de la partie.\
    \n\n5. Si un joueur est envoyé à un mini carré qui a déjà été gagné, ou dans lesquels toutes les cellules\
sont déjà remplies, alors le joueur peut ensuite placer sa marque dans n'importe quelle cellule \
inoccupé dans un autre carré mini. \n\n source: \n \
https://itunes.apple.com/fr/app/ultime-tic-tac-toe-hd-jeu/id672190466?mt=8"))

