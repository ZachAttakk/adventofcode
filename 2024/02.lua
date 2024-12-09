Inputs_file = "02.txt"

function Part1()
    Data = split_lines(Lines)

    local total = 0
    for _i, report in pairs(Data) do
        local result = validate(report)
        if result then
            total = total + 1
        end
    end
    return total
end

function Part2()
    local total = 0
    for _i, report in pairs(Data) do
        local result = validate(report)
        if result then
            total = total + 1
        else
            local fixed_result = error_check(report)
            if fixed_result then
                total = total + 1
            end
        end
    end
    return total
end

function validate(report)
    -- Validate according to rules
    -- Return index of error
    -- if valid, return 0


    -- which way are we going
    local increasing = false
    if tonumber(report[1]) < tonumber(report[2]) then
        increasing = true
    end


    for _i = 1, #report - 1 do
        -- check direction
        local a = tonumber(report[_i])
        local b = tonumber(report[_i + 1])
        if increasing and a >= b then
            return false
        elseif not increasing and a <= b then
            return false
        end

        -- check tolerance
        if math.abs(a - b) > 3 then
            return false
        end
    end

    return 0
end

function error_check(report)
    -- removes digits one by one until it passes

    for _i = 1, #report do
        local _instance = copy(report)
        table.remove(_instance, _i)
        if validate(_instance) then return true end
    end
    return false
end

function copy(t)
    -- renders a copy of an array without affecting original
    local t2 = {}
    for k, v in pairs(t) do
        t2[k] = v
    end
    return t2
end
