from domain.Stack import Stack
from copy import deepcopy
from random import randint

class Vertoning:
    def __init__(self, zaalNummer, slot, datum, filmID, vrijePlaatsen):
        self.id = randint(1,100)
        self.zaalNummer = zaalNummer
        self.slot = slot
        self.datum = datum
        self.filmID = filmID
        self.vrijePlaatsen = vrijePlaatsen
        self.totalePlaatsen = vrijePlaatsen
        self.stack = Stack()

        self.slotUren = {0: "14u30", 1: "17u00", 2: "20u00", 3: "22u30"}

    # Contract voor Vertoning
    def add_vertoning(self, id, zaalNummer, slot, datum, filmID, vrijePlaatsen):
        """
        Functie: add_vertoning
        Beschrijving: voegt een vertoning toe
        Input Parameters en PreCondities
            :param id: int, moet een uniek getal zijn en mag niet leeg zijn
            :param zaalNummer: int, moet een bestaande zaal zijn en mag niet leeg zijn
            :param slot: int, is een getal tussen 1 en 4
            :param datum: int, is een bestaande datum, die in de toekomst plaatsvindt
            :param filmID: int, is een bestaande ID
            :param vrijePlaatsen: int, niet groter dan het aantal plaatsen in de zaal en niet kleiner dan 0
        PostCondities:
            Er zit nu 1 vertoning meer in de lijst en het tijdsslot is niet meer beschikbaar
        :return: None
        """
        pass

    def get_datum(self, id):
        """
        Functie: get_datum
        Beschrijving: geeft de datum van een vertoning terug
        Input Parameters en Precondities
            :param id: int, moet een bestaande ID zijn en mag niet leeg gelaten worden
        PostCondities:
            Geeft de datum terug
        :return: datum
        """
        pass

    def getStartUur(self):
        '''
        Functie: getStartUur
        Beschrijving: Geeft het startuur van de film weer
        Input Parameters en PreConidities: /
        PostCondities: /
        :return: startuur van de film
        '''
        pass

    def verlaagVrijePlaatsen(self, plaatsen):
        '''
        Functie: verlaagVrijePlaatsen
        Beschrijving: Verlaag het aantal beschikbare plaatsen
        Input Parameters en PreCondities:
        :param plaatsen: int, aantal bezette plaatsen. Dit is kleiner dan of gelijk aan het aantal beschikbare plaatsen
        :return: True als gelukt, False als niet gelukt
        '''
        pass

    def getID(self):
        '''
        Funcite: getID
        Beschrijving: geeft het ID van een vertoning
        Input Parameters: /
        PreCondities: De vertoning bestaat
        PostCondities: /
        :return: Het id van de vertoning
        '''
        pass