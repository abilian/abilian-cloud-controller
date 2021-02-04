#!/usr/bin/env python

from acc import commands
from acc.config import DEBUG
import sys
import getopt


#
# Main
#
def run(argv):
    opts, args = getopt.getopt(argv, "t:")
    options = {}
    cmd = args[0]
    for k, v in opts:
        if k == "-t":
            options["type"] = v
    fn = vars(commands)["cmd_" + cmd]
    if len(args) > 1:
        fn(*args[1:], **options)
    else:
        fn(**options)


def main():
    if len(sys.argv) == 1:
        args = ["help"]
    else:
        args = sys.argv[1:]
    if DEBUG:
        run(args)
    else:
        try:
            run(args)
        except Exception as e:
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    main()
