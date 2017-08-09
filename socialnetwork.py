class User:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.user_name = name
        self.user_id = []
        self.connections = []

    def user_name(self, user_name):
        self.user_name = user_name

    def user_id(self, number):
        self.user_id = number

    def connections(self, friend):
        self.connections.append(friend)

    def getconnections(self):
        return self.connections

    def getuser_id(self):
        return self.user_id

class Network:
    # Define the fields and methods for your object here.
    def users(self, list):
        list = []

def main():
    # Define the program flow for your user interface here.
