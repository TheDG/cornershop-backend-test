"""Python script that runs all quality tools."""

import subprocess

TEST = "python manage.py test"

try:
    subprocess.check_output(TEST, shell=True)
except subprocess.CalledProcessError:
    print("Failed Tests")
    quit(1)

COVERAGE = 'coverage report --skip-covered --fail-under=90'
try:
    subprocess.check_output(COVERAGE, shell=True)
except subprocess.CalledProcessError:
    print("Failed due to uncomplete coverage")
    quit(1)

PYCODESTYLE = 'pycodestyle .'
try:
    subprocess.check_output(PYCODESTYLE, shell=True)
except subprocess.CalledProcessError:
    print("Failed due to style conventions -- pycodestyle")
    quit(1)

MC_CABE = 'python ci/run_mccabe.py 10'
try:
    subprocess.check_output(MC_CABE, shell=True)
except subprocess.CalledProcessError:
    print("Failed due to complexity checker -- McCabe")
    quit(1)

PYFLAKES = 'python ci/run_pyflakes.py'
try:
    subprocess.check_output(PYFLAKES, shell=True)
except subprocess.CalledProcessError:
    print("Failed due to source files for errors -- PyFlakes")
    quit(1)

PYLINT = 'python ci/run_pylint.py'
try:
    subprocess.check_output(PYLINT, shell=True)
except subprocess.CalledProcessError:
    print("Failed due to ... -- Pylint")
    quit(1)

print("Passed all quality control")
quit(0)
