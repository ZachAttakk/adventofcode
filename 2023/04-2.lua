local utils = require "utils"

local input_file = "04.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE
local data = {}
local multipliers = {}

for index, value in ipairs(inputs) do
    -- First break the list into winning numbers and scoring numbers
    local card_str = value:sub(value:find(":") + 1)
    local card = {}

    local separated_lines = utils.split(card_str, "|")
    card.winning_nums = utils.split(separated_lines[1], "%s")
    card.scoring_nums = utils.split(separated_lines[2], "%s")

    -- for each scoring number that exists in its winning numbers, count the wins
    local wins = 0
    for _, scoring_num in ipairs(card.scoring_nums) do
        if table.contains(card.winning_nums, scoring_num) then
            wins = wins + 1
        end
    end
    -- add to data
    table.insert(data, wins)
end

-- now count the number of wins and multiply them out
-- first make a list of multipliers as long as the data list
for i = 1, #data, 1 do
    table.insert(multipliers, 1)
end

-- then inscrease the multiplier based on wins

for card_index, card in pairs(data) do
    for i = card_index + 1, card_index + card, 1 do
        -- add to successive cards the multiplier
        multipliers[i] = multipliers[i] + multipliers[card_index]
    end
end

-- OUTPUT THE RESULT
print("  ")
print(utils.sum(multipliers))
