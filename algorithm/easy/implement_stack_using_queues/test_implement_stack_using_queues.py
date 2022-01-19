from unittest import TestCase
from implement_stack_using_queues import MyStack


class TestMyStack(TestCase):
    def test_push(self):
        s = MyStack()
        s.push(3)
        s.push(2)
        s.push(1)
        x = s.pop()
        self.assertTrue(x, 1)
        self.assertTrue(x, 2)
        self.assertTrue(x, 3)

    def test_pop(self):
        self.skipTest('x')

    def test_top(self):
        s = MyStack()
        s.push(3)
        s.push(2)
        s.push(1)
        x = s.top()
        self.assertTrue(x, 1)

    def test_empty(self):
        s = MyStack()
        self.assertTrue(s.empty())
        s.push(1)
        self.assertFalse(s.empty())

    def test_full(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        x = s.top()
        self.assertEqual(x, 2)
        y = s.pop()
        self.assertEqual(y, 2)
        self.assertFalse(s.empty())
