local utils = require "utils"

local input_file = "16.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local NAME = "16-1"

local stats = {}
stats.MAX_WIDTH = 0
stats.MAX_HEIGHT = 0
stats.BOUNCES = {}

local function reset_energy()
    for y = 1, stats.MAX_HEIGHT, 1 do
        for x = 1, stats.MAX_WIDTH, 1 do
            DATA[y][x].energized = false
        end
    end
end
local function check_bounce(bounce)
    for _, b in pairs(stats.BOUNCES) do
        if b.x == bounce.x and b.y == bounce.y and b.dir == bounce.dir then return true end
    end
    return false
end


local function delete_beam(beam)
    for i, beam_in_list in ipairs(stats.BEAMS) do
        if beam_in_list == beam then
            table.remove(stats.BEAMS, i)
            break
        end
    end
end

local function update_cell(beam)
    local bounce = { x = beam.x, y = beam.y, dir = beam.dir }
    local bounced = false
    if beam.x > stats.MAX_WIDTH or beam.y > stats.MAX_HEIGHT or beam.x < 1 or beam.y < 1 then
        delete_beam(beam)
        return
    end

    local symbol = DATA[beam.y][beam.x].symbol
    -- if it's a "." we do nothing
    -- we've already been here
    if check_bounce(bounce) then
        delete_beam(beam)
    end

    DATA[beam.y][beam.x].energized = true
    -- R,L,U,D
    if symbol == "\\" then
        bounced = true
        if beam.dir == "R" then
            beam.dir = "D"
        elseif beam.dir == "L" then
            beam.dir = "U"
        elseif beam.dir == "U" then
            beam.dir = "L"
        else -- going down
            beam.dir = "R"
        end
    elseif symbol == "/" then
        bounced = true
        if beam.dir == "R" then
            beam.dir = "U"
        elseif beam.dir == "L" then
            beam.dir = "D"
        elseif beam.dir == "U" then
            beam.dir = "R"
        else -- going down
            beam.dir = "L"
        end
    elseif symbol == "-" and (beam.dir == "U" or beam.dir == "D") then
        -- split horizontal
        bounced = true
        beam.dir = "L"
        table.insert(stats.BEAMS, { x = beam.x, y = beam.y, dir = "R" })
    elseif symbol == "|" and (beam.dir == "R" or beam.dir == "L") then
        -- split horizontal
        bounced = true
        beam.dir = "U"
        table.insert(stats.BEAMS, { x = beam.x, y = beam.y, dir = "D" })
    end
    -- record bounce
    if bounced then
        table.insert(stats.BOUNCES, bounce)
    end
end

local function move_beams(starting_beam)
    table.insert(stats.BEAMS, starting_beam)
    stats.BOUNCES = {}
    reset_energy()
    local beam_limit_check = 0
    while #stats.BEAMS > 0 do
        beam_limit_check = beam_limit_check + 1
        for _, beam in ipairs(stats.BEAMS) do
            -- move the beam
            if beam.dir == "R" then
                beam.x = beam.x + 1
            elseif beam.dir == "L" then
                beam.x = beam.x - 1
            elseif beam.dir == "U" then
                beam.y = beam.y - 1
            else -- beam is going down
                beam.y = beam.y + 1
            end
            update_cell(beam)
        end
        --[[ print(#stats.BEAMS, beam_limit_check)
        utils.timestamp() ]]
    end

    -- now we count the energized cells
    local energized_cell_count = 0
    for y = 1, stats.MAX_HEIGHT, 1 do
        for x = 1, stats.MAX_WIDTH, 1 do
            if DATA[y][x].energized then
                energized_cell_count = energized_cell_count + 1
            end
        end
    end
    return energized_cell_count
end



-- beam direction:
-- R,L,U,D
stats.BEAMS = { { x = 0, y = 1, dir = "R" } }


DATA = {}
for y, value in ipairs(inputs) do
    local row = {}
    local symbols = utils.split(value)
    for x, symbol in ipairs(symbols) do
        table.insert(row, { x = x, y = y, symbol = symbol, energized = false })
    end
    table.insert(DATA, row)
end
-- set size globals
stats.MAX_WIDTH = #DATA[1]
stats.MAX_HEIGHT = #DATA

-- move beams
local output = move_beams()

-- OUTPUT THE RESULT
print("")
print.green(output)
utils.timestamp()

local M = {}
M.stats = stats
M.check_bounce = check_bounce
M.delete_beam = delete_beam
M.update_cell = update_cell
M.move_beams = move_beams
M.reset_energy = reset_energy

return M
