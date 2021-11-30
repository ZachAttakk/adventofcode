import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils import utils as zUtils

data = {}
orbits = []
bodies = []

def get_data(filename):
  if path.exists(filename):
    f=open(filename, "r")
    if f.mode == 'r':
      _data =f.readlines()
      f.close()
      return _data
  else: return -1

  #INIT

def orbit_split(obj):
  split_index = str(obj).find(')')
  return (str(obj)[0:split_index],str(obj)[split_index+1:len(str(obj))])
  


def get_orbit(obj): #send one side, find the other
  target = ""
  for i in orbits:
    if str(i[1]) == str(obj): target = str(i[0])
  return target

def count_orbits(body):
  count = 0
  current_body = str(body)
  while True:
    current_body = get_orbit(str(current_body))
    if len(current_body) > 0: count += 1
    else: break
  return count

def list_orbits(body):
  orbs = []
  current_body = str(body)
  while True:
    current_body = get_orbit(str(current_body))
    if len(current_body) > 0: list.append(orbs,current_body)
    else: break
  return orbs

def body_exists(body):
  for i in bodies:
    if str(i[0]) == str(body): return True
  return False

# Code for startup
start_time = timer()
if len(sys.argv) < 2: filename = "advent06.txt"
else: filename = sys.argv[1]
data = get_data(filename)
if (data == -1):
  print("NO FILE")

# sanitize data
for i in range(0, len(data)):
  data[i] = data[i].rstrip()
  _new = orbit_split(str(data[i]))
  list.append(orbits,_new)
  if not body_exists(_new[0]): list.append(bodies, [str(_new[0]),0])
  if not body_exists(_new[1]): list.append(bodies, [str(_new[1]),0])

#HERE WE GO

#zUtils.printDebug(str(data))
zUtils.printDebug(str(orbits))

#for i in range(0,len(orbits)):
#  zUtils.printDebug(orbits[i][1] + " orbits " + orbits[i][0])

#for i in range(0,len(bodies)):
#  bodies[i][1] = count_orbits(str(bodies[i][0]))
#  zUtils.printDebug(bodies[i][0] + " orbits " + str(bodies[i][1]) + " things")

#total = 0
#for i in range(0,len(bodies)):
#  total += bodies[i][1]


#find the orbital sequence for YOU
you_orbs = list_orbits("YOU")
zUtils.printOK("YOU: %s" % str(you_orbs))

# find the orbital sequence for SAN

san_orbs = list_orbits("SAN")
zUtils.printOK("SAN: %s" % str(san_orbs))

answer = 0
# find where they overlap
for you_count in range(0, len(you_orbs)):
  zUtils.printOK("You looking for %s" % you_orbs[you_count])
  for san_count in range(0,len(san_orbs)):
    zUtils.printDebug("Is it %s?" % san_orbs[san_count])
    if you_orbs[you_count] == san_orbs[san_count]:
      zUtils.printGood("Yes it is!")
      zUtils.printOK("You is %s and SAN is %s" % (you_count, san_count))
      answer = san_count+you_count
      break
  if answer != 0 : break

zUtils.printGood("Transfer path: %s" % answer)



# count how many steps on each to reach the common point

#zUtils.printGood("Total: %s" % total)
zUtils.printOK("Time: %.2f seconds" % (timer()-start_time))