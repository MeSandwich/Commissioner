# Class that contains all information about the commission

class Commission:
    _priorityLevel = 0
    _client = ""
    _clientContactInfo = ""
    _dueDate = ""

    _price = ""
    _notes = ""

    # Creates a new Commission with the basic stats
    def __init__(self,priority, client, clientInfo, dueDate):
        self.updateCommision(priority,client,clientInfo,dueDate)

    # Updates the commission
    def updateCommision(self,priority, client, clientInfo, dueDate):
        self._priorityLevel = priority
        self._client = client
        self._clientContactInfo = clientInfo
        self._dueDate = dueDate

    # Returns very basic info of the commission
    def getBasicCommisionInfo(self):
        commissionInfo = [self._priorityLevel,self._client,self._dueDate]

