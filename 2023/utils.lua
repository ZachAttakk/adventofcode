-- file reading module

local NAME = "utils"

local M = {}

-- see if the file exists
local function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end
M.file_exists = file_exists

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

M.lines_from = lines_from

return M
