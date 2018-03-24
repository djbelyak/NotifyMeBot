#!/usr/bin/env python
''' The main entry point of the app. '''
import sys
from notifyme.cli import parse_args


def main():
    args = parse_args(sys.argv[1:])
    print('Args: {}'.format(args))


if __name__ == '__main__':
    main()
