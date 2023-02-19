class User:
    def __init__(self, name, wishlist = None, visited_list = None, id = None):
        if wishlist == None:
            wishlist =[]
            self.wishlist = wishlist

        if visited_list == None:
            visited_list = []
            self.visited_list = visited_list    

        self.name = name
        self.id = id

    def add_to_wishlist(self,destination):
        self.wishlist.append(destination.id)

    def add_to_visited_list(self, destination):
        self.visited_list.append(destination.id)

    def remove_from_wishlist(self,destination):
        self.wishlist.remove(destination.id)