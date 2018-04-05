"""Set up script"""
from distutils.core import setup

setup(name="fryptos",
      version='0.0.1',
      description='Encrypt files.',
      # long_description="",
      # classifiers=[],
      keywords='encrypt'
      author='Shohei Mukai',
      author_email='mukaishohei76@gmail.com',
      py_modules=['main'],
      packages=['fryptos'],
      entry_points={
          'console_scripts': [
              ],
          },
      licence='MIT',
      # install_requires=[],
      # test_suite=''
      )

