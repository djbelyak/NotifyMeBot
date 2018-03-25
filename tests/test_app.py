import unittest
import mock

from notifyme.app import App


class TestApp(unittest.TestCase):

    @mock.patch('subprocess.run')
    def test_one_word_command(self, mock_app):
        argv = ['python']
        app = App(argv)
        app.run()
        mock_app.assert_called_with(argv)
