local utils = require "utils"

local input_file = "11.txt"
local inputs = utils.lines_from(input_file)

local function timestamp()
    print(string.format("Elapsed time: %.3f seconds", os.clock()))
end

local function print_grid(grid)
    for y, line in ipairs(grid) do
        print(table.concat(line))
    end
    print(" ")
end

local function expand_blank_column(starmap)
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
            for y = 1, #starmap, 1 do
                table.insert(starmap[y], x_pos, starmap[y][x_pos])
            end
            x_pos = x_pos + 1 -- skip new one
        end
    end
    return starmap
end

local function expand_blank_row(starmap)
    local i = 0
    while i < #starmap do
        i = i + 1
        if not table.contains(starmap[i], "#") then
            table.insert(starmap, i, starmap[i])
            -- TODO: causes duplicate references
            -- skip the one we just added
            i = i + 1
        end
    end
    return starmap
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
    return math.abs(gal1.x - gal2.x) + math.abs(gal1.y - gal2.y)
end

-- DO THE CODE HERE

local starmap = {}

for _, value in ipairs(inputs) do
    table.insert(starmap, utils.split(value))
end

print_grid(starmap)

-- handle expansion
starmap = expand_blank_column(starmap)
starmap = expand_blank_row(starmap)

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
