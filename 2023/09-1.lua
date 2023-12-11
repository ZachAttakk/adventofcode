local utils = require "utils"

local input_file = "09.txt"
local inputs = utils.lines_from(input_file)

local function timestamp()
    print(string.format("Elapsed time: %.3f seconds", os.clock()))
end

-- DO THE CODE HERE


local function all_zero(list)
    for _, value in ipairs(list) do
        if value ~= 0 then return false end
    end
    return true
end

local function print_numbers(sequence)
    -- for debug
    for i, line in ipairs(sequence) do
        local str = string.rep("  ", i)
        for _, value in ipairs(line) do
            str = str .. string.format("%8d", value)
        end
        print(str)
    end
    print(" ")
end

local data = {}

for index, value in ipairs(inputs) do
    table.insert(data, { utils.split_to_nums(value, "%s") })
end

timestamp()
-- extrapolate differences
-- for each line in data
for i, sequence in ipairs(data) do
    local nums_count = 1
    local cur_sequence = sequence[nums_count]
    while not all_zero(cur_sequence) do
        cur_sequence = {}
        for n = 2, #sequence[nums_count], 1 do
            table.insert(cur_sequence, sequence[nums_count][n] - sequence[nums_count][n - 1])
        end
        table.insert(sequence, cur_sequence)
        nums_count = nums_count + 1
    end
end

local final_numbers = {}

-- calculate missing number for each
for _, sequence in pairs(data) do
    table.insert(sequence[#sequence], 0)
    for i = #sequence - 1, 1, -1 do
        table.insert(sequence[i], sequence[i][#sequence[i]] + sequence[i + 1][#sequence[i + 1]])
    end
    table.insert(final_numbers, sequence[1][#sequence[1]])
end

-- OUTPUT THE RESULT
print("")
print(utils.sum(final_numbers))
timestamp()
