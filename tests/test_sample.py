import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from notifyme import test


class TestSample(unittest.TestCase):

    def test_test(self):
        expected = 'Everything ok!'
        self.assertEqual(test(), expected)


if __name__ == '__main__':
    unittest.main()