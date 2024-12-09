require "03"

Lines = {}

if arg[2] == "debug" then
    require("lldebugger").start()
end

function love.load()
    love.window.setTitle("Advent of Code 2024")
    Load_inputs()
    print("Part 1:")
    print("Solution: " .. Part1())
    print("")
    print("Part 2:")
    print("Solution: " .. Part2())
end

function Load_inputs()
    for line in love.filesystem.lines(Inputs_file) do
        table.insert(Lines, line)
    end
end

function split(input, sep)
    if sep == nil then
        sep = "%s"
    end
    local t = {}
    for str in string.gmatch(input, "([^" .. sep .. "]+)") do
        table.insert(t, str)
    end
    return t
end

function split_lines()
    local split_data = {}
    for _i, line in pairs(Lines) do
        local _splits = split(line)
        table.insert(split_data, _splits)
    end
    return split_data
end

local love_errorhandler = love.errorhandler

function love.errorhandler(msg)
    if lldebugger then
        error(msg, 2)
    else
        return love_errorhandler(msg)
    end
end

function sum_total(list)
    local total = 0
    for _, val in pairs(list) do
        total = total + val
    end
    return total
end
