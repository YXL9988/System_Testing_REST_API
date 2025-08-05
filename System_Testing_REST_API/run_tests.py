import subprocess
import sys
subprocess.run([sys.executable, '-m', 'pip', 'install', 'flask_jwt_extended'])
import os
import unittest

# Add the starter_code directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'starter_code')))

# Discover and run tests
loader = unittest.TestLoader()
suite = loader.discover(start_dir='starter_code/tests', pattern='*_test.py')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
