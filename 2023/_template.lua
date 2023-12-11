local utils = require "utils"

local input_file = "01.txt"
local inputs = utils.lines_from(input_file)

local function timestamp()
    print(string.format("Elapsed time: %.3f seconds", os.clock()))
end

-- DO THE CODE HERE


for index, value in ipairs(inputs) do
    -- MAKE IT WORK
end

-- OUTPUT THE RESULT
print("")
print("OUTPUT GOES HERE")
timestamp()
