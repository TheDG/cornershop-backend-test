"""Python script to run all linters."""

import os

print("------------running Pycodestyle------------")
PYCODESTYLE = 'pycodestyle .'
os.system(PYCODESTYLE)

print("------------running McCabe------------")
MC_CABE = 'python ci/run_mccabe.py 10'
os.system(MC_CABE)

print("------------running Pyflakes------------")
PYFLAKES = 'python ci/run_pyflakes.py'
os.system(PYFLAKES)

print("------------running Pylint------------")
PYLINT = 'pylint lunch_poll pages ci --load-plugins pylint_django'
os.system(PYLINT)
