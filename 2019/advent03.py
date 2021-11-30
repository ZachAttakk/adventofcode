import sys
import os
from timeit import default_timer as timer
from os import path

#FUNCTIONS
def manhattan(x1,y1,x2,y2):
  return (abs(x2-x1) + abs(y2-y1))

def get_inputs(filename):
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
data = get_inputs(sys.argv[1])
if (data == -1):
  print("NO FILE")

array = []

#HERE WE GO
for wire_count in range(0,len(data)):
  wire = data[wire_count]
  wire_line = []
  #we'll start in the centre
  starting_x = 0
  starting_y = 0

  #break the instructions into steps
  stripped_wire = wire.rstrip().split(",")
  print("Wire: %s" % wire.rstrip())
  x_off = 0
  y_off = 0

  #loop the individual instructions
  for i in stripped_wire:
    #print("Step: %s" % i)
    x_off = 0
    y_off = 0
    if i[0] == "R": x_off = 1
    elif i[0] == "L": x_off = -1
    elif i[0] == "D": y_off = -1
    elif i[0] == "U": y_off = 1
    else:
      print("Unknown instruction")

    #step through stripped wire and add them to the wire line
    for _step in range(0, int(i[1:])):  
      starting_x += x_off
      starting_y += y_off
      #print("Iterate: %s: %s,%s" % (_step,starting_x, starting_y))
      wire_line.append((starting_x,starting_y))

  #add the wire line to the array of lines
  print("Length: ", len(wire_line))
  array.append(wire_line)

# Now we find the intersections
dup = []

last_perc = 0.0
for _idx, _pos in enumerate(array[0]):
  #print("Looking for ", _pos)
  percent = ((_idx+1)/len(array[0]))*100
  if int(percent) != last_perc: 
        print(int(percent))
        last_perc = int(percent)

  if array[1].count(_pos) > 0:
    print("Intersection found: ", str(_pos))
    if dup.count(_pos) == 0:
      dup.append(_pos)

print("Intersections: ", len(dup))
#print(dup)
#find the shortest
final_dist = 10000
for sec in dup:
  print(sec)
  _dist = manhattan(sec[0],sec[1],0,0)
  print("Dist: ", _dist)
  if _dist < final_dist: final_dist = _dist


print("DONE: ", final_dist)
print("Time: %.2f seconds" % (timer()-start_time))