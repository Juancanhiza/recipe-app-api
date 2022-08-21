"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def addTest(self):
        """Test add operation"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)