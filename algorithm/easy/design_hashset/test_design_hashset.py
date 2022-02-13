from unittest import TestCase
from design_hashset import MyHashSet


class TestMyHashSet(TestCase):
    def test_add(self):
        hash_set = MyHashSet()
        hash_set.add(10)
        hash_set.add(10)
        hash_set.add(10)
        self.assertTrue(hash_set.contains(10))

    def test_remove(self):
        hash_set = MyHashSet()
        hash_set.add(10)
        hash_set.remove(10)
        self.assertFalse(hash_set.contains(10))

    def test_contains(self):
        hash_set = MyHashSet()
        self.assertFalse(hash_set.contains(15))


    def test_scenario(self):
        hash_set = MyHashSet()
        hash_set.add(9)


