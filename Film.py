from random import randint
class Film:
    def __init__(self, id, titel, rating = 1):
        self.id = id
        self.titel = titel
        self.rating = rating
        self.filmLijst = []
        self.filmLijst.append(self.id)


    # Contract voor Film

    def addFilm(self, id, titel, rating):
        """
        Functie: add_film
        Beschrijving: voegt een film toe
        Input Parameters en PreCondities
            :param id: int, deze is een uniek getal tussen 10 en 100
            :param titel: String, mag niet de lege string zijn
            :param rating: float, > 0
        PostCondities:
            Er zit nu 1 film meer in de lijst
        :return: None
        """
        pass

    def setRating(self, rating):
        '''
        Functie setRating()
        Beschrijving: past de rating van de film aan
        Input Parameters en PreCondities:
        :param rating: float, getal tussen 0 en 5 (inclusief 5)
        :return: True als gelukt is
        '''
        pass

    def getRating(self):
        '''
        Functie getRating()
        Beschrijving: Geeft de rating van een film weer
        Input Parameters en PreCondities: /
        PostCondities: /
        :return: Rating
        '''
        pass

    def getID(self):
        '''
        Functie getID()
        Beschrijving: Geeft het ID van de film
        Input Parameters en PreCondities: /
        PostCondities: /
        :return: ID
        '''
        pass
