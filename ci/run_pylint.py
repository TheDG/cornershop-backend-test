"""Python script that runs Pylint on all specfied directories."""

import subprocess
import sys


def main():
    """Main function /command for Pylint script. Runs pylint with djano plugin"""
    test = "pylint lunch_poll pages ci users --load-plugins pylint_django"
    try:
        subprocess.check_output(test, shell=True)
    except subprocess.CalledProcessError:
        print("Failed Pylint")
        quit(1)


if __name__ == "__main__":
    sys.exit(main())
