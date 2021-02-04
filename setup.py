#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='acc',
    version="0.2",
    description='acc is the Abilian Cloud Controller',
    author='Stefane Fermigier',
    author_email='sf@abilian.com',
    url='https://github.com/abilian/abilian-cloud-controler',
    packages=find_packages(),
    # Not needed (yet?)
    #data_files=[('acc', ['config/nginx.conf']),],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'acc = acc.main:main',
            'abilianwrapper = acc.abilianwrapper:main',
        ]
    },
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: System :: Systems Administration',
    ],
)
