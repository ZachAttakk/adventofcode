local utils = require "utils"

local input_file = "05.txt"
local inputs = utils.lines_from(input_file)

local function parse_lookup(lines)
    --[[ example data:
        seed-to-soil map:
        50 98 2
        52 50 48
    ]]

    local output = {}

    -- first line is the name of the lookup
    local names = lines[1]:split("-")
    output.source_name = names[1]
    output.dest_name = names[3]:sub(1, #names[3] - 5)
    output.cons = {}

    -- process lookups
    for i = 2, #lines, 1 do
        local lookup = {}
        lookup.numbers = lines[i]:split("%s")
        lookup.start_dest = tonumber(lookup.numbers[1])
        lookup.start_source = tonumber(lookup.numbers[2])
        lookup.range = tonumber(lookup.numbers[3])
        table.insert(output.cons, lookup)
    end
    return output
end

local function process_lookup(data, lookup)
    print(string.format("Converting %s to %s", lookup.source_name, lookup.dest_name))

    local new_seeds = {}
    for _, seed in pairs(data) do
        local new_seed_value = -1
        for _, value in pairs(lookup.cons) do
            if tonumber(seed) >= value.start_source and tonumber(seed) <= value.start_source + value.range then
                new_seed_value = seed - value.start_source + value.start_dest
                break
            end
        end
        if new_seed_value >= 0 then
            table.insert(new_seeds, new_seed_value)
        else
            table.insert(new_seeds, tonumber(seed))
        end
    end
    return new_seeds
end

-- DO THE CODE HERE

-- Make seeds list
local seeds = inputs[1]:sub(8):split("%s")

-- grab each lookup and add it to a table
local lookups = {}
local lookup_input = {}
-- go one over to trigger the last lookup add
for i = 3, #inputs + 1, 1 do
    if inputs[i] == "" or i > #inputs then
        table.insert(lookups, parse_lookup(lookup_input))
        lookup_input = {}
    else
        table.insert(lookup_input, inputs[i])
    end
end

-- send the seeds list through all the lookups (destructively)

for _, lookup in pairs(lookups) do
    seeds = process_lookup(seeds, lookup)
end

table.sort(seeds)

-- OUTPUT THE RESULT
print("")
print(seeds[1])
