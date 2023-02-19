class User:
    def __init__(self, name, id = None):
        self.name = name
        self.wishlist = []
        self.visited_list =[]
        self.id = id

    def add_to_wishlist(self,destination):
        self.wishlist.append(destination.id)

    def add_to_visited_list(self, destination):
        self.visited_list.append(destination.id)

    def remove_from_wishlist(self,destination):
        self.wishlist.remove(destination.id)