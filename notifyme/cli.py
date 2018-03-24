''' This package contains all about command line interface.'''
import argparse
from notifyme import __doc__


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=__doc__.strip()
    )
    parser.add_argument(
        'command',
        nargs='+',
        help='command which will be execute'
    )
    return parser.parse_args(args)
