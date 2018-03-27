''' This package contains a main logic of application. '''
import subprocess


class App():
    def __init__(self, command, notificator):
        self.command = command
        self.notificator = notificator

    def run(self):
        subprocess.run(self.command)
        self.notificator.notify(' '.join(self.command) + ' complete')
