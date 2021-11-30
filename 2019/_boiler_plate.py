import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils import utils as zUtils

data = []

def get_data(filename):
  if path.exists(filename):
    f=open(filename, "r")
    if f.mode == 'r':
      _data =f.readlines()
      f.close()
      return _data
  else: return -1

  #INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2: filename = "advent06.txt"
else: filename = sys.argv[1]
data = get_data(filename)
if (data == -1):
  print("NO FILE")

array = []

#HERE WE GO





zUtils.printOK("Time: %.2f seconds" % (timer()-start_time))