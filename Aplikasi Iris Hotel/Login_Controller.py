from cassandra.cluster import Cluster
from Admin import Admin
from Receptionist import Receptionist

cluster = Cluster()
session = cluster.connect()

class LoginControl:
    def __init__(self):
        self.cluster = cluster

    def checkLoginAdmin(self,username,password):
        if admin.getpassword() == admin:
            return True
        return False

    def checkLoginReceptionist(self,username,password):
        if receptionist.getpassword() == receptionist:
            return True
        return False
