#!/usr/bin/python3

from bs4 import BeautifulSoup  # import de bs4.BeautifulSoup
from urllib import request  # import de urllib.request


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

    def add_date_jouralier(self, date):
        self.date_jour = date

    def add_date_semaine(self, date):
        self.date_semaine = date

    def get_lien_journalier(self):
        return self.lien_jour + str(self.date_jour)

    def get_lien_hebdo(self):
        return self.lien_hebdo + str(self.date_semaine)

    def get_liens(self, type):
        tab = []
        if (type == "J"):
            for i in range(self.nb_page):
                tab.append(self.recuperation_lien_journalier() + "/" + str(i + 1))
        if (type == "H"):
            for i in range(self.nb_page):
                tab.append(self.recuperation_lien_hebdo() + "/" + str(i + 1))
        return (tab)
