from __future__ import print_function
try:
    from importlib import reload
except ImportError:
    try:
        from imp import reload
    except ImportError:
        pass
import copy
import traceback
import inspect
import re
import sys
import time
import glob
import struct
import random
import subprocess
import os.path
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
from functions import *
def ADD(a:int, b:int) -> int:
    return add(a, b)
def SUBTRACT(a:int, b:int) -> int:
    return subtract(a, b)
def MULTIPLY(a:int, b:int) -> int:
    return multiply(a, b)
# END STANDALONE CODE
