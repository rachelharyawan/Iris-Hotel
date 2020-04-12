from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

class Admin:
    def __init__(self):
        self.cluster = cluster

    def getusername(self):
        return admin['admin']

    def getpassword(self):
        return admin['admin']
        
