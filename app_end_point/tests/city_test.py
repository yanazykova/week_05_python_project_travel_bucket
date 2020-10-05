import unittest
from models.city import City 

# class City:
#     def __init__(self, name, country, visited = False, id=None):
#         self.name = name 
#         self.country = country 
#         self.visited = visited
#         self.id = id 

#     def mark_visited(self):
#         self.visited = True

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Moscow", "Russia", False)

    def test_city_has_name(self):
        self.assertEqual("Moscow", self.city.name)

    def test_city_has_country(self):
        self.assertEqual("Russia", self.city.country)

    def test_city_visited_starts_false(self):
        self.assertEqual(False, self.city.visited)

    def test_can_mark_city_visited(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)

    

    

    