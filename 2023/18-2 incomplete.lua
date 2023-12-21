local utils = require "utils"

local input_file = "18.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function add_to_set(set, val)
    for _, s in pairs(set) do
        if s[1] == val[1] and s[2] == val[2] then
            return set
        end
    end
    table.insert(set, val)
    return set
end

local function check_neighbours(grid, pos, t, b, l, r)
    local neighbours = {}
    for y = math.max(pos[2] - 1, t), math.min(pos[2] + 1, b), 1 do
        for x = math.max(pos[1] - 1, l), math.min(pos[1] + 1, r), 1 do
            if not grid[y][x] then
                table.insert(neighbours, { x, y })
            end
        end
    end
    return neighbours
end

local function fill_grid(grid, t, b, l, r)
    -- changing to flood fill
    local st = { t + 1, l + 1 }
    local found = false
    for y = t + 1, b, 1 do
        for x = l + 1, r, 1 do
            if grid[y - 1][x] and grid[y][x - 1] then
                -- we're inside the first wall
                st = { x, y }
                found = true
            end
            break
        end
        if found then break end
    end
    -- flood fill
    local neighbours = check_neighbours(grid, st, t, b, l, r)
    while #neighbours > 0 do
        local locations_to_check = utils.deepcopy(neighbours)
        neighbours = {}
        for _, val in pairs(locations_to_check) do
            grid[val[2]][val[1]] = "#"
            local new_n = check_neighbours(grid, val, t, b, l, r)
            for _, n_val in pairs(new_n) do
                add_to_set(neighbours, n_val)
            end
        end
        print(#neighbours)
        utils.timestamp()
    end
    return grid
end

local function count_filled(grid)
    local total = 0
    for y, line in pairs(grid) do
        for x, cell in pairs(line) do
            if cell ~= "." then
                total = total + 1
            end
        end
    end
    return total
end

local instructions = {}
for index, value in ipairs(inputs) do
    local splits = utils.split(value, "%s")
    -- local inst = { dir = splits[1], dist = tonumber(splits[2]), col = splits[3]:sub(2, #splits[3] - 1) }
    local dist = tonumber(splits[3]:sub(3, 7), 16)
    local dir = tonumber(splits[3]:sub(#splits[3] - 1, #splits[3] - 1), 16)
    local inst = { dir = dir, dist = dist, col = "#" }
    table.insert(instructions, inst)
end

local grid = {}
-- make the first row
table.insert(grid, {})

local pos = { 1, 1 }
grid[pos[2]][pos[1]] = "#ffffff"
for i, inst in ipairs(instructions) do
    print(i, inst.dir, inst.dist)
    local s = os.clock()
    for i = 1, inst.dist, 1 do
        if inst.dir == 0 then
            pos = { pos[1] + 1, pos[2] }
        elseif inst.dir == 3 then
            pos = { pos[1], pos[2] - 1 }
        elseif inst.dir == 2 then
            pos = { pos[1] - 1, pos[2] }
        else -- has to be down
            pos = { pos[1], pos[2] + 1 }
        end

        -- check whether the row exists
        if not grid[pos[2]] then
            grid[pos[2]] = {}
        end
        -- set the space
        grid[pos[2]][pos[1]] = inst.col
    end
    utils.timestamp(s)
end

local t, b, l, r = utils.get_grid_size(grid)
utils.timestamp()
fill_grid(grid, t, b, l, r)
--utils.print_grid(grid, false)


-- OUTPUT THE RESULT
print("")
print.green(count_filled(grid))
utils.timestamp()
