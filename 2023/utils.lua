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

local function format_time(seconds)
    if seconds < 60 then
        return string.format("%.3fs", seconds)
    elseif seconds < 3600 then
        return string.format("%d:%.3fs", seconds // 60, seconds % 60)
    else
        return string.format("%d:%d:%.3f%s", seconds // 3600, seconds % 3600, seconds % 60)
    end
end
M.format_time = format_time


local function timestamp(start_time)
    local time_dif = os.clock()
    local output = string.format("Elapsed time: %s", format_time(time_dif))
    if start_time then
        time_dif = os.clock() - start_time
        output = string.format("Elapsed time: %s / %s", format_time(time_dif), format_time(os.clock()))
    end
    if time_dif > 10 then
        print.red(output)
    else
        print(output)
    end
end
M.timestamp = timestamp

local function progress_bar(value, total)
    local perc = value / total
    return string.format("%s%s", string.rep("#", math.floor(perc * 100)), string.rep("_", math.floor((1 - perc) * 100)))
end
M.progress_bar = progress_bar

local function get_grid_size(grid)
    local l = 1 -- left start
    local t = 1 -- top start
    local b = #grid
    local r = 1
    for i, v in pairs(grid) do
        if i > b then b = i end
        if i < t then t = i end
        for x, _ in pairs(v) do
            if x > r then r = x end
            if x < l then l = x end
        end
    end
    return t, b, l, r
end
M.get_grid_size = get_grid_size

local function print_grid(grid, with_symbols)
    if with_symbols == nil then with_symbols = true end
    -- get size
    local t, b, l, r = get_grid_size

    local output = ""
    for y = t, b, 1 do
        local line = ""
        if not grid[y] then
            line = string.rep(".", r - l)
        else
            line = ""
            for x = l, r, 1 do
                if not grid[y][x] or grid[y][x] == "." then
                    line = line .. "."
                else
                    if with_symbols then
                        line = line .. grid[y][x]
                    else
                        line = line .. "#"
                    end
                end
            end
        end
        output = output .. line .. "\n"
    end
    print(output)
    return t, b, l, r
end

M.print_grid = print_grid

return M


--#endregion
