# Vertoning management

class Vertoning:
    def __init__(self, zaalnr, vrij, fid, slot, date,bezet=0):
        '''
        :param zaalnr: zaalnummer (int)
        :param vrij: vrije plaatsen (int)
        :param fid: film-id (int)
        :param slot: slot (str)
        :param date: datum (str)
        :return succes: bool
        '''
        self.zaalnr = zaalnr
        self.vrij = vrij
        self.fid = fid
        self.slot = slot
        self.date = date
        self.bezet = bezet


    def getZaalnr(self):
        '''
        Geef info over vertoning weer
        :return zaalnr: int
        '''
        return self.zaalnr

    def getVrij(self):
        '''
        Geeft aantal vrije plaatsen terug
        :return vrij: int
        '''
        return self.vrij

    def getFilmId(self):
        '''
        Geeft Film-Id terug
        :return fid: int
        '''
        return self.fid

    def getSlot(self):
        '''
        Geeft slot terug
        :return slot: str
        '''
        return self.slot

    def getDate(self):
        '''
        Geeft datum terug
        :return date: str
        '''
        return self.date

