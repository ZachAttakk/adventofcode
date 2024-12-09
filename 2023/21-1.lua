local utils = require "utils"
local aStar = require("AStar")

local input_file = "21.txt"
local inputs = utils.lines_from(input_file)

STEP_LIMIT = 64

local function manhattan(x1, y1, x2, y2)
    return math.abs(y2 - y1) + math.abs(x2 - x1)
end

local function expand(n)
    local neighbours = {}
    local coords = utils.split_to_nums(n, ",")
    for y = coords[2] - 1, coords[2] + 1, 1 do
        if y >= 1 and y <= HEIGHT then
            for x = coords[1] - 1, coords[1] + 1, 1 do
                if x >= 1 and x <= WIDTH and (x == coords[1] or y == coords[2]) and not (x == coords[1] and y == coords[2]) then
                    local node_name = string.format("%03d,%03d", x, y)
                    -- walkable is absolute so handle it here
                    if GRAPH[node_name] ~= "#" then
                        table.insert(neighbours, node_name)
                    end
                end
            end
        end
    end
    return neighbours
end

local function cost(from)
    return function(to)
        return 1
    end
end

local function heuristic(n)
    return 0
end

local goal = function(n)
    -- how do I know when the goal is reached?
    -- what if I do it backwards? Make the start node the goal?
    -- then I can work from each node to start...
    return GRAPH[n] == "S"
end

-- DO THE CODE HERE

local data = {}
for index, value in ipairs(inputs) do
    table.insert(data, utils.split(value))
end

-- convert data to usable graph
WIDTH = #data[1]
HEIGHT = #data
GRAPH = {}
local start_node = { 0, 0 }
for y = 1, #data, 1 do
    for x = 1, #data[1], 1 do
        GRAPH[string.format("%03d,%03d", x, y)] = data[y][x]
        if data[y][x] == "S" then
            start_node = { x, y }
        end
    end
end

local simpleAStar = aStar(expand)(cost)(heuristic)

-- NOW WE RUN IT
local destinations = {}
local halfway_mark = 0
for y = 1, HEIGHT, 1 do
    for x = 1, WIDTH, 1 do
        if data[y][x] == "S" then
            -- we're halfway
            halfway_mark = os.clock()
        end
        if data[y][x] == "." and manhattan(start_node[1], start_node[2], x, y) <= STEP_LIMIT then
            local node_name = string.format("%03d,%03d", x, y)
            print(node_name)
            utils.timestamp()
            if halfway_mark > 0 then
                print("ETA: " .. utils.format_time(halfway_mark * 2 - os.clock()))
            end
            local path = simpleAStar(goal)(node_name)
            if path == nil then
                -- Didn't find a path
            else
                if path ~= nil and #path - 1 == STEP_LIMIT or (#path - 1 < STEP_LIMIT and (#path - 1) % 2 == STEP_LIMIT % 2) then
                    table.insert(destinations, { path[1], #path - 1 })
                end
            end
        end
    end
end
-- if it's an even number of steps, we can also reach the original spot
if STEP_LIMIT % 2 == 0 then
    table.insert(destinations, "start")
end

-- OUTPUT THE RESULT
print("")
print.green(#destinations)
utils.timestamp()
