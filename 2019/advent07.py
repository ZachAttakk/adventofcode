import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils import utils as zUtils
from intcode import doCalc
from itertools import permutations

data = []
phases = []

def get_data(filename):
  if path.exists(filename):
    f=open(filename, "r")
    if f.mode == 'r':
      _data =f.readlines()
      f.close()
      return _data
  else: return None

def get_phase_list():
  #debug reasons
  #return [[(1,0,4,3,2),0]]
  #actual code
  a = [0,1,2,3,4]
  combinations = list(permutations(a, 5))

  _phases = []
  for i in combinations:
    list.append(_phases, [i,0])

  return _phases

#INIT
# Code for startup
start_time = timer()
if len(sys.argv) > 1: data = get_data(sys.argv[len(sys.argv)-1])[0]
else: data = get_data("advent07.txt")[0]

if (data == None):
  zUtils.printDisaster("NO FILE")

#HERE WE GO


codes_original = data.rstrip().split(",")

# Get a list of all the possible phases
phases = get_phase_list()


# Call intcode once for every phase, passing the last result along with the phase, saving the result in the list

highest_index = -1

for phase_ind in range(0,len(phases)):

  
  zUtils.printOK("Starting phase sequence: %s" % str(phases[phase_ind]))
  #each sequence of numbers has 5 numbers so we do the below 5 times, sending the last result with
  last_result = 0
  for i in phases[phase_ind][0]:
    zUtils.printDebug("Phase %s, sending %s" % (i, last_result))
    last_result = doCalc(codes_original, [i,last_result])
    zUtils.printDebug("Got back %s" % last_result)
  zUtils.printOK("Output: %s" % last_result)
  phases[phase_ind][1] = last_result
  if last_result > phases[highest_index][1]: 
    highest_index = phase_ind


zUtils.printGood("Highest output phases: %s -- Result %s" % (phases[highest_index][0],phases[highest_index][1]))
zUtils.printOK("Time: %.2f seconds" % (timer()-start_time))