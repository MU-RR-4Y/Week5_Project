class Destination:
    def __init__(self, name, country, information, id = None):
        self.name = name
        self.country = country
        self.information = information
        self.id = id
        self.wishlisted = []
        self.visited_by =[]

    def add_to_wishlisted(self, user):
        self.wishlisted.append(user)

    def remove_from_wishlisted(self, user):
        self.wishlisted.remove(user)

    def add_to_visited(self, user):
        self.visited_by.append(user)

