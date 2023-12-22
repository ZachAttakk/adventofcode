local utils = require "utils"

local input_file = "20.txt"
local inputs = utils.lines_from(input_file)

local pushes = 1

SIGNAL_COUNT_LOW = 0
SIGNAL_COUNT_HIGH = 0

local function send_signal(sender, signal, dest)
    if signal then
        SIGNAL_COUNT_HIGH = SIGNAL_COUNT_HIGH + 1
    else
        SIGNAL_COUNT_LOW = SIGNAL_COUNT_LOW + 1
    end
    local signal_str = "-low->"
    if signal then
        signal_str = "-high->"
    end
    print(string.format("%s %s %s", sender, signal_str, dest))

    table.insert(SIGNALS, { sender = sender, signal = signal, dest = dest })
end

local function flipflop(self, signal, sender)
    local outputs = {}
    if not signal then
        self.state = not self.state
        for _, out in ipairs(self.outputs) do
            send_signal(self.name, self.state, out)
        end
    end
    return outputs
end


local function conjunction(self, signal, sender)
    local outputs = {}
    -- find the state and save it
    self.inputs[sender] = signal

    self.state = false
    for index, value in pairs(self.inputs) do
        if not value then -- sending low pulse because one of them is low
            self.state = true
        end
    end
    -- if we reach here it means all inputs are high
    for _, out in ipairs(self.outputs) do
        send_signal(self.name, self.state, out)
    end
    return outputs
end

local function broadcast(self, signal, sender)
    local outputs = {}
    for _, out in ipairs(self.outputs) do
        send_signal(self.name, self.state, out)
    end
    return outputs
end

local function new_mod(name, op, outputs)
    local mod = {}
    mod.op = op
    mod.name = name
    mod.outputs = outputs
    mod.state = false -- false for low, true for high
    mod.inputs = {}   -- table used for saving states

    if mod.op == "%" then
        mod.process = flipflop
    elseif mod.op == "&" then
        mod.process = conjunction
    elseif mod.op == "b" then
        mod.process = broadcast
    end
    return mod
end

local function new_mod_from_str(str)
    local values = utils.split(str, "%s")
    local op = values[1]:sub(1, 1)
    local name = values[1]:sub(2, #values[1])
    local outputs = utils.split(str:sub(str:find(">") + 2, #str), ",")
    return new_mod(name, op, outputs)
end
-- DO THE CODE HERE

MODULES = {}
SIGNALS = {}
local broadcast_to = utils.split(inputs[1]:sub(inputs[1]:find("->") + 3, #inputs[1]), ",")
MODULES["broadcaster"] = new_mod("broadcaster", "b", broadcast_to)
for i = 2, #inputs, 1 do
    local mod_name = inputs[i]:sub(2, inputs[i]:find("-") - 2)
    MODULES[mod_name] = new_mod_from_str(inputs[i])
end

-- prep the conjuntions
for index, mod in pairs(MODULES) do
    if mod.op == "&" then
        for key, dest in pairs(MODULES) do
            if table.contains(dest.outputs, mod.name) then
                mod.inputs[dest.name] = false
            end
        end
    end
end

-- then we go
local s = os.clock()
for i = 1, pushes, 1 do
    print(i)
    send_signal("button", false, "broadcaster")
    while #SIGNALS > 0 do
        if MODULES[SIGNALS[1].dest] then
            MODULES[SIGNALS[1].dest]:process(SIGNALS[1].signal, SIGNALS[1].sender)
        end
        table.remove(SIGNALS, 1)
    end
    utils.timestamp(s)
    print("")
    s = os.clock()
end

-- OUTPUT THE RESULT
print("")
print.green(SIGNAL_COUNT_HIGH * SIGNAL_COUNT_LOW)
utils.timestamp()
