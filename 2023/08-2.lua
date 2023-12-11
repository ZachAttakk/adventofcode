local utils = require "utils"

local input_file = "08.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function get_start_nodes(nodes)
    local node_list = {}
    for node_name, cons in pairs(nodes) do
        if node_name:endswith("A") then
            table.insert(node_list, node_name)
        end
    end
    return node_list
end

local function find_factor(list, num)
    for id, value in ipairs(list) do
        if value[1] == num then
            return id, value[2]
        end
    end
    return nil, 0
end

local function prime_factors(value)
    local factors = {}
    for i = 2, value, 1 do
        while value % i == 0 do
            value = value / i
            if utils.is_prime(i) then
                local fac_id, cur_fac = find_factor(factors, i)
                if cur_fac == 0 then
                    table.insert(factors, { i, 1 })
                elseif cur_fac < factors[fac_id][2] then
                    factors[fac_id][2] = factors[fac_id][2] + 1
                end
            end
        end
    end
    if value == 1 then
        return factors
    end
end

local function lcm(list)
    -- Find all the prime factors of each given number and write them in exponent form.
    -- List all the prime numbers found, using the highest exponent found for each.
    -- Multiply the list of prime factors with exponents together to find the LCM.
    local factor_list = {}
    for _, num in ipairs(list) do
        local facs = prime_factors(num)
        for i = 1, #facs, 1 do
            local fac_id, cur_fac = find_factor(factor_list, facs[i][1])
            if cur_fac == 0 then
                table.insert(factor_list, facs[i])
            elseif cur_fac < factor_list[fac_id][2] then
                factor_list[fac_id][2] = facs[2]
            end
        end
    end

    local mult_step_list = {}
    for _, value in pairs(factor_list) do
        table.insert(mult_step_list, value[1] ^ value[2])
    end

    return utils.multiply(mult_step_list)
end

local function get_dist(current_node)
    local step_count = 0
    local instruction_index = 1

    while not current_node:endswith("Z") do
        local next_step = Instructions:sub(instruction_index, instruction_index)
        print(string.format("%s --> %s", current_node, Nodes[current_node][next_step]))
        current_node = Nodes[current_node][next_step]
        step_count = step_count + 1

        -- go to next instruction
        instruction_index = instruction_index + 1
        -- start the instructions over
        if instruction_index > #Instructions then
            instruction_index = 1
        end
    end
    return step_count
end


Instructions = inputs[1]
Nodes = {}

for i = 3, #inputs, 1 do
    local line = inputs[i]

    -- make the node
    local node_info = utils.split(line, "=")
    local connections = utils.split(node_info[2].sub(node_info[2], 2, #node_info[2] - 1), ",")
    local node = { L = connections[1], R = connections[2] }
    Nodes[node_info[1]] = node
end

-- get all the starting nodes
local start_nodes = get_start_nodes(Nodes)


-- traverse the network
local distances = {}
for _, node_name in ipairs(start_nodes) do
    table.insert(distances, get_dist(node_name))
end



-- OUTPUT THE RESULT
print(" ")
print(lcm(distances))



print(string.format("Elapsed time: %.2f seconds", os.clock()))
