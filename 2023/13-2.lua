local utils = require "utils"

local input_file = "13.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function validate_reflection(str, i)
    local len = math.min(i, #str - i)
    local left = str:sub(i - len + 1, i)
    local right = string.reverse(str:sub(i + 1, i + len))
    if left == right then return true else return false end
end

local function find_reflection(pat)
    for column = 1, #pat[1], 1 do
        for i = 1, #pat[1] - 1, 1 do
            -- get count of reflections
            local reflection_count = 0
            for j = 1, #pat, 1 do
                if validate_reflection(pat[j], i) then
                    reflection_count = reflection_count + 1
                end
            end
            if reflection_count == #pat - 1 then
                -- found the one with only 1 error
                return i
            end
        end
    end
    return 0
end

local function pivot(grid)
    local rotated = {}
    for x = 1, #grid[1], 1 do
        local new_line = ""
        for y = 1, #grid, 1 do
            new_line = new_line .. grid[y]:sub(x, x)
        end
        table.insert(rotated, new_line)
    end
    return rotated
end



local data = {}

local pattern = {}
for index, value in ipairs(inputs) do
    if #value == 0 then
        table.insert(data, pattern)
        pattern = {}
    else
        table.insert(pattern, value)
    end
    if index == #inputs then
        -- catch the last one
        table.insert(data, pattern)
    end
end


local reflections = {}

for pat_index, pat in ipairs(data) do
    print(string.format("Checking grid %d...", pat_index))
    -- check for a reflection column
    local reflection_point = 0
    reflection_point = find_reflection(pat)

    if reflection_point ~= 0 then
        -- found a column so insert it
        print("Found column " .. reflection_point)
        table.insert(reflections, reflection_point)
    else
        -- if we didn't find a column, try for a row
        -- now we rotate the grid
        print("No column, checking rows...")
        local rotated_pattern = pivot(pat)
        reflection_point = find_reflection(rotated_pattern)
        print("Found row " .. reflection_point)
        table.insert(reflections, reflection_point * 100)
    end
end


-- OUTPUT THE RESULT
print("")
print.green(utils.sum(reflections))
utils.timestamp()
