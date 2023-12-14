print = require "chroma"

--#region table functions

-- add contains functions to table
function table.contains(table, element)
    for _, value in pairs(table) do
        if value == element then
            return true
        end
    end
    return false
end

-- sort in ascending order
function table.sort_asc(list)
    table.sort(list, function(a, b) return a > b end)
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

--#endregion

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
    local t = {}
    if sep == nil then
        for i = 1, #inputstr, 1 do
            table.insert(t, inputstr:sub(i, i))
        end
    else
        for str in string.gmatch(inputstr, "([^" .. sep .. "]+)") do
            table.insert(t, trim(str))
        end
    end
    return t
end
M.split = split

local function split_to_nums(inputstr, sep)
    -- split a string into values and then convert them all to numbers
    local strs = split(inputstr, sep)
    for i = 1, #strs, 1 do
        strs[i] = tonumber(strs[i])
    end

    return strs
end
M.split_to_nums = split_to_nums

local function sum(number_list)
    local total = 0
    for _, value in pairs(number_list) do
        total = total + value
    end
    return total
end
M.sum = sum

local function multiply(number_list)
    local total = number_list[1]

    for i = 2, #number_list, 1 do
        total = total * number_list[i]
    end
    return total
end
M.multiply = multiply

local function is_prime(x)
    -- Negative numbers, 0 and 1 are not prime.
    if x < 2 then
        return false
    end

    -- Primality for even numbers is easy.
    if x == 2 then
        return 2
    end
    if x % 2 == 0 then
        return false
    end

    -- Since we have already considered the even numbers,
    -- see if the odd numbers are factors.
    for i = 3, math.sqrt(x), 2 do
        if x % i == 0 then
            return false
        end
    end
    return x
end
M.is_prime = is_prime

local function deepcopy(o, seen)
    seen = seen or {}
    if o == nil then return nil end
    if seen[o] then return seen[o] end

    local no
    if type(o) == 'table' then
        no = {}
        seen[o] = no

        for k, v in next, o, nil do
            no[deepcopy(k, seen)] = deepcopy(v, seen)
        end
        setmetatable(no, deepcopy(getmetatable(o), seen))
    else -- number, string, boolean, etc
        no = o
    end
    return no
end
M.deepcopy = deepcopy

local function timestamp(start_time)
    if not start_time then
        print(string.format("Elapsed time: %.3f s", os.clock()))
    else
        local time_dif = os.clock() - start_time
        if time_dif > 10 then
            print.red(string.format("Elapsed time: %.3f/%.3fs", os.clock() - start_time, os.clock()))
        else
            print(string.format("Elapsed time: %.3f/%.3fs", os.clock() - start_time, os.clock()))
        end
    end
end
M.timestamp = timestamp

return M


--#endregion
