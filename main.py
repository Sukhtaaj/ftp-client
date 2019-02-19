import sys
import argparse

from wrapper import SFTPWrapper


def main():
    sftp_wrapper = SFTPWrapper()
    sftp_wrapper.cmdloop()

if __name__ == '__main__':
    main()
