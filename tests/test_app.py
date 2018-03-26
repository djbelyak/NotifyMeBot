import unittest
import mock

from notifyme.app import App


class TestApp(unittest.TestCase):

    @mock.patch('subprocess.run')
    @mock.patch('telegram.Bot')
    def test_run_app(self, mock_bot, mock_app):
        argv = ['python', '--version']
        token = 'token'
        user_id = 'user_id'
        app = App(argv, token, user_id)
        app.run()
        mock_app.assert_called_with(argv)
        mock_bot.assert_called_with(token)
