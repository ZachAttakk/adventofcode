local utils = require "utils"

local input_file = "11.txt"
local inputs = utils.lines_from(input_file)

TIMESCALE = 1000000

local function timestamp()
    print(string.format("Elapsed time: %.3f seconds", os.clock()))
end

local function print_grid(grid)
    print(string.format("Grid current size: %d x %d", #grid[1], #grid))
    --[[ for y, line in ipairs(grid) do
        print(table.concat(line))
    end
    print(" ") ]]
end

local function expand_blank_column(starmap)
    local exp_columns = {}
    local x_pos = 0
    while x_pos < #starmap[1] do
        local blank = true
        x_pos = x_pos + 1
        for y = 1, #starmap, 1 do
            if (starmap[y][x_pos]) == "#" then
                blank = false
                break
            end
        end
        -- still here? it was blank
        if blank then
            table.insert(exp_columns, x_pos)
        end
    end
    return exp_columns
end

local function expand_blank_row(starmap)
    local exp_rows = {}
    local i = 0
    while i < #starmap do
        i = i + 1
        if not table.contains(starmap[i], "#") then
            table.insert(exp_rows, i)
        end
    end
    return exp_rows
end

local function find_galaxies(starmap)
    local galaxies = {}
    for y = 1, #starmap, 1 do
        if table.contains(starmap[y], "#") then
            for x = 1, #starmap[y], 1 do
                if starmap[y][x] == "#" then
                    table.insert(galaxies, { x = x, y = y })
                end
            end
        end
    end
    return galaxies
end

local function manh(gal1, gal2)
    if gal1 == gal2 then return 0 end
    local prelim = math.abs(gal1.x - gal2.x) + math.abs(gal1.y - gal2.y)
    -- check for x expansion
    for _, x in ipairs(EXP_X) do
        if (x > gal1.x and x < gal2.x) or (x > gal2.x and x < gal1.x) then
            prelim = prelim + TIMESCALE - 1
        end
    end
    -- check for y expansion
    for _, y in ipairs(EXP_Y) do
        if (y > gal1.y and y < gal2.y) or (y > gal2.y and y < gal1.y) then
            prelim = prelim + TIMESCALE - 1
        end
    end
    return prelim
end

-- DO THE CODE HERE

local starmap = {}

for _, value in ipairs(inputs) do
    table.insert(starmap, utils.split(value))
end

print_grid(starmap)

-- handle expansion
-- make these global, less passing around
EXP_X = expand_blank_column(starmap)
EXP_Y = expand_blank_row(starmap)

print_grid(starmap)

local galaxy_list = find_galaxies(starmap)

local distances = {}
-- Now we calculate all possible distances
for a = 1, #galaxy_list, 1 do
    for b = a + 1, #galaxy_list, 1 do
        table.insert(distances, manh(galaxy_list[a], galaxy_list[b]))
    end
end


-- OUTPUT THE RESULT
print(" ")
print(utils.sum(distances))
timestamp()
