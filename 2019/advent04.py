from timeit import default_timer as timer
start_time = timer()




start_value = 254032
end_value = 789860
count = 0



for i in range(start_value, end_value):
  number_string = str(i)
  has_double = False
  has_decreasing = False

  # Loop characters
  for char_idx in range(0,len(number_string)-1):
    # Check for double
    if number_string[char_idx] == number_string[char_idx+1]:
      has_double = True
    # Check for decreasing digits
    if int(number_string[char_idx]) > int(number_string[char_idx+1]):
      #print(int(number_string[char_idx]), int(number_string[char_idx+1]))
      has_decreasing = True

  if (has_double) and (not has_decreasing):
    # if we get here, all validation has passed
    print(i)
    count += 1



print("Done: ", count)

print("Time: %.2f seconds" % (timer()-start_time))