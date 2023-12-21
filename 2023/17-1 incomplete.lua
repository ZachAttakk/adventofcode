local utils = require "utils"
local aStar = require "AStar"

local input_file = "17.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function convert_data_to_grid(data)
    local grid = {}
    for y = 1, #data, 1 do
        for x = 1, #data[y], 1 do
            table.insert(row, { x = x, y = y, cost = data[y][x] })
        end
    end
end

local function expand(n)
    return graph[n]
end

local function cost(from)
    return function(to)
        return 1
    end
end

local function heuristic(n)
    return 0
end

local goalD = function(n)
    return n == "D"
end

local data = {}
for index, value in ipairs(inputs) do
    table.insert(data, utils.split_to_nums(value))
end

local grid = convert_data_to_grid(data)



-- OUTPUT THE RESULT
print("")
print.green("OUTPUT GOES HERE")
utils.timestamp()
