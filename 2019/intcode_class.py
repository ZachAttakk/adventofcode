#INIT
import zUtils.utils as zUtils
zUtils.outputDebug = True


class intcode():


  def __init__(self,name,original_codes):
    self.name = name
    self.codes = list.copy(original_codes)
    self.code_index = 0
    self.outputs = []
    self.parameters = []
    self.running = True
    self.doCalc()


  def add(self,a,b):
    _result = a + b
    zUtils.printDebug(self.name + ": %s + %s = %s" % (a,b,_result))
    return _result

  def multiply(self,a,b):
    _result = a * b
    zUtils.printDebug(self.name + ": %s * %s = %s" % (a,b,_result))
    return _result

  def getOutput(self):
    if len(self.outputs): return self.outputs.pop(0)
    else: return None

  def giveInput(self, value):
    zUtils.printDebug(self.name + ": Input received: %s" % value)
    list.append(self.parameters, value)
    self.doCalc()

  def doCalc(self):

    while self.code_index < len(self.codes) :
      zUtils.printDebug(self.name + ": opcode: " + str(self.codes[self.code_index]))
      op_code = int(str(self.codes[self.code_index])[-2:])
      param_1_mode = 0
      param_2_mode = 0
      #param_3_mode = 0

      op_code_len = len(str(self.codes[self.code_index]))
      if op_code_len > 2:  #mode switches
        param_1_mode = int(str(self.codes[self.code_index])[-3:-2])
        if op_code_len > 3:
          param_2_mode = int(str(self.codes[self.code_index])[-4:-3])
          #if op_code_len > 4:
          # param_3_mode = int(str(codes[code_index])[-5:-4])

      #zUtils.printDebug("opcode: " + str(op_code))
      if op_code in [1,2,5,6,7,8]:
        first_num = int(self.codes[self.code_index+1])
        if not param_1_mode: first_num = int(self.codes[first_num])
        second_num = int(self.codes[self.code_index+2])
        if (not param_2_mode) and second_num < len(self.codes): second_num = int(self.codes[second_num])
        target = int(self.codes[self.code_index+3])

        zUtils.printDebug(self.name + ": Working %s and %s, saving to %s " % (first_num,second_num,target))
        if op_code == 1: # add
          self.codes[target] = self.add(first_num, second_num)
          self.code_index += 4
        elif op_code == 2: # multiply
          self.codes[target] = self.multiply(first_num, second_num)
          self.code_index += 4
        elif op_code == 5: #jump if not zero
          if first_num != 0: self.code_index = second_num
          else: self.code_index += 3
        elif op_code == 6: #jump if zero
          if first_num == 0: self.code_index = second_num
          else: self.code_index += 3
        elif op_code == 7: #less than
          if first_num < second_num:
            self.codes[target] = 1
          else:
            self.codes[target] = 0
          self.code_index += 4
        elif op_code == 8: #equals
          if first_num == second_num:
            self.codes[target] = 1
          else:
            self.codes[target] = 0
          self.code_index += 4
      elif op_code == 3: # input
        first_num = int(self.codes[self.code_index+1])
        if len(self.parameters) <= 0:
          zUtils.printDebug(self.name + ": Waiting for input...")
          break
        else:
          response = self.parameters.pop(0)
          zUtils.printDebug(self.name + ": Setting %s to %s " % (first_num, response))
          self.codes[first_num] = response
          self.code_index += 2
      elif op_code == 4: # output
        first_num = int(self.codes[self.code_index+1])
        if not param_1_mode: first_num = int(self.codes[first_num])
        zUtils.printDebug(self.name + ": Output: %s" % first_num)
        list.append(self.outputs,first_num)
        self.code_index += 2
      elif op_code == 99: # done
        zUtils.printOK(self.name + ": DONE")
        self.running = False
        break
      else:
        return("ERROR: OP CODE %s UNKNOWN" % str(op_code))