local utils = require "utils"

local input_file = "14.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function print_grid(grid)
    for y, line in ipairs(grid) do
        print.gray(table.concat(line))
    end
end

local data = {}
for index, value in ipairs(inputs) do
    table.insert(data, utils.split(value))
end

for y = 2, #data, 1 do
    for x = 1, #data[1], 1 do
        if data[y][x] == "O" then
            -- we found a rock
            -- scan up until we find where it comes to rest
            for new_y = y - 1, 0, -1 do
                if new_y == 0 or data[new_y][x] == "O" or data[new_y][x] == "#" then
                    data[y][x] = "."
                    data[new_y + 1][x] = "O"
                    break
                end
            end
        end
    end
end

print_grid(data)

local total_weight = 0

-- now we calculate the weight
for y = 1, #data, 1 do
    for x = 1, #data[1], 1 do
        if data[y][x] == "O" then
            total_weight = total_weight + #data - y + 1
        end
    end
end

-- OUTPUT THE RESULT
print("")
print.green(total_weight)
utils.timestamp()
