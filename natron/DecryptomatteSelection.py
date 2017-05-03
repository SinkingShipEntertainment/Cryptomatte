# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named DecryptomatteSelectionExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from DecryptomatteSelectionExt import *
except ImportError:
    pass

try:
    from CryptomatteExt import *
except ImportError:
    print "Fail"

def getPluginID():
    return "com.Cryptomatte.pyplug.DecryptomatteSelection"

def getLabel():
    return "DecryptomatteSelection"

def getVersion():
    return 1

def getIconPath():
    return "cryptomatte_logo.png"

def getGrouping():
    return "Keyer/Cryptomatte"

def getPluginDescription():
    return "This plugin can be used to convert selected Cryptomatte nodes into expressions."

def getIsToolset():
    return True

def createInstance(app,group):
    print "Called DecryptomatteSelection"

    decryptomatte_selected(app)
    