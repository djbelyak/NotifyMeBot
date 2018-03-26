import unittest

from notifyme.cli import parse_args


class TestParseArgs(unittest.TestCase):

    def test_one_word_command(self):
        token = 'token'
        user_id = '123'
        command = ['python']
        argv = ['--token', token] + ['--user_id', user_id] + command
        args = parse_args(argv)
        self.assertEqual(args.command, command)
        self.assertEqual(args.token, token)
        self.assertEqual(args.user_id, user_id)

    def two_words_command(self):
        argv = ['python', '--version']
        args = parse_args(argv)
        self.assertEqual(args.command, argv)
