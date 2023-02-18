import unittest
from models.user import User
from models.destination import Destination

class TestUser(unittest.TestCase):
    def setUp(self):
        self.destination_1 = Destination('Rome', 'Italy', 'Capital of Italy')
        self.destination_2 = Destination('Paris', 'France','Capital of France')
        self.user = User('Dave')


    def test_user_name(self):
        self.assertEqual('Dave', self.user.name)

    def test_user_wish_list(self):
        self.assertEqual(0, len(self.user.wishlist))

    def test_user_visited_list(self):
        self.assertEqual(0, len(self.user.visited_list))

    def test_add_to_wishlist(self):
        self.user.add_to_wishlist(self.destination_1)
        self.assertEqual(1,len(self.user.wishlist))
        self.assertEqual('Rome', self.user.wishlist[0].name)

    def test_add_to_visited_list(self):
        self.user.add_to_visited_list(self.destination_1)
        self.assertEqual(1,len(self.user.visited_list))
        self.assertEqual('Rome', self.user.visited_list[0].name)

    def test_remove_from_wishlist(self):
        self.user.add_to_wishlist(self.destination_1)
        self.user.add_to_wishlist(self.destination_2)
        self.user.remove_from_wishlist(self.destination_1)
        self.assertEqual(1, len(self.user.wishlist))
        self.assertEqual('Paris', self.user.wishlist[0].name)

    def test_user_id__isNone(self):
        self.assertIsNone(self.user.id)
   
    def test_user_isNotNone(self):
        self.user.id = 1
        self.assertEqual(1, self.user.id)

