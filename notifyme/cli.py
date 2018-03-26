''' This package contains all about command line interface.'''
import argparse
from notifyme import __doc__


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=__doc__.strip()
    )
    parser.add_argument(
        'command',
        nargs=argparse.REMAINDER,
        help='command which will be execute'
    )

    parser.add_argument(
        '--token',
        required=True,
        help='your Telegram API token for bot'
    )

    parser.add_argument(
        '--user_id',
        required=True,
        help='your telegram user_id (ask @userinfobot)'
    )

    return parser.parse_args(args)
