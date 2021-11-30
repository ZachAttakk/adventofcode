#INIT
weights = [94735, 80130, 127915, 145427, 89149, 91232, 100629, 97340, 86278, 87034, 147351, 123045, 91885, 85973, 64130, 113244, 58968, 76296, 127931, 98145, 120731, 98289, 110340, 118285, 60112, 57177, 58791, 59012, 66950, 139387, 145378, 86204, 147082, 84956, 134161, 148664, 74278, 96746, 144525, 81214, 70966, 107050, 134179, 138587, 80236, 139871, 104439, 64643, 145453, 94791, 51690, 94189, 148476, 79956, 81760, 149796, 109544, 57533, 142999, 126419, 115434, 57092, 64244, 109663, 94701, 109265, 145851, 95183, 84433, 53818, 106234, 127380, 149774, 59601, 138851, 54488, 100877, 136952, 61538, 67705, 60299, 130769, 113176, 106723, 133280, 111065, 63688, 139307, 122703, 60162, 89567, 63994, 66608, 126376, 136052, 112255, 98525, 134023, 141479, 98200]
#weights = [100756, 1969]



def get_fuel(weight):
  #to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
  fuel_amt = (weight // 3) - 2
  print("Weight:  %a Fuel: %f" % (weight,fuel_amt))
  return fuel_amt

print("Running...")

total = 0.0

for i in weights:
  print("New module: %s" % i)
  _fuel = i
  #recursion until 0 or negative
  while True:
    _fuel = get_fuel(_fuel)
    if _fuel <= 0: break
    total += _fuel

  print("Running total: %s" % total)

#we're done, print total
print("Total fuel used: %s" % total)
