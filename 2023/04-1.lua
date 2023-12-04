local utils = require "utils"

local input_file = "04.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE
local data = {}
local wins = {}

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

    -- if there's 1 win the score is one.
    -- in all other cases it is 2^wins-1
    card.win_count = wins
    if wins > 1 then
        card.score = 2 ^ (wins - 1)
    else
        card.score = wins
    end

    -- add to data
    table.insert(data, card.score)
end

-- OUTPUT THE RESULT
print("  ")
print(utils.sum(data))
