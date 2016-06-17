from setuptools import setup, find_packages

setup(name='v0lt',
      version='1.5.0.1',
      description='CTF oriented Toolkit',
      author='P1kachu',
      author_email='stanislas.lejay@epita.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4',
          'requests',
          'filemagic',
          'passlib',
          'hexdump'
      ],
      zip_safe=False)


#                      $$$$$
#                      $NNN$$$:
#                      $$$N  $$$7   7$$$$$$$
#                        $$>>>>$$$$$$$  NNN$
#                        :$$$::::::::>>>NOO$
#                           $:       >$$$$
#                          C>         $777
#                          $:Q:    $  $$$$$$$
#                          $:H:   :H  $?????$?
#                          $:N:   :H  $>>>>>$$
#                          $?       CC$>    >$
#                          $O       OO$7     $
#                          Q$>>>>>>>77$$  :::$
#                           $O::::::  >$ >$$$$
#                           $7 :::::>?$$ $$
#                           $$::::::  $?>$
#                            $: ::-  ???$$
#                            $$ C$$$7$$$$
#                             Q$$ :$$$
#                  ____  _ _              _
#                 |  _ \/ | | ____ _  ___| |__  _   _
#                 | |_) | | |/ / _` |/ __| '_ \| | | |
#                 |  __/| |   < (_| | (__| | | | |_| |
#                 |_|   |_|_|\_\__,_|\___|_| |_|\__,_|
