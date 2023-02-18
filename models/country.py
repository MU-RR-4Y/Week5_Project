class Country:
    def __init__(self, name, id = None):
        self.name = name
        self.destination = []
        self.id = id
        

    def add_destination(self, destination):
        self.destination.append(destination)