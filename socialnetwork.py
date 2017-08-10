import turtle
import math

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
    def __init__(self):
        self.connection = []
        self.users = []
        
    def connection(self):
        self.connections = []

    def getusers(self):
        return self.users 

    def add_user(self, alloweduser):
        self.user.append(alloweduser)

    def addconnection(self, user1, user2):
        if user1.connection not in connections:
            user1.addconnection(user2)
            user2.addconnecton(user1)
        if user2.connection not in connections:
            user1.addconnection(user2)
            user2.addconnection(user1)


def main():
    # Define the program flow for your user interface here.

# Runs your program.
if __name__ == '__main__':
    main():
