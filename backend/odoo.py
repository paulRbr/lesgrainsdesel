import xmlrpc.client


class Odoo:
    def __init__(self):
        self.url = 'http://127.0.0.1:8069'
        self.db = 'foodcoops'
        self.username = 'admin'
        self.password = 'admin'

        self.common = False
        self.models = False
        self.uid = False

    def setCredentials(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

    def setCommonEndpoint(self):
        self.common = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(self.url))

    def authenticate(self):
        self.uid = self.common.authenticate(
            self.db, self.username, self.password, {})

    def setObjectEndpoint(self):
        self.models = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/object'.format(self.url))

    def connect(self):
        self.setCommonEndpoint()
        self.authenticate()
        self.setObjectEndpoint()

    def searchRead(self, dbTable: str, filters: [str], fields: [str]):
        if(self.models):
            return self.models.execute_kw(self.db, self.uid, self.password,
                                          dbTable, 'search_read',
                                          [filters],
                                          {'fields': fields})

    def createEvent(self, name: str, dateBegin: str, dateEnd: str, organizerID: int):
        return self.models.execute_kw(self.db, self.uid, self.password, 'event.event', 'create', [{
            'name': name, 'date_begin': dateBegin, 'date_end': dateEnd, 'organizer_id': organizerID
        }])

    def version(self) -> str:
        if self.common != None:
            return self.common.version()
        else:
            return "You need to connect first.\nExecute .setCommonEndpoint()"
