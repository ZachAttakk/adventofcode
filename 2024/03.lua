Inputs_file = "03.txt"

pattern = "mul%(%d+,%d+%)"

function Part1()
    -- for each pattern find the calsulations
    local mults = {}
    for _, line in pairs(Lines) do
        for w in line:gmatch(pattern) do
            table.insert(mults, w)
        end
    end

    -- calculate them
    local calcs = {}
    for _, calculation in pairs(mults) do
        local factors = get_factors(calculation)
        local ans = multiply(factors)
        print(calculation .. ": " .. ans)
        table.insert(calcs, ans)
    end

    -- sum them
    return sum_total(calcs)
end

function Part2()
    --return total
end

function multiply(factors)
    return tonumber(factors[1]) * tonumber(factors[2])
end

function get_factors(calc)
    local factors = {}
    for w in calc:gmatch("%d+") do
        table.insert(factors, w)
    end
    return factors
end
