''' This package contains all about notification via Telegram. '''
import telegram


class Notificator():

    def __init__(self, token, chat_id):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id

    def notify(self, message):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=message
            )
