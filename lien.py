#!/usr/bin/python3

# Class permettant la composition du lien à chercher

class Lien():

    def __init__(self):
        self.date_jour = None
        self.date_semaine = None
        self.nb_page = 0
        self.lien_hebdo = "https://fr.tennistemple.com/pronostics/classement/"
        self.lien_jour = "https://fr.tennistemple.com/pronostics/classement/jour/"

    def add_nombre_de_page(self, nb):
        self.nb_page = nb

    def get_nb_page(self):
        return self.nb_page

    def add_date_journalier(self, date):
        self.date_jour = date

    def add_date_semaine(self, date):
        self.date_semaine = date

    def get_lien_journalier(self):
        return self.lien_jour + str(self.date_jour)

    def get_lien_hebdo(self):
        return self.lien_hebdo + str(self.date_semaine)

    def get_liens(self, type):
        tab = []
        if (str(type) == "J"):
            for i in range(int(self.nb_page)):
                tab.append(self.get_lien_journalier() + "/" + str(i + 1))
        if (str(type) == "H"):
            for i in range(int(self.nb_page)):
                tab.append(self.get_lien_hebdo() + "/" + str(i + 1))
        return (tab)
