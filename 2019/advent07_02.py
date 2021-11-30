import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils import utils as zUtils
from intcode_class import intcode
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
  #return [[(9,7,8,5,6),0]]
  #actual code
  a = [5,6,7,8,9]
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
  amps = []

  #start first amp
  while True:
    for amp_ind in range(0,5):
      i = phases[phase_ind][0][amp_ind]
      if amp_ind > len(amps)-1:
        amps.append(intcode("AMP " + chr(amp_ind+97).upper(), codes_original))
        amps[amp_ind].giveInput(i)
      amps[amp_ind].giveInput(last_result)
      last_result = amps[amp_ind].getOutput()
      zUtils.printDebug("Got back %s" % last_result)
    zUtils.printOK("Output: %s" % last_result)
    phases[phase_ind][1] = last_result
    if not amps[len(amps)-1].running:
      zUtils.printOK("Amps are done running. Final output: %s" % last_result)
      break
    else: zUtils.printOK("Amps are still running, looping again.")

  if last_result > phases[highest_index][1]: 
    highest_index = phase_ind


zUtils.printGood("Highest output phases: %s -- Result %s" % (phases[highest_index][0],phases[highest_index][1]))
zUtils.printOK("Time: %.2f seconds" % (timer()-start_time))