import argparse
import sys
from . import datatool


def main():
    parser = argparse.ArgumentParser(description='datatool')
    cmd_parsers = parser.add_subparsers(help=' - sub-commands -',
                                        dest='subparser_name')

    add_parser = cmd_parsers.add_parser('add',
                                        help='Add directory to search path')
    add_parser.add_argument('dir',
                            help='Add directory to the search path')

    fetch_parser = cmd_parsers.add_parser('fetch',
                                          help='Download dataset')
    fetch_parser.add_argument('package',
                              help='Fetch files from this package')
    fetch_parser.add_argument('group', nargs='?',
                              help='Fetch this group of files (optional)')

    status_parser = cmd_parsers.add_parser('status',
                                           help='Show status of package(s)')
    status_parser.add_argument('package', nargs='?',
                               help='Package to operate on')

    parser.add_argument('extra', nargs="*", help=argparse.SUPPRESS)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    cmd = args.subparser_name

    if cmd == 'add':
        datatool.add(path=args.dir)
    elif cmd == 'fetch':
        datatool.fetch(package=args.package, group=args.group)
    elif cmd == 'status':
        datatool.status(package=args.package)


if __name__ == '__main__':
    main()
