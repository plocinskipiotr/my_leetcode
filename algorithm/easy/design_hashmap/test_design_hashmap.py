from unittest import TestCase
from design_hashmap import MyHashMap


class TestMyHashMap(TestCase):
    def test_my(self):
        my_map = MyHashMap()
        my_map.put(1, 1)
        my_map.put(2, 2)
        my_map.get(1)
        my_map.get(3)
        my_map.put(2, 1)
        my_map.get(2)
        my_map.remove(2)
        my_map.get(1)

