from unittest import TestCase
from min_stack import MinStack


class TestMinStack(TestCase):
    def test_overall(self):
        m = MinStack()
        m.push(-2)
        m.push(-0)
        m.push(-3)
        self.assertEqual(-3, m.getMin())
        m.pop()
        self.assertEqual(0, m.top())
        self.assertEqual(-2, m.getMin())

    def test_overall2(self):
        m = MinStack()
        m.push(2147483646)
        m.push(2147483646)
        m.push(2147483646)
        m.top()
        m.pop()
        m.getMin()
        m.pop()
        m.getMin()
        m.pop()
        m.push(2147483646)
        m.top()
        m.getMin()
        m.push(-2147483646)
        m.top()
        m.getMin()
        m.pop()
        m.getMin()
