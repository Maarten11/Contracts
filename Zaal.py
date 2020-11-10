from copy import deepcopy

class Zaal:
    def __init__(self, nummer, plaatsen):
        self.zaalNummer = nummer
        self.plaatsen = plaatsen

    # Contract voor Zaal

    def add_zaal(self, nummer, plaatsen):
        """
        Functie: add_zaal
        Beschrijving: voegt een nieuwe zaal toe
        Input Parameters:
        :param nummer: nummer van de zaal
        :param plaatsen: aantal plaatsen in de zaal
        PreCondities:
            nummer: > 0, uniek en mag niet leeg gelaten worden
            plaatsen: positief getal en mag niet leeg gelaten worden
        PostCondities:
            Er is een extra zaal in de bioscoop
        :return: None
        """
        pass

    def remove_zaal(self, nummer):
        """
        Functie: verwijder zaal
        Beschrijving: verwijdert een bestaande zaal
        Input Parameters:
            :param nummer: nummer van de zaal
        PreCondities:
            nummer: > 0, en mag niet leeg gelaten worden
        PostCondities:
            Er is een zaal minder in de bioscoop
        :return: True als verwijderen gelukt, False als niet gelukt
        """
        pass

    def getPlaatsen(self):
        pass

    def getZaalNummer(self):
        pass

