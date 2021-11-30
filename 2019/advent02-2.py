#INIT
codes = []
original_codes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]


def add(a,b):
  _result = a + b
  #print("%s + %s = %s" % (a,b,_result))
  return _result

def multiply(a,b):
  _result = a * b
  #print("%s * %s = %s" % (a,b,_result))
  return _result

def run_op_codes(_noun,_verb):
  code_index = 0
  codes = list.copy(original_codes)
  print("codes reset. Params: ")
  codes[1] = _noun
  codes[2] = _verb

  while code_index < len(codes):
    op_code = codes[code_index]
    if op_code in [1,2]:
      first_num = codes[code_index+1]
      second_num = codes[code_index+2]
      target = codes[code_index+3]
      #print("Working %s and %s, saving to %s " % (first_num,second_num,target))
      if op_code == 1:
        codes[target] = add(codes[first_num],codes[second_num])
      else:
        codes[target] = multiply(codes[first_num],codes[second_num])
        #increase code index to skip parameters
      code_index += 4
    elif op_code == 99:
      print()
      #print("DONE. Result: %s" % str(codes)[1:-1])
      break
    else:
      #print("OP CODE %s UNKNOWN" % str(op_code))
      break
  return codes[0]

#HERE WE GO
print()
print("Running...")
found = False
for noun in range(0,100):
  if found: break
  print("Checking noun ",noun)
  for verb in range(0,100):
    if found: break
    print("Checking verb ",verb)
    result = run_op_codes(noun,verb)

    print("Execution result: %s" % result)
    if (result == 19690720):
      print("WE FOUND IT!")
      final_answer = 100 * noun + verb
      print ("Final answer: %s" % final_answer)
      found = True