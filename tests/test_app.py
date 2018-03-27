import unittest
import mock

from notifyme.app import App


class TestApp(unittest.TestCase):

    @mock.patch('subprocess.run')
    @mock.patch('notifyme.notificator.Notificator')
    def test_run_app(self, mock_notificator, mock_run):
        argv = ['python', '--version']
        app = App(argv, mock_notificator)
        app.run()
        mock_run.assert_called_with(argv)
        mock_notificator.notify.assert_called()
