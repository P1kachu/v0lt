from setuptools import setup, find_packages

setup(name='v0lt',
      version='1.2.8',
      description='CTF oriented Toolkit',
      author='P1kachu',
      author_email='stanislas.lejay@epita.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4',
          'requests',
          'filemagic',
      ],
      zip_safe=False)
