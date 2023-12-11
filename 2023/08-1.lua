local utils = require "utils"

local input_file = "08.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local instructions = inputs[1]
local nodes = {}

for i = 3, #inputs, 1 do
    local line = inputs[i]

    -- make the node
    local node_info = utils.split(line, "=")
    local connections = utils.split(node_info[2].sub(node_info[2], 2, #node_info[2] - 1), ",")
    local node = { L = connections[1], R = connections[2] }
    nodes[node_info[1]] = node
end

local step_count = 0
local instruction_index = 1
local current_node = "AAA"

-- traverse the network
while current_node ~= "ZZZ" do
    -- step to the next node
    local next_step = instructions:sub(instruction_index, instruction_index)
    print(string.format("%s --> %s", current_node, nodes[current_node][next_step]))
    current_node = nodes[current_node][next_step]
    step_count = step_count + 1

    -- go to next instruction
    instruction_index = instruction_index + 1
    -- start the instructions over
    if instruction_index > #instructions then
        instruction_index = 1
    end
end


-- OUTPUT THE RESULT
print("")
print(step_count)
