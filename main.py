#!/usr/bin/python3

from bs4 import BeautifulSoup  # import de bs4.BeautifulSoup
from urllib import request  # import de urllib.request
from lien import Lien


def main():  # fonction principale

    tab = scenario()
    manuel = input("Saisir manuellement les personnes (y or n)\n")
    if (manuel == "y"):
        recherche_manuel(tab)
    if (manuel == "n"):
        recherche_automatique(tab)


def recherche_manuel(tab):
    personne_check = "Debut"
    while (personne_check != "Fin"):
        valfin = -1
        personne_check = input("Saisir la personne rechercher (Mettre Fin pour quitter)\n")
        if personne_check != "Fin":
            for i in range(0, int(len(tab))):
                if valfin != 1:
                    soup = get_parsed_page(tab[i])
                    valfin = print_post_personnes(soup, personne_check)

def recherche_automatique(tab):
    fichier = open("data.txt", "r")
    for ligne in fichier:
        valfin = -1
        field = ligne.split(",")

        personne_check = field[0]

        for i in range(0, int(len(tab))):
            if valfin != 1:
                soup = get_parsed_page(tab[i])
                valfin = print_post_personnes(soup, personne_check)
    fichier.close()


def get_parsed_page(url):  # fonction qui retourne une page parsée à partir d'une url
    with request.urlopen(url) as page:
        html = page.read()
    return BeautifulSoup(html, 'html.parser')  # parse la page avec BeautifulSoup


def print_post_personnes(soup, personne_check):
    points = soup.find_all('div', class_='points')
    personnes = soup.find_all('div', class_='name')
    pourcentage = soup.find_all('div', class_='percent')

    if (len(personnes) != 1):
        for i in range(0, len(personnes)):
            if (personnes[i].getText().strip().upper() != '' and personnes[
                i].getText().strip().upper() == personne_check.upper()):
                fichieres = open("datares.csv", "a")
                print(personnes[i].getText().strip() + " : " + points[i].getText().strip() + " " + pourcentage[
                    i].getText().strip())
                fichieres.write(personnes[i].getText().strip() + "," + points[i].getText().strip() + "," + pourcentage[
                    i].getText().strip() + "\n")
                fichieres.close()
                return 1
    return 0


def scenario():
    type = input("Saisir J pour le score journalier/H pour le score hebdo (J par défaut)\n")
    lien = Lien()
    if (type == "H"):
        semaine = input("Saisir la date (Format MM-AAAA)\n")
        nb = input("Saisir le nombre de page dans l'hebdo\n")
        lien.add_nombre_de_page(nb)
        lien.add_date_semaine(semaine)
    else:
        jour = input("Saisir la date (Format AAAA-MM-JJ)\n")
        nb = input("Saisir le nombre de page dans le journalier\n")
        lien.add_nombre_de_page(nb)
        lien.add_date_journalier(jour)
    return lien.get_liens(type)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
