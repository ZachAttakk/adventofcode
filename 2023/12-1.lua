local utils = require "utils"

local input_file = "12.txt"
local inputs = utils.lines_from(input_file)

local function timestamp(start_time)
    if not start_time then
        print(string.format("Elapsed time: %.3f seconds", os.clock()))
    else
        print(string.format("Elapsed time: %.3f seconds", os.clock() - start_time))
    end
end

-- DO THE CODE HERE

local function get_variations(str)
    local vars = {}
    -- find first questionmark
    local first_var = str.find(str, "?")
    if first_var then
        -- found one
        local yes_str = str.gsub(str, "?", "#", 1)
        local no_str = str.gsub(str, "?", ".", 1)
        str.gsub(no_str, "?", ".", 1)
        -- check whether this was the last one
        if not str.find(yes_str, "?") then
            table.insert(vars, yes_str)
            table.insert(vars, no_str)
        else
            local roll_up = get_variations(yes_str)
            for _, value in pairs(roll_up) do
                table.insert(vars, value)
            end
            local roll_up = get_variations(no_str)
            for _, value in pairs(roll_up) do
                table.insert(vars, value)
            end
        end
    end
    return vars
end


local function validate_match(str, pat)
    local char_index = 1
    local cur_pat_index = 1
    local cur_pat = ""
    local last_pat_found_index = 0
    while char_index <= #str and cur_pat_index <= #pat do
        local char = str:sub(char_index, char_index)
        if char == "#" then
            cur_pat = cur_pat .. char
        elseif char == "." and #cur_pat > 0 then
            if #cur_pat == pat[cur_pat_index] then
                -- The pattern length matches
                cur_pat = ""
                cur_pat_index = cur_pat_index + 1
                last_pat_found_index = char_index
            else
                -- the pattern is too short or too long
                return false
            end
        end
        char_index = char_index + 1
    end
    if cur_pat_index > #pat then
        -- we've reached the last pattern
        local last_bit = str:sub(last_pat_found_index + 1, #str)
        if not string.find(last_bit, "#") then
            return true
        else
            return false
        end
    elseif cur_pat_index == #pat and #cur_pat == pat[#pat] then
        -- we've reached the end of the string without matching the last pattern
        return true
    else
        return false
    end
end

local function check_matches(vars, pattern)
    local matched = {}
    -- now we match them all
    for i, var in ipairs(vars) do
        if validate_match(var, pattern) then
            table.insert(matched, var)
        end
    end
    return matched
end


local data = {}
local patterns = {}
local matched_variations = {}

for _, value in ipairs(inputs) do
    local splits = utils.split(value, "%s")
    table.insert(data, splits[1])
    table.insert(patterns, utils.split_to_nums(splits[2], ","))
end

local last_match_completed_time = os.clock()
for i, row in pairs(data) do
    local vars = get_variations(row)
    -- TODO: do regex to check which match
    table.insert(matched_variations, check_matches(vars, patterns[i]))
    print("Row " .. i .. " Matches: " .. #matched_variations[i])
    timestamp(last_match_completed_time)
    last_match_completed_time = os.clock()
end

-- now we get the total
local total_matches = 0
for _, match in ipairs(matched_variations) do
    total_matches = total_matches + #match
end

-- OUTPUT THE RESULT
print("")
print(total_matches)
timestamp()
