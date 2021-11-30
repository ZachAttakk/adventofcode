import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils import utils as zUtils
from intcode import doCalc

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
if len(sys.argv) > 1: data = get_data(sys.argv[len(sys.argv)-1])[0]
else: data = get_data("advent05.txt")[0]

if (data == -1):
  zUtils.printDisaster("NO FILE")

#HERE WE GO
codes = data.rstrip().split(",")
output = doCalc(codes)
if output.startswith("DONE"): zUtils.printGood(output)
elif output.startswith("ERROR"): zUtils.printDisaster(output)
else: zUtils.printOK(output)



zUtils.printOK("Time: %.2f seconds" % (timer()-start_time))