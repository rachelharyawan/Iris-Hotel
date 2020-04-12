from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

class Receptionist:
    def __init__(self):
        self.cluster = cluster

    def getusername(self):
        return receptionist['receptionist']

    def getpassword(self):
        return receptionist['receptionist']
        
