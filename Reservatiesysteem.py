from copy import deepcopy
from domain.Gebruiker import Gebruiker
from domain.LinkedChain import LinkedChain
from domain.Film import Film
from domain.Reservatie import Reservatie
from domain.Vertoning import Vertoning
from domain.Queue import Queue


class ReservatieSysteem:
    def __init__(self):
        self.reservatieID = None
        self.vertoningID = None
        self.filmID = None
        self.userID = None
        self.aantalPersonen = 0
        self.gebruikersLijst = LinkedChain()
        self.filmLijst = LinkedChain()
        self.vertoningLijst = [] # Boom als arrayImplementatie
        self.reservatieLijst = Queue()


    # Contract voor ReservatieSysteem

    def maakReservatie(self, id, userID, timeStamp, vertoningID, plaatsenGereserveerd):
        '''
        Functie: maakReservatie
        Beschrijving: Maakt een nieuwe reservatie aan
        Input Parameters en PreCondities:
            :param id: int, deze is uniek en niet leeg
            :param userID: int, deze is bestaand en uniek
            :param timeStamp: int, de vertoning vindt plaats op dit tijdstip
            :param vertoningID: int, deze is bestaand
            :param plaatsenGereserveerd: int, deze is kleiner dan het aantal beschikbare plaatsen
        PostCondities:
            Reservatie gemaakt, er wordt een mail gestuurd naar de gebruiker met de tickets, het aantal vrije plaatsen voor die voorstelling verlaagt
        :return: unieke reservatieID
        '''
        pass

    def verwijderReservatie(self, vertoningID, userID):
        '''
        Functie: verwijderReservatie
        Beschrijving: verwijdert een eerder gemaakte reservatie
        Input Parameters en PreCondities:
            :param vertoningID: int, deze is bestaand en staat op naam van de gebruiker
            :param userID: int, deze is bestaand
        PostCondities: Meer plaatsen vrij voor de vertoning, reservatie wordt geschrapt
        :return: True als gelukt
        '''
        pass

    def meldAan(self, email, password):
        '''
        Functie: meldAan
        Beschrijving: De gebruiker meld zich aan bij het systeem
        Input Parameters en PreCondities
            :param email: string, deze bestaat reeds in het systeem
            :param password: string, deze komt overeen met het wachtwoord van de gebruiker
        PostCondities: None
        :return: True als gelukt
        '''
        pass

    def maakAccount(self, voornaam, achternaam, email, wachtwoord):
        '''
        Functie: maakAccount
        Beschrijving: De gebruiker maakt een nieuw account aan
        Input Parameters en PreCondities:
            :param voornaam: string, niet leeg
            :param achternaam: string, niet leeg
            :param email: string, geldig emailadres (__@__.__)
            :param wachtwoord: string, controle op sterkte wachtwoord -> 8 tekens en combinatie letters + cijfers + hoofdletters
        PostCondities: Voegt een gebruiker toe aan de lijst met gebruikers, stuurt een bevestigingsmail, slaat unieke userID op
        :return: unieke userID
        '''
        pass

    def verwijderAccount(self, userID):
        '''
        Functie: verwijderAccount
        Beschrijving: De account wordt verwijderd
        Input Parameters en PreCondities:
            :param userID: int, deze bestaat in het systeem en is van de aangemeldde gebruiker
        PostCondities: Alle informatie van dit account wordt uit het systeem verwijdert
        :return: True als gelukt
        '''
        pass

    def bekijkReservatie(self, reservatieID):
        '''
        Functie: bekijkReservatie
        Beschrijving: De reservatie wordt weergegeven met de informatie
        Input Parameters en PreCondities:
            :param reservatieID: int, deze bestaat in het systeem en is van de aangemeldde gebruiker
        PostCondities:  Geeft informatie terug
        :return: alle informatie omtrent deze reservatie (id, userID, timeStamp, vertoningID, plaatsenGereserveerd)
        '''
        pass

    def voegGebruikerToe(self, gebruiker):
        '''
        Functie voegGebruikerToe
        Beschrijving: Zet een nieuwe gebruiker in het systeem
        :param gebruiker: Een geldig geinitialiseerde gebruiker, die nog niet in het systeem zit
        :return: True als gelukt, False als niet
        '''
        pass

    def voegFilmToe(self, film):
        '''
        Functie addFilm
        Beschrijving: Zet een nieuwe film in het systeem
        :param gebruiker: Een geldig geinitialiseerde film, die nog niet in het systeem zit
        :return: True als gelukt, False als niet
        '''
        pass

    def voegVertoningToe(self, vertoning):
        '''
        Functie addFilm
        Beschrijving: Zet een nieuwe film in het systeem
        :param gebruiker: Een geldig geinitialiseerde film, die nog niet in het systeem zit
        :return: True als gelukt, False als niet
        '''
        pass

    def voegReservatieToe(self, reservatie):
        '''
        Functie addFilm
        Beschrijving: Zet een nieuwe film in het systeem
        :param gebruiker: Een geldig geinitialiseerde film, die nog niet in het systeem zit
        :return: True als gelukt, False als niet
        '''
        pass

    def leesReservatie(self):
        '''
        Functie: leesReservatie
        Beschrijving: leest de volgende reservatie in
        Input Parameters en PreCondities: /
        PostCondities: Verwerkt de reservatie en haalt deze van de queue
        :return: Reservatie, True als gelukt, False als niet gelukt
        '''
        pass

    def startVertoning(self, vertoning):
        pass

    def getFilmByID(self, id):
        pass

    def getVertoningByID(self, id):
        pass
