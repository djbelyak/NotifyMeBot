import unittest
import mock

from notifyme.notificator import Notificator


class TestNotificator(unittest.TestCase):

    @mock.patch('telegram.Bot')
    def test_notificator_init(self, mock_bot):
        token = 'token'
        user_id = 'user_id'

        Notificator(token, user_id)

        mock_bot.assert_called_with(token=token)

    @mock.patch('telegram.Bot')
    def test_notify(self, mock_bot):
        token = 'token'
        user_id = 'user_id'
        message = 'Message'

        nf = Notificator(token, user_id)
        nf.notify(message)

        mock_bot.assert_called_with(token=token)
        mock_bot.send_message.asser_called_with(
            chat_id=user_id,
            text=message)
