local utils = require "utils"

local input_file = "15.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function add_char(char, last_val)
    if last_val == nil then last_val = 0 end
    --Determine the ASCII code for the current character of the string.
    local ascii = string.byte(char)
    --Increase the current value by the ASCII code you just determined.
    last_val = last_val + ascii
    --Set the current value to itself multiplied by 17.
    last_val = last_val * 17
    --Set the current value to the remainder of dividing itself by 256.
    last_val = last_val % 256

    return last_val
end

local function get_hash(str)
    local chars = utils.split(str)
    local total = 0
    for _, char in ipairs(chars) do
        total = add_char(char, total)
    end
    return total
end

local data = utils.split(inputs[1], ",")

local total = 0
for _, value in ipairs(data) do
    total = total + get_hash(value)
end


-- OUTPUT THE RESULT
print("")
print.green(total)
utils.timestamp()
