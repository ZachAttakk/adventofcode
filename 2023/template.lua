local input_file = "01.txt"

-- see if the file exists
local function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end

-- get all lines from a file, returns an empty
-- list/table if the file does not exist
local function lines_from(file)
    if not file_exists(file) then return {} end
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local inputs = lines_from(input_file)

-- DO THE CODE HERE

for index, value in ipairs(inputs) do
    -- space intentionally left blank
end

-- OUTPUT THE RESULT
print("")
print("OUTPUT")
