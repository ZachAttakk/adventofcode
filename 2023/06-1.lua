local utils = require "utils"

local input_file = "06.txt"
local inputs = utils.lines_from(input_file)

local data = {}

-- DO THE CODE HERE

local function get_dist(race_time, hold_time)
    return (race_time - hold_time) * hold_time
end

local function get_hold_times(race_time, record)
    local start_hold = race_time // 2
    local hold_delta = 0
    local r_longest = start_hold
    local r_shortest = start_hold

    while true do
        hold_delta = hold_delta + 1

        local long_hold = start_hold + hold_delta
        local short_hold = start_hold - hold_delta
        local long_dist = get_dist(race_time, long_hold)
        local short_dist = get_dist(race_time, short_hold)

        if long_dist > record then
            r_longest = long_hold
        end
        if short_dist > record then
            r_shortest = short_hold
        end

        if long_dist < record and short_dist < record then
            return r_shortest, r_longest
        end
    end
end

-- parse time and distance into 2 arrays
local times = utils.split_to_nums(inputs[1]:sub(12), "%s")
local distances = utils.split_to_nums(inputs[2]:sub(12), "%s")


for i = 1, #times, 1 do
    -- start with the current record
    local t = times[i]
    local r = distances[i]
    local shortest, longest = get_hold_times(t, r)
    print(t, shortest, longest)
    table.insert(data, longest - shortest + 1)
end

-- OUTPUT THE RESULT
print("")
print(utils.multiply(data))
