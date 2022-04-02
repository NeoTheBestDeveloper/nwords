from setuptools import setup

setup(name='neowords',
      version='0.1.0',
      packages=['neowords'],
      entry_points={'console_scripts': ['nw = pycli.__main__:main']})
