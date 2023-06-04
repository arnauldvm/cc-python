import logging
import argparse
from ._version import version
from . import token as tk
# CHANGE_ME: You should replace "token" by your own module(s)

logger = logging.getLogger(__name__)


class UsageArgParseAction(argparse.Action):
    def __call__(self, parser, ns, valuers, option):
        parser.print_usage()
        exit(0)


class ToggleArgParseAction(argparse.Action):
    def __call__(self, parser, ns, valuers, option):
        setattr(ns, self.dest, bool('-+'.index(option[0])))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Generate a cryptographic safe random password',
        prefix_chars='-+',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-U', '--usage', action=UsageArgParseAction, nargs=0,
                        help='shows summary usage and exit')
    parser.add_argument('-V', '--version', action='version', version=version,
                        help="shows version number and exit")

    parser.add_argument('-v', '--verbose', default=0, action='count',
                        help='Increase verbosity (repeat for more)')
    parser.add_argument('-L', '--length', type=int, default=12,
                        help='Length of the password')
    parser.add_argument('-u', '+u', '--upper', '++upper', action=ToggleArgParseAction,
                        dest='use_upper', default=True, nargs=0,
                        help='Disable/Enable uppercase letters')
    parser.add_argument('-l', '+l', '--lower', '++lower', action=ToggleArgParseAction,
                        dest='use_lower', default=False, nargs=0,
                        help='Disable/Enable lowercase letters')
    parser.add_argument('-d', '+d', '--digits', '++digits', action=ToggleArgParseAction,
                        dest='use_digits', default=True, nargs=0,
                        help='Disable/Enable digits')
    parser.add_argument('-s', '+s', '--special', '++special', action=ToggleArgParseAction,
                        dest='use_special', default=False, nargs=0,
                        help='Disable/Enable special characters')
    parser.add_argument('actions', choices=['token', 'entropy'], default='password',
                        metavar='ACTION', nargs='+',
                        help='Whether to generate a token ("token") '
                             'or compute the entropy ("entropy") (may be combined)')
    args = parser.parse_args()
    return args


def config_logging(verbosity: int) -> None:
    if verbosity >= 3:
        loggingLevel = logging.DEBUG
    elif verbosity >= 2:
        loggingLevel = logging.INFO
    elif verbosity >= 1:
        loggingLevel = logging.WARNING
    else:
        loggingLevel = logging.ERROR
    logging.basicConfig(level=loggingLevel)


def main():
    args = parse_args()

    config_logging(args.verbose)

    logger.debug('args = %r', args)

    alphabet = tk.AlphabetDefinition(
        use_upper=args.use_upper,
        use_lower=args.use_lower,
        use_digits=args.use_digits,
        use_special=args.use_special,
        )
    logger.debug('alphabet = %r', alphabet)
    logger.info('alphabet: %s', alphabet.get_chars())

    if 'token' in args.actions:
        token = tk.generate(alphabet, args.length)
        print(token)
    if 'entropy' in args.actions:
        entropy = tk.compute_entropy(alphabet, args.length)
        print(f"{entropy:.1f} bits: {tk.get_strength_class(entropy)}")


if __name__ == '__main__':
    main()
