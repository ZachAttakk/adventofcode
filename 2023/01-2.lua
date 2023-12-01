local utils = require "utils"

local input_file = "01.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

-- this works because lua indexes from one
NUMBERS = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" }

outputs = {}

for line_index, value in pairs(inputs) do
    -- find the numbers in each line
    local nums = ""

    local last_found = 1

    while last_found <= #value do
        -- first find the first word
        local first_word_index = math.maxinteger
        local first_word_found = 0
        for index, word in pairs(NUMBERS) do
            local found = string.find(value, word, last_found)
            if found ~= nil and found < first_word_index then
                first_word_index = found
                first_word_found = index
            end
        end

        -- then find the first digit
        local first_digit_index = string.find(value, "%d", last_found)

        -- use the one that's smaller
        if first_digit_index ~= nil and first_digit_index < first_word_index then
            nums = nums .. string.sub(value, first_digit_index, first_digit_index)
            -- apparently the names of words can overlap.
            -- good thing someone posted it on reddit...
            last_found = first_digit_index + 1
        elseif first_word_index < math.maxinteger then
            nums = nums .. first_word_found
            last_found = first_word_index + 1
        else
            -- no more numbers found
            break
        end
    end

    -- add the first and last number
    table.insert(outputs, string.sub(nums, 1, 1) .. string.sub(nums, #nums))
    print(line_index, outputs[line_index], nums, value)
end

-- add them all up

local total = 0

for index, value in pairs(outputs) do
    total = total + tonumber(value)
end


-- OUTPUT THE RESULT
print("")
print(total)
