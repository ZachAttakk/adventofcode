local utils = require "utils"

local input_file = "10.txt"
local inputs = utils.lines_from(input_file)

local function timestamp()
    print(string.format("Elapsed time: %.3f seconds", os.clock()))
end

-- DO THE CODE HERE

UP = { "|", "F", "7" }
DOWN = { "|", "J", "L" }
LEFT = { "L", "F", "-" }
RIGHT = { "J", "7", "-" }

local function find_connection(map, cur_pipe, st_x, st_y)
    local check_up, check_down, check_left, check_right = true, true, true, true
    if cur_pipe ~= "S" then
        check_up = table.contains(DOWN, cur_pipe)
        check_down = table.contains(UP, cur_pipe)
        check_left = table.contains(RIGHT, cur_pipe)
        check_right = table.contains(LEFT, cur_pipe)
    end

    if check_up and table.contains(UP, map[st_y - 1][st_x]) then
        return st_x, st_y - 1
    elseif check_left and table.contains(LEFT, map[st_y][st_x - 1]) then
        return st_x - 1, st_y
    elseif check_down and table.contains(DOWN, map[st_y + 1][st_x]) then
        return st_x, st_y + 1
    elseif check_right and table.contains(RIGHT, map[st_y][st_x + 1]) then
        return st_x + 1, st_y
    end

    return 0, 0
end

local function find_start(grid)
    for y = 1, #grid, 1 do
        for x = 1, #grid[1], 1 do
            if grid[y][x] == "S" then return x, y end
        end
    end
    return 0, 0
end

local function print_grid(grid)
    for y, line in ipairs(grid) do
        print(table.concat(line))
    end
    print(" ")
end

-- build map
local map = {}
for index, value in ipairs(inputs) do
    table.insert(map, utils.split(value))
end

print_grid(map)

-- find the first connection
local cur_x, cur_y = find_start(map)
local pipes_list = {}
local steps = 0
-- keep going until we don't find anything
while cur_x ~= 0 do
    steps = steps + 1
    table.insert(pipes_list, map[cur_y][cur_x])
    map[cur_y][cur_x] = "*" -- to mark visited
    cur_x, cur_y = find_connection(map, pipes_list[#pipes_list], cur_x, cur_y)
    --print_grid(map)
end
-- whole path is this lenght, so return half

--print_grid(map)

-- OUTPUT THE RESULT
print("")
print(steps // 2)
timestamp()
