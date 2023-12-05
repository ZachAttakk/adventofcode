local utils = require "utils"

local input_file = "05.txt"
local inputs = utils.lines_from(input_file)


local function check_for_overlap(seed, con)
    -- seeds ahead, seeds overlap, seeds after
    local ahead = { -1, -1 }
    local overlap = { -1, -1 }
    local after = { -1, -1 }

    if seed[2] >= con.start_val and seed[1] <= con.end_val then
        -- there is an overlap
        local overlap_start = math.max(con.start_val, seed[1])
        local overlap_end = math.min(con.end_val, seed[2])
        overlap = { overlap_start, overlap_end }
        if overlap_start > seed[1] then
            ahead = { seed[1], math.min(seed[2], overlap_start) - 1 }
        end
        if overlap_end < seed[2] then
            after = { math.max(overlap_end, con.end_val) + 1, seed[2] }
        end
    elseif seed[2] <= con.start_val then
        -- we're ahead
        ahead = seed
    elseif seed[1] >= con.end_val then
        -- we're after
        after = seed
    end
    return ahead, overlap, after
end


local function make_seed_list(seeds)
    local seed_list = {}
    local values = seeds:split("%s")

    for i = 1, #values, 2 do
        table.insert(seed_list, { tonumber(values[i]), tonumber(values[i]) + tonumber(values[i + 1]) - 1 })
    end
    return seed_list
end

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

    -- make lookups
    for i = 2, #lines, 1 do
        local lookup = {}
        lookup.numbers = lines[i]:split("%s")
        lookup.start_val = tonumber(lookup.numbers[2])
        lookup.end_val = tonumber(lookup.numbers[2]) + tonumber(lookup.numbers[3]) - 1
        lookup.mod = tonumber(lookup.numbers[1]) - lookup.start_val
        table.insert(output.cons, lookup)
    end
    return output
end

local function process_lookup(data, lookup)
    print(string.format("Converting %s to %s", lookup.source_name, lookup.dest_name))
    local new_seeds = {}

    local seeds_left_to_process = data
    local new_seeds_to_process = {}
    while #seeds_left_to_process > 0 do
        for _, seed in pairs(seeds_left_to_process) do
            local processed = false
            for _, con in pairs(lookup.cons) do
                local ahead
                local overlap
                local after
                ahead, overlap, after = check_for_overlap(seed, con)
                if overlap[1] ~= -1 then
                    -- there's a part that needs to be converted
                    processed = true

                    table.insert(new_seeds, { overlap[1] + con.mod, overlap[2] + con.mod })
                    -- if there's a part of the range we didn't convert, it might still match other cons
                    if ahead[1] ~= -1 then
                        table.insert(new_seeds_to_process, ahead)
                    end
                    if after[1] ~= -1 then
                        table.insert(new_seeds_to_process, after)
                    end
                    break
                end
            end
            -- didn't find a match, pass it on
            if not processed then
                table.insert(new_seeds, seed)
            end
        end
        seeds_left_to_process = new_seeds_to_process
        new_seeds_to_process = {}
    end
    return new_seeds
end

-- DO THE CODE HERE

-- Make seeds list
local seeds = make_seed_list(inputs[1]:sub(8))

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

table.sort(seeds, function(a, b) return a[1] < b[1] end)

-- OUTPUT THE RESULT
print("")
print(seeds[1][1])
