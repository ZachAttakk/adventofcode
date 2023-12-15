local utils = require "utils"

local input_file = "15.txt"
local inputs = utils.lines_from(input_file)


local function add_char(char, last_val)
    if last_val == nil then last_val = 0 end
    --Determine the ASCII code for the current character of the string.
    local ascii = string.byte(char)
    --Increase the current value by the ASCII code you just determined.
    last_val = last_val + ascii
    --Set the current value to itself multiplied by 17.
    last_val = last_val * 17
    --Set the current value to the remainder of dividing itself by 256.
    last_val = last_val % 256

    return last_val
end

local function get_hash(str)
    local chars = utils.split(str)
    local total = 0
    for _, char in ipairs(chars) do
        total = add_char(char, total)
    end
    return total
end

local function calc_focus_power(box_num, lens_index, focal_length)
    return (1 + box_num) * lens_index * focal_length
end

-- DO THE CODE HERE

local data = utils.split(inputs[1], ",")

-- init boxes
local boxes = {}
for i = 0, 255, 1 do
    boxes[i] = {}
end

-- do lenses
for _, value in ipairs(data) do
    if value:find("-") then
        -- calculate label
        local label = value:sub(1, #value - 1)
        -- get box number
        local box_num = get_hash(label)
        -- find the lens in the box
        local lens_pos = 0
        for lens_index, lens_data in ipairs(boxes[box_num]) do
            if label == lens_data[1] then
                lens_pos = lens_index
            end
        end
        if lens_pos ~= 0 then
            table.remove(boxes[box_num], lens_pos)
        end
    else
        -- calculate label
        local label = value:sub(1, value:find("=") - 1)
        -- get box number
        local box_num = get_hash(label)
        -- get the focal length
        local focal_length = value:sub(value:find("=") + 1, #value)
        -- find the lens in the box
        local lens_pos = 0
        for lens_index, lens_data in ipairs(boxes[box_num]) do
            if label == lens_data[1] then
                lens_pos = lens_index
            end
        end
        if lens_pos == 0 then
            -- add lens
            table.insert(boxes[box_num], { label, focal_length })
        else
            -- update focal length
            boxes[box_num][lens_pos][2] = focal_length
        end
    end
end

-- calculate lens_powers
local lens_powers = {}
for box_num = 0, 255, 1 do
    for lens_pos, lens in ipairs(boxes[box_num]) do
        local lens_power = calc_focus_power(box_num, lens_pos, lens[2])
        print(string.format("%s: %d", lens[1], lens_power))
        table.insert(lens_powers, calc_focus_power(box_num, lens_pos, lens[2]))
    end
end


-- OUTPUT THE RESULT
print("")
print.green(utils.sum(lens_powers))
utils.timestamp()
