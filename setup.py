from setuptools import setup, find_packages

setup(name='v0lt',
      version='1.3',
      description='CTF oriented Toolkit',
      author='P1kachu',
      author_email='stanislas.lejay@epita.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4',
          'requests',
          'filemagic',
          'hexdump'
      ],
      zip_safe=False)
