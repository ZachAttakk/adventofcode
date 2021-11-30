#INIT
import zUtils.utils as zUtils
zUtils.outputDebug = False



def add(a,b):
  _result = a + b
  zUtils.printDebug("zUtil:%s + %s = %s" % (a,b,_result))
  return _result

def multiply(a,b):
  _result = a * b
  zUtils.printDebug("zUtil:%s * %s = %s" % (a,b,_result))
  return _result

def askUser(text):
  return int(input(text))

def doCalc(original_codes, parameters = None):
  codes = list.copy(original_codes)
  code_index = 0

  while code_index < len(codes) :
    zUtils.printDebug("zUtil:opcode: " + str(codes[code_index]))
    op_code = int(str(codes[code_index])[-2:])
    param_1_mode = 0
    param_2_mode = 0
    #param_3_mode = 0

    op_code_len = len(str(codes[code_index]))
    if op_code_len > 2:  #mode switches
      param_1_mode = int(str(codes[code_index])[-3:-2])
      if op_code_len > 3:
        param_2_mode = int(str(codes[code_index])[-4:-3])
        #if op_code_len > 4:
        # param_3_mode = int(str(codes[code_index])[-5:-4])

    #zUtils.printDebug("opcode: " + str(op_code))
    if op_code in [1,2,5,6,7,8]:
      first_num = int(codes[code_index+1])
      if not param_1_mode: first_num = int(codes[first_num])
      second_num = int(codes[code_index+2])
      if (not param_2_mode) and second_num < len(codes): second_num = int(codes[second_num])
      target = int(codes[code_index+3])

      zUtils.printDebug("zUtil:Working %s and %s, saving to %s " % (first_num,second_num,target))
      if op_code == 1: # add
        codes[target] = add(first_num, second_num)
        code_index += 4
      elif op_code == 2: # multiply
        codes[target] = multiply(first_num, second_num)
        code_index += 4
      elif op_code == 5: #jump if not zero
        if first_num != 0: code_index = second_num
        else: code_index += 3
      elif op_code == 6: #jump if zero
        if first_num == 0: code_index = second_num
        else: code_index += 3
      elif op_code == 7: #less than
        if first_num < second_num:
          codes[target] = 1
        else:
          codes[target] = 0
        code_index += 4
      elif op_code == 8: #equals
        if first_num == second_num:
          codes[target] = 1
        else:
          codes[target] = 0
        code_index += 4
    elif op_code == 3: # input
      first_num = int(codes[code_index+1])
      if len(parameters) <= 0:
        response = int(askUser("Please provide input:"))
      else: response = parameters.pop(0)
      zUtils.printDebug("zUtil:Setting %s to %s " % (first_num, response))
      codes[first_num] = response
      code_index += 2
    elif op_code == 4: # output
      first_num = int(codes[code_index+1])
      if not param_1_mode: first_num = int(codes[first_num])
      zUtils.printDebug("zUtil:Output: %s" % first_num)
      return first_num
      #code_index += 2
    elif op_code == 99: # done
      return("DONE")
    else:
      return("ERROR: OP CODE %s UNKNOWN" % str(op_code))