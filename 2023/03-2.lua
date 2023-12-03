local utils = require "utils"

local input_file = "03.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local data = {}
for index, value in ipairs(inputs) do
    -- First we break it into infividual cells.
    local row = {}
    for i = 1, #value, 1 do
        table.insert(row, string.sub(value, i, i))
    end
    table.insert(data, row)
end
-- data is now a 2D array

local function check_neighbours(inputs, y_pos, x_pos)
    -- if any neighbour of a number is a symbol return true
    local found_numbers = {}
    for _y = y_pos - 1, y_pos + 1, 1 do
        if _y >= 1 and _y <= #inputs then
            -- find the numbers in the line and if they're adjacent we add them to the list
            local last_match = 0
            while last_match < #inputs[_y] do
                local start_index, end_index = inputs[_y]:find("%d+", last_match)
                if start_index == nil then break end
                last_match = end_index + 1
                if start_index <= x_pos + 1 and end_index >= x_pos - 1 then
                    -- number is adjacent
                    table.insert(found_numbers, tonumber(inputs[_y]:sub(start_index, end_index)))
                end
            end
        end
    end

    -- check if it's 2 numbers, return product, otherwise return 0
    if #found_numbers == 2 then
        return found_numbers[1] * found_numbers[2]
    else
        return 0
    end
    return false
end

local gears = {}
-- get the gear, then check its neighbours for numbers
-- first keep it a string until we have the whole number
for line_index, line in pairs(inputs) do
    -- it's easier to find full numbers in the original string
    local last_match = 0
    while last_match < #line do
        local gear_x = string.find(line, "*", last_match)
        -- break if we found the last one
        if gear_x == nil then break end
        last_match = gear_x + 1
        table.insert(gears, check_neighbours(inputs, line_index, gear_x))
    end
end

-- OUTPUT THE RESULT
print("")
print(utils.sum(gears))
