from setuptools import setup

DESCRIPTION = "View pretty tables in IPython"
LONG_DESCRIPTION = DESCRIPTION
NAME = "itable"
AUTHOR = "Melissa Gymrek"
AUTHOR_EMAIL = "mgymrek@mit.edu"
MAINTAINER = "Melissa Gymrek"
MAINTAINER_EMAIL = "mgymrek@mit.edu"
DOWNLOAD_URL = 'http://github.com/mgymrek/itable'
LICENSE = 'MIT'

VERSION = '0.0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=DOWNLOAD_URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['itable'],
      package_dir={'itable': 'itable'},
      install_requires=['pandas','numpy'],
      classifiers=['Development Status :: 4 - Beta',\
                       'Programming Language :: Python :: 2.6',\
                       'License :: OSI Approved :: MIT License',\
                       'Operating System :: OS Independent',\
                       'Topic :: Scientific/Engineering :: Visualization']
     )
