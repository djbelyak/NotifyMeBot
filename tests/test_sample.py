import unittest

from notifyme import test


class TestSample(unittest.TestCase):

    def test_test(self):
        expected = 'Everything ok!'
        self.assertEqual(test(), expected)
