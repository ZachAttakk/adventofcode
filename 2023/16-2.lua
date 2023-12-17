local utils = require "utils"
local part1 = require "16-1"

local input_file = "16.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE
DATA = {}
for y, value in ipairs(inputs) do
    local row = {}
    local symbols = utils.split(value)
    for x, symbol in ipairs(symbols) do
        table.insert(row, { x = x, y = y, symbol = symbol, energized = false })
    end
    table.insert(DATA, row)
end

-- move beams

local positions = {}
local st_beam = {}
local s = os.clock()
-- check from top
for x = 1, part1.stats.MAX_WIDTH, 1 do
    st_beam = { x = x, y = 0, dir = "D" }
    print(st_beam.x, st_beam.y)
    table.insert(positions, part1.move_beams(st_beam))
    print(positions[#positions])
    utils.timestamp(s)
    print()
    s = os.clock()
end
-- check from bottom
for x = 1, part1.stats.MAX_WIDTH, 1 do
    st_beam = { x = x, y = part1.stats.MAX_HEIGHT + 1, dir = "U" }
    print(st_beam.x, st_beam.y)
    table.insert(positions, part1.move_beams(st_beam))
    print(positions[#positions])
    utils.timestamp(s)

    s = os.clock()
end
-- check from left
for y = 1, part1.stats.MAX_HEIGHT, 1 do
    st_beam = { x = 0, y = y, dir = "R" }
    print(st_beam.x, st_beam.y)
    table.insert(positions, part1.move_beams(st_beam))
    print(positions[#positions])
    utils.timestamp(s)
    print()
    s = os.clock()
end
-- check right
for y = 1, part1.stats.MAX_HEIGHT, 1 do
    st_beam = { x = part1.stats.MAX_WIDTH, y = y, dir = "L" }
    print(st_beam.x, st_beam.y)
    table.insert(positions, part1.move_beams(st_beam))
    print(positions[#positions])
    utils.timestamp(s)
    print()
    s = os.clock()
end

table.sort_asc(positions)

-- OUTPUT THE RESULT
print("")
print.green(positions[1])
utils.timestamp()
