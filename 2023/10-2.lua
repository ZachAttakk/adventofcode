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
    if st_y == 1 then check_up = false end
    if st_y == #map then check_down = false end
    if st_x == 1 then check_left = false end
    if st_x == #map[1] then check_right = false end

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

local function invert_map(new, old)
    for y = 1, #old, 1 do
        for x = 1, #old[y], 1 do
            if new[y][x] ~= "*" then
                old[y][x] = "."
            end
        end
    end
    return old
end

local function deepcopy(o, seen)
    seen = seen or {}
    if o == nil then return nil end
    if seen[o] then return seen[o] end

    local no
    if type(o) == 'table' then
        no = {}
        seen[o] = no

        for k, v in next, o, nil do
            no[deepcopy(k, seen)] = deepcopy(v, seen)
        end
        setmetatable(no, deepcopy(getmetatable(o), seen))
    else -- number, string, boolean, etc
        no = o
    end
    return no
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

local original_map = deepcopy(map, false)

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
end

-- invert map to have only path
map = invert_map(map, original_map)
print_grid(map)

local inside_cell_count = 0

-- find cells inside path
for y = 1, #map, 1 do
    local inside = false
    for x = 1, #map[y], 1 do
        local cell = map[y][x]
        if table.contains(UP, cell) or table.contains(DOWN, cell) then
            inside = not inside
        end
        if map[y][x] == "." then
            map[y][x] = inside and "I" or "O"
            inside_cell_count = inside_cell_count + 1
        end
    end
end

print_grid(map)

-- OUTPUT THE RESULT
print("")
print(steps // 2)
timestamp()
