#!/usr/bin/python

from subprocess import call

call(['sudo','apt-get','install','solc'])
execfile('PythonModules/generateNode.py')
execfile('PythonModules/compileABI.py')

