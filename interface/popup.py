__author__ = 'Cristi'
__date__ = "19 avril 2015"

from tkinter import *
from tictactoe.joueur import Joueur



class Popup():
    """
    Classe modélisant une fenêtre demandant a l'utilisateur de choisir le type
    de joueurs (deux personnes ou une personne et un ordinateur), le nom des
    personnes et le pion des joueurs (celui du deuxième est déduit).

    Attributes:
        infojoueurs (Information des joueurs): La liste des caractéristiques
                    des deux joueurs (initialement une liste vide), tel que
                    le type, le nom et le pion.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant la fenêtre.

        """

        super().__init__()
        # Création du widget principal parent :
        self.fen1 = Tk()
        #self.fen1.eval('tk::PlaceWindow %s center' % self.fen1.winfo_pathname(self.fen1.winfo_id()))
        self.fen1.title("Réglages des joueurs")

        self.var = IntVar()
        self.var_pion = IntVar()
        self.var_nom1 = StringVar()
        self.var_nom2 = StringVar()

        self.piona = ""
        self.pionb = ""

        # Buttons radio des choix du type de joueurs
        R1 = Radiobutton(self.fen1, text="Jouer contre un autre joueur", variable=self.var, value=2, command=self.name2)
        R1.grid(row=1, columnspan=2)

        R2 = Radiobutton(self.fen1, text="Jouer contre l'ordinateur", variable=self.var, value=1, command=self.name1)
        R2.grid(row=0, columnspan=2)

    def valider(self):
        """

        :return: joueur1.type, joueur1.nom, joueur1.pion,
                joueur2.type, joueur2.nom, joueur2.pion

        """

        if self.var_pion.get() == 1:
            self.piona = "X"
            self.pionb = "O"
        elif self.var_pion.get() == 2:
            self.piona = "O"
            self.pionb = "X"

        if self.var.get() == 1:
            self.fen1.destroy()
            (self.p1.type, self.p1.nom, self.p1.pion, self.p2.type, self.p2.nom, self.p2.pion) = \
                str('Personne'), str(self.var_nom1.get()), self.piona,\
                str('Ordinateur'), str("Colosse"), self.pionb
        elif self.var.get() == 2:
            self.fen1.destroy()
            (self.p1.type, self.p1.nom, self.p1.pion, self.p2.type, self.p2.nom, self.p2.pion) = \
                str('Personne'), str(self.var_nom1.get()), self.piona, \
                str('Personne'), str(self.var_nom2.get()), self.pionb


    def name1(self):
        """
            ! à completer

        """

        # Effacer la fenetre
        for widget in self.fen1.winfo_children():
            widget.destroy()

        # Etiqutte de qui demande d'enter le nom du 1er joueur
        l1 = Label(self.fen1, text='Nom du premier Joueur :')
        l1.grid(row=2, column=0)

        # Champ d'entrée du nom du 1er joueur
        entry1 = Entry(self.fen1, textvariable=self.var_nom1)
        entry1.grid(row=2, column=1)

        # Etiqutte de qui demande de choisir le pion du joueur 1
        l2 = Label(self.fen1, text='Pion du Joueur 1:')
        l2.grid(row=3, rowspan=2, column=0)

        # Bouttons radio pour choisir le pion du joueur 1
        rj1 = Radiobutton(self.fen1, text="X", variable=self.var_pion, value=1,)
        rj1.grid(row=4, column=1)
        rj2 = Radiobutton(self.fen1, text="O", variable=self.var_pion, value=2,)
        rj2.grid(row=5, column=1)

        # Boutton pour valider
        B1 = Button(self.fen1, text="Valider", command=self.valider)
        B1.grid(row=6, columnspan=2)


    def name2(self):
        """

            ! à completer

        """
        for widget in self.fen1.winfo_children():
            widget.destroy()

        # Etiqutte de qui demande d'enter le nom du 1er joueur
        l1 = Label(self.fen1, text='Nom du premier Joueur :')
        l1.grid(row=2, column=0)

        # Champ d'entrée du nom du 1er joueur
        entry1 = Entry(self.fen1, textvariable=self.var_nom1)
        entry1.grid(row=2, column=1)

        # Etiqutte de qui demande d'enter le nom du 2e joueur
        l2 = Label(self.fen1, text='Nom du deuxième Joueur :')
        l2.grid(row=3, column=0)

        # Champs d'entrée du nom du 1er joueur
        entry2 = Entry(self.fen1, textvariable=self.var_nom2)
        entry2.grid(row=3, column=1)

        # Etiqutte de qui demande de choisir le pion du joueur 1
        l3 = Label(self.fen1, text='Pion du Joueur 1:')
        l3.grid(row=4, rowspan=2, column=0)

        # Bouttons radio pour choisir le pion du joueur 1
        rj1 = Radiobutton(self.fen1, text="X", variable=self.var_pion, value=1,)
        rj1.grid(row=4, column=1)
        rj2 = Radiobutton(self.fen1, text="O", variable=self.var_pion, value=2,)
        rj2.grid(row=5, column=1)


        B1 = Button(self.fen1, text="Valider", command=self.valider)
        B1.grid(row=6, columnspan=2)