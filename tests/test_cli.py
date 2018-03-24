import unittest

from notifyme.cli import parse_args


class TestParseArgs(unittest.TestCase):

    def test_one_word_command(self):
        argv = ['python']
        args = parse_args(argv)
        self.assertEqual(args.command, argv)
