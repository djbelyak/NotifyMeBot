#!/usr/bin/env python
''' The main entry point of the app. '''
import sys
from notifyme.cli import parse_args
from notifyme.app import App
from notifyme.notificator import Notificator


def main():
    args = parse_args(sys.argv[1:])
    notificator = Notificator(
        token=args.token,
        chat_id=args.user_id
    )
    app = App(args.command, notificator)
    app.run()


if __name__ == '__main__':
    main()
