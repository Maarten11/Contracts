from random import randint
from copy import deepcopy

class Gebruiker:
    # Contract voor Gebruiker
    def __init__(self, voornaam, achternaam, email, wachtwoord):
        self.gebruikersLijst = []
        self.voornaam = voornaam
        self.achternaam = achternaam


    def addGebruiker(self, voornaam, achternaam, email, wachtwoord):
        """
        Functie: add_gebruiker
        Beschrijving: Voegt een gebruiker toe
        Input Parameters en PreCondities:
            :param id: int, dit getal is uniek en positief
            :param voornaam: String, niet leeg
            :param achternaam: String, niet leeg
            :param email: String, niet leeg en bevat "@" en ".com" of een dergelijk adres
            :param wachtwoord: String, niet leeg en controle op sterkte wachtwoord -> 8 tekens en combinatie letters + cijfers + hoofdletters
        PostCondities:
            Maakt een extra gebruiker aan
        :return: None
        """
        pass

    def verwijderGebruiker(self):
        pass

    def getID(self):
        pass
