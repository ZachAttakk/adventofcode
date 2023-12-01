local utils = require "utils"

local input_file = "01.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

outputs = {}

for _, value in pairs(inputs) do
    -- find the numbers in each line
    local nums = {}
    for w in string.gmatch(value, "%d") do
        table.insert(nums, w)
    end

    -- add the first and last number
    table.insert(outputs, nums[1] .. nums[#nums])
end

-- add them all up

local total = 0

for index, value in pairs(outputs) do
    print(index, value)
    total = total + tonumber(value)
end


-- OUTPUT THE RESULT
print("")
print(total)
