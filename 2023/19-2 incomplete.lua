local utils = require "utils"

local input_file = "19.txt"
local inputs = utils.lines_from(input_file)

-- DO THE CODE HERE

local function load_condition(text)
    local func, err = load(string.format("return function(x,m,a,s) return %s end", text))
    if func then
        local ok, condition = pcall(func)
        return condition
    else
        print("Compilation error:", err)
        return
    end
end

local function process_part(workflows, part)
    local workflow = workflows[part.workflow]
    local parts_to_process = { part }
    local parts_to_output = {}
    for _, step in ipairs(workflow) do
        local processed_parts = {}
        if step.has_condition then
            -- need to check condition and pass a new part that has the bits that didn't make it
            for _, part in ipairs(parts_to_process) do
                local new_part = utils.deepcopy(part)
                if step.compare == ">" and part[step.var][2] > step.amount then
                    part[step.var][1] = step.amount + 1
                    part.workflow = step.dest
                    table.insert(parts_to_output, utils.deepcopy(part))

                    new_part[step.var][2] = step.amount
                    table.insert(processed_parts, new_part)
                elseif part[step.var][1] < step.amount then
                    part[step.var][2] = step.amount - 1
                    part.workflow = step.dest
                    table.insert(parts_to_output, utils.deepcopy(part))

                    new_part[step.var][1] = step.amount
                    table.insert(processed_parts, new_part)
                else
                    table.insert(processed_parts, part)
                end
            end
            parts_to_process = processed_parts
        else
            part.workflow = step.dest
            table.insert(parts_to_output, part)
        end
    end
    return parts_to_output
end

local workflows = {}
local reading_workflows = true
for index, value in ipairs(inputs) do
    if reading_workflows then
        if #value == 0 then
            -- done with the workflows
            reading_workflows = false
        else
            -- read workflow
            local wf_name = value:sub(1, value:find("{") - 1)
            local wf_flow = value:sub(value:find("{") + 1, value:find("}") - 1)
            local wf_steps_st = utils.split(wf_flow, ",")
            local wf_steps = {}
            for _, st in pairs(wf_steps_st) do
                local step = {}
                if not st:find(":") then -- only a destination
                    step.has_condition = false
                    step.dest = st
                    table.insert(wf_steps, step)
                else
                    step.var = st:sub(1, 1)
                    step.compare = st:sub(2, 2)
                    step.amount = tonumber(st:sub(3, st:find(":") - 1))
                    step.has_condition = true
                    step.dest = st:sub(st:find(":") + 1, #st)
                    step.condition = load_condition(st:sub(1, st:find(":") - 1))
                    table.insert(wf_steps, step)
                end
            end
            workflows[wf_name] = wf_steps
        end
    else
        break
    end
end

local completed = {}
-- we need to make ranges instead of values
local ranges = {
    { x = { 1, 4000 }, m = { 1, 4000 }, a = { 1, 4000 }, s = { 1, 4000 }, workflow = "in" }
}
-- keep going until they're all processed
while # ranges > 0 do
    local processed_ranges = {}
    for _, part in ipairs(ranges) do
        local new_parts = process_part(workflows, part)
        for _, n_part in ipairs(new_parts) do
            if n_part.workflow == "A" or n_part.workflow == "R" then
                table.insert(completed, n_part)
            else
                table.insert(processed_ranges, n_part)
            end
        end
    end
    ranges = processed_ranges
end

-- add up all the values
local totals = {}
for _, p in pairs(completed) do
    if p.workflow == "A" then
        table.insert(totals, (p.x[2] - p.x[1]) * (p.m[2] - p.m[1]) * (p.a[2] - p.a[1]) * (p.s[2] - p.s[1]))
    end
end


-- OUTPUT THE RESULT
print("")
print.green(utils.sum(totals))
utils.timestamp()
