# Gebruiker management

class Gebruiker:
    def __init__(self, fname, lname, email):
        '''
        :param fname: firstname (str)
        :param lname: lastname (str)
        :param email: (str)
        :return succes: bool,duidt aan of het toevoegen gelukt is
        '''
        pass

    def getFname(self):
        '''
        Vraagt voornaam op
        :return fname: str
        '''
        pass

    def getLname(self):
        '''
        Vraagt achternaam op
        :return lname: str
        '''
        pass

    def getEmail(self):
        '''
        Vraagt email op
        :return email: str
        '''
        pass

    def changeFname(self, fname):
        '''
        Verander de voornaam van een user
        :param fname: str
        :return succes: bool duidt aan of het aanpassen gelukt is
        '''
        pass

    def changeLname(self, lname):
        '''
        Verander de achternaam van een user
        :param lname: str
        :return succes: bool duidt aan of het aanpassen gelukt is
        '''
        pass

    def changeMail(self, email):
        '''
        Verander de email van een user
        :param email: str
        :return succes: bool duidt aan of het aanpassen gelukt is
        '''
        pass

