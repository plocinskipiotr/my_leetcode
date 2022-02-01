from unittest import TestCase
from student_attendance_record_1 import Solution


class TestSolution(TestCase):
    def test_check_record(self):
        s = Solution()
        s1 = "PPALLP"
        self.assertTrue(s.checkRecord(s1))

    def test_check_record2(self):
        s = Solution()
        s1 = "PPALLL"
        self.assertFalse(s.checkRecord(s1))
