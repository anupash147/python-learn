import os
import sys

# add package .zip to python lookup path
__dir__ = os.path.dirname(__file__)
path = os.path.join(__dir__, 'funniest')
sys.path.insert(0, path)

import funniest
print funniest.joke()
print "I am not funny"

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print args.echo
