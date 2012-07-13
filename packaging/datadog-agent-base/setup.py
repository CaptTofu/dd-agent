#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import os, sys

from distutils.command.install import INSTALL_SCHEMES

def getVersion():
    try:
        from config import get_version
    except ImportError:
        import sys
        sys.path.append("../..")
        from config import get_version
   
    return get_version()

def printVersion():
    print getVersion()

if __name__ == "__main__":

    setup(name='datadog-agent-base',
          version=getVersion(),
          description='Datatadog monitoring agent',
          author='Datadog',
          author_email='info@datadoghq.com',
          url='http://datadoghq.com/',
          packages=['resources', 'compat'],
          scripts=['agent.py', 'daemon.py', 'minjson.py', 'util.py', 
                    'emitter.py', 'config.py', 'graphite.py'],
          data_files=[('/etc/dd-agent/', ['../../datadog.conf.example'])] 
         )
