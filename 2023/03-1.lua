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

local function check_neighbours(data, y_pos, x_pos_start, num_x_pos_end)
    -- if any neighbour of a number is a symbol return true
    for _y = y_pos - 1, y_pos + 1, 1 do
        if _y >= 1 and _y <= #data then
            for _x = x_pos_start - 1, num_x_pos_end + 1, 1 do
                -- ignore the number itself
                if _x >= 1 and _x <= #data[_y] and (_y ~= y_pos or not (_x >= x_pos_start and _x <= num_x_pos_end)) then
                    if data[_y][_x] ~= "." then
                        return true
                    end
                end
            end
        end
    end
    return false
end

-- get the whole number, then check its neighbours
-- first keep it a string until we have the whole number
-- it's easier to find numbers in strings so we check original inputs
local total_part_number = 0
for line_index, line in pairs(inputs) do
    -- it's easier to find full numbers in the original string
    local last_match = 0
    while last_match < #line do
        local start_index, end_index = line:find("%d+", last_match + 1)
        -- stop when we find the last number
        if start_index == nil then break end

        last_match = end_index
        local found_number = tonumber(line:sub(start_index, end_index))
        print(found_number)
        -- now we check whether we should add it or not
        if check_neighbours(data, line_index, start_index, end_index) then
            -- ok we add it
            print(tostring(found_number) .. " added")
            total_part_number = total_part_number + found_number
        end
    end
    print(" ---- ")
end

-- OUTPUT THE RESULT
print("")
print(total_part_number)
