from copy import deepcopy

class Reservatie:
    def __init__(self, id, userID, timeStamp, vertoningID, plaatsenGereserveerd):
        self.id = id
        self.userID = userID
        self.timeStamp = timeStamp
        self.vertoningID = vertoningID
        self.plaatsenGereserveerd = plaatsenGereserveerd

    # contract voor Reservatie

    def add_reservatie(self, id, userID, timeStamp, vertoningID, plaatsenGereserveerd):
        """
        Functie: add_reservatie
        Beschrijving: voegt een reservatie toe
        Input Parameters en PreCondities
            :param id: int, de ID is uniek
            :param userID: int, deze ID bestaat
            :param timeStamp: int, > 0 deze tijd en datum zijn beschikbaar voor de gekozen film
            :param vertoningID: int, dit is een bestaande ID
            :param plaatsenGereserveerd: int, > 0 en niet groter dan het aantal beschikbare plaatsen voor de film op die dag
        PostCondities:
            Er is nu één extra reservatie en verlaagt het aantal beschikbare plaatsen voor die film op die dag
        :return: None
        """
        self.id = id
        self.userID = userID
        self.timeStamp = timeStamp
        self.vertoningID = vertoningID
        self.plaatsenGereserveerd = plaatsenGereserveerd

    def getVertoning(self):
        pass

    def getPlaatsenGereserveerd(self):
        pass
