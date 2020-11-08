# Reservatiemanagement
class Reservatie:
    def __init__(self, userid, verid, plaatsen, timestamp):
        '''
        :param userid: user-id (int)
        :param verid: vertoning-id (int)
        :param plaatsen: #Gereserveerde plaatsen (int)
        :param timestamp: timestamp (str)
        '''
        pass

    def getUserId(self):
        '''
        Geeft User-Id terug
        :return userid: (int)
        '''
        pass

    def getVertoningId(self):
        '''
        Geeft vertoning-Id terug
        :return verid: (int)
        '''
        pass

    def getPlaatsen(self):
        '''
        Geeft aantal plaatsen terug
        :return plaatsen: (int)
        '''
        pass

    def getTimestamp(self):
        '''
        Geeft timestamp terug
        :return timestamp: (str)
        '''
        pass

