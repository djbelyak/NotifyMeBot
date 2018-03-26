#!/usr/bin/env python
''' The main entry point of the app. '''
import sys
from notifyme.cli import parse_args
from notifyme.app import App


def main():
    args = parse_args(sys.argv[1:])
    app = App(args.command, args.token, args.user_id)
    app.run()


if __name__ == '__main__':
    main()
