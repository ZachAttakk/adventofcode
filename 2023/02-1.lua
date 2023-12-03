local utils = require "utils"

local input_file = "02.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local red_limit = 12
local green_limit = 13
local blue_limit = 14

local function parse_turns(turns_list)
    -- 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    local turns = {}
    for _, turn in ipairs(turns_list) do
        -- split by comma
        local hands_list = utils.split(turn, ",")
        -- now we parse the hand
        -- 3 blue, 4 red
        local hand = { green = 0, blue = 0, red = 0 }
        for _, colour_str in ipairs(hands_list) do
            local colour_list = utils.split(colour_str, " ")
            if colour_list[2] == "green" then
                hand.green = tonumber(colour_list[1])
            elseif colour_list[2] == "red" then
                hand.red = tonumber(colour_list[1])
            else
                hand.blue = tonumber(colour_list[1])
            end
        end
        table.insert(turns, hand)
    end
    return turns
end

local function validate_game(game)
    for turn_index, turn in ipairs(game) do
        if turn.red > red_limit or turn.green > green_limit or turn.blue > blue_limit then
            return false
        end
    end
    return true
end

local data = {}

for game_id, value in ipairs(inputs) do
    -- start at the colon
    local game_turns_str = string.sub(value, string.find(value, ":") + 2)
    -- turns are split by semicolon
    local turns_list = utils.split(game_turns_str, ";")
    local game_data = parse_turns(turns_list)
    table.insert(data, game_data)
end

-- Now that we have the data, check whether any games are impossible.
local result_list = {}
for game_index, game in ipairs(data) do
    table.insert(result_list, validate_game(game))
end

local result_total = 0
for game_id, game_value in ipairs(result_list) do
    if game_value then
        result_total = result_total + game_id
    end
end

-- OUTPUT THE RESULT
print("")
print(result_total)
