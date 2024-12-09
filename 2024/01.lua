Inputs_file = "01.txt"

left_data = {}
right_data = {}

function Part1()
    print("Part 1:")

    split_left_right_lists()

    table.sort(left_data)
    table.sort(right_data)

    local total = 0
    for _i = 1, #left_data do
        total = total + math.abs(left_data[_i] - right_data[_i])
    end

    return total
end

function Part2()
    print("Part 2: ")

    local total = 0

    -- go through each number on left
    for _i, l_val in pairs(left_data) do
        --count occurrences on right
        local count = 0
        for _j, r_val in pairs(right_data) do
            if r_val == l_val then
                count = count + 1
            elseif r_val > l_val then
                break
            end
        end
        if count ~= 0 then
            print(l_val .. ": " .. count)
        end
        total = total + l_val * count
    end
    return total
end

function split_left_right_lists()
    for _i, line in pairs(Lines) do
        local _splits = split(line)
        table.insert(left_data, _splits[1])
        table.insert(right_data, _splits[2])
    end
end
