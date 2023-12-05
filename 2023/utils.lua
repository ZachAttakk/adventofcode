-- add contains functions to table
function table.contains(table, element)
    for _, value in pairs(table) do
        if value == element then
            return true
        end
    end
    return false
end

-- string functions
function string:startswith(start)
    return self:sub(1, #start) == start
end

function string:endswith(ending)
    return ending == "" or self:sub(- #ending) == ending
end

function string:trim()
    return (self:gsub("^%s*(.-)%s*$", "%1"))
end

function string:split(sep)
    if sep == nil then
        sep = "%s"
    end
    local t = {}
    for str in string.gmatch(self, "([^" .. sep .. "]+)") do
        table.insert(t, string.trim(str))
    end
    return t
end

--#region utils
-- utils module
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

local function trim(s)
    return (s:gsub("^%s*(.-)%s*$", "%1"))
end
M.trim = trim

local function split(inputstr, sep)
    if sep == nil then
        sep = "%s"
    end
    local t = {}
    for str in string.gmatch(inputstr, "([^" .. sep .. "]+)") do
        table.insert(t, trim(str))
    end
    return t
end
M.split = split

local function sum(number_list)
    local total = 0
    for _, value in pairs(number_list) do
        total = total + value
    end
    return total
end
M.sum = sum
return M

--#endregion
