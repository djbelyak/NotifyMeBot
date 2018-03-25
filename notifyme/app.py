''' This package contains a main logic of application. '''
import subprocess


class App():
    def __init__(self, command):
        self.command = command

    def run(self):
        subprocess.run(self.command)
