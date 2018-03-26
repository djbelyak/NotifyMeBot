''' This package contains a main logic of application. '''
import subprocess
import telegram


class App():
    def __init__(self, command, token, user_id):
        self.command = command
        self.token = token
        self.user_id = user_id

    def run(self):
        subprocess.run(self.command)
        bot = telegram.Bot(self.token)
        bot.send_message(
            chat_id=self.user_id,
            text=' '.join(self.command) + ' complete'
            )
