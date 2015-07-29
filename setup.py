from setuptools import setup

setup(name='v0lt',
      version='0.3',
      description='CTF oriented Tools',
      author='P1kachu',
      author_email='stanislas.lejay@epita.fr',
      license='MIT',
      packages=['v0lt'],
      install_requires=[
          'beautifulsoup4',
          'requests',
      ],
      zip_safe=False)
