local utils = require "utils"

local input_file = "07.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

CARD_LIST = { "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" }
CARD_STRENGTH = "J23456789TJQKA"
HAND_TYPES = {
    { 1, 1, 1, 1, 1 },
    { 2, 1, 1, 1 },
    { 2, 2, 1 },
    { 3, 1, 1 },
    { 3, 2 },
    { 4, 1 },
    { 5 }
}

local function sort_hands(a, b)
    if a.strength ~= b.strength then
        return a.strength < b.strength
    else
        for i = 1, 5, 1 do
            local a_c = string.find(CARD_STRENGTH, a.cards:sub(i, i))
            local b_c = string.find(CARD_STRENGTH, b.cards:sub(i, i))
            if a_c ~= b_c then
                return a_c < b_c
            end
        end
    end
end

local function get_counts(cards)
    local counts_list = {}
    for _, v in pairs(CARD_LIST) do
        local _, count = cards:gsub(v, "")
        if count > 0 then
            counts_list[v] = count
        end
    end

    -- add joker card to highest count
    local jokers = counts_list["J"] or 0
    counts_list["J"] = nil

    --convert to string
    local counts = {}
    for _, v in pairs(counts_list) do
        table.insert(counts, v)
    end

    table.sort_asc(counts)

    if jokers > 0 and #counts > 0 then
        counts[1] = counts[1] + jokers
    elseif #counts == 0 then
        -- in the edge case where all 5 cards are jokers
        table.insert(counts, jokers)
    end
    return counts
end

local function get_strength(counts)
    for strength, value in pairs(HAND_TYPES) do
        if table.concat(counts) == table.concat(value) then
            return strength
        end
    end
end

local hands = {}

for _, value in ipairs(inputs) do
    local input_split = value:split("%s")
    local hand = { cards = input_split[1], bid = tonumber(input_split[2]) }
    hand.counts = get_counts(hand.cards)
    hand.strength = get_strength(hand.counts)
    table.insert(hands, hand)
end

table.sort(hands, sort_hands)

local winnings = {}

for rank, hand in pairs(hands) do
    table.insert(winnings, hand.bid * rank)
end

-- OUTPUT THE RESULT
print("  ")
print(utils.sum(winnings))
