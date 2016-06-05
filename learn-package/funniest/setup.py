from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      data_files=[ ('', ['__main__.py', ])],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/funniest-joke'],
      zip_safe=False)
