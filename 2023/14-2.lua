local utils = require "utils"

local input_file = "14.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE
-- north, west, south, east
DIRECTIONS = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } }

LOOPS = 1000000000

local function print_grid(grid)
    for y, line in ipairs(grid) do
        print.gray(table.concat(line))
    end
end

local data = {}
for index, value in ipairs(inputs) do
    table.insert(data, utils.split(value))
end


local t = 0

local last_100_weights = {}
for i = 1, LOOPS, 1 do
    for _, dir in pairs(DIRECTIONS) do
        if dir[1] ~= 0 then
            -- up/down
            for y = math.max(dir[1] * #data, 1), math.max(dir[1] * -1 * #data, 1), dir[1] * -1 do
                for x = 1, #data[1], 1 do
                    if data[y][x] == "O" then
                        -- we found a rock
                        -- scan until we find where it comes to rest
                        for new_pos = y + dir[1], math.max(dir[1] * #data + 1, 0), dir[1] do
                            if new_pos == 0 or new_pos == #data + 1 or data[new_pos][x] == "O" or data[new_pos][x] == "#" then
                                data[y][x] = "."
                                data[new_pos - dir[1]][x] = "O"
                                break
                            end
                        end
                    end
                end
            end
        else
            -- left/right
            for x = math.max(dir[2] * #data[2], 1), math.max(dir[2] * -1 * #data[2], 1), dir[2] * -1 do
                for y = 1, #data[1], 1 do
                    if data[y][x] == "O" then
                        -- we found a rock
                        -- scan until we find where it comes to rest
                        for new_pos = x + dir[2], math.max(dir[2] * #data + 1, 0), dir[2] do
                            if new_pos == 0 or new_pos == #data + 1 or data[y][new_pos] == "O" or data[y][new_pos] == "#" then
                                data[y][x] = "."
                                data[y][new_pos - dir[2]] = "O"
                                break
                            end
                        end
                    end
                end
            end
        end
        --print_grid(data)
        --print(" ")
    end
    if i == 1 then
        -- get loop time
        t = os.clock()
    end
    local perc_done = i // LOOPS
    print(string.format("Loop %d %s%s ETA %.0f hours", i, string.rep("#", perc_done * 10),
        string.rep("_", 10 - perc_done * 10),
        (LOOPS - i) * t / 3600))
    utils.timestamp()

    local total_weight = 0

    -- now we calculate the weight
    for y = 1, #data, 1 do
        for x = 1, #data[1], 1 do
            if data[y][x] == "O" then
                total_weight = total_weight + #data - y + 1
            end
        end
    end

    -- record last 100 weights
    if #last_100_weights >= 100 then
        table.remove(last_100_weights, 1)
    end
    table.insert(last_100_weights, total_weight)

    if utils.sum(last_100_weights) // 100 == total_weight then
        --we've leveled out
        break
    end
end

-- OUTPUT THE RESULT
print("")
print.green(last_100_weights[#last_100_weights])
utils.timestamp()
