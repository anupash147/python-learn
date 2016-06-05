import os
import sys

# add package .zip to python lookup path
__dir__ = os.path.dirname(__file__)
path = os.path.join(__dir__, 'funniest')
sys.path.insert(0, path)

import funniest
print funniest.joke()
