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
    for _, step in ipairs(workflow) do
        if step.has_condition then
            if step.condition(part.x, part.m, part.a, part.s) then return step.dest end
        else
            return step.dest
        end
    end
    return "oops"
end

local workflows = {}
local parts = {}
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
                    --[[ step.var = st:sub(1, 1)
                    step.compare = st:sub(2, 2)
                    step.amount = tonumber(st:sub(3, st:find(":") - 1))]]
                    step.has_condition = true
                    step.dest = st:sub(st:find(":") + 1, #st)
                    step.condition = load_condition(st:sub(1, st:find(":") - 1))
                    table.insert(wf_steps, step)
                end
            end
            workflows[wf_name] = wf_steps
        end
    else
        -- read parts
        local part_st = value:sub(2, #value - 1)
        local part_vals_st = utils.split(part_st, ",")
        local part = {}
        part["text"] = value
        part["workflow"] = "in"
        for _, part_val in ipairs(part_vals_st) do
            local details = utils.split(part_val, "=")
            part[details[1]] = tonumber(details[2])
        end
        table.insert(parts, part)
    end
end

for _, part in ipairs(parts) do
    local sequence = {}
    while part.workflow ~= "R" and part.workflow ~= "A" do
        table.insert(sequence, part.workflow)
        part.workflow = process_part(workflows, part)
    end
    print(part.text, table.concat(sequence, "->"), part.workflow)
end

-- add up all the values
local totals = {}
for _, p in pairs(parts) do
    if p.workflow == "A" then
        table.insert(totals, p.x)
        table.insert(totals, p.m)
        table.insert(totals, p.a)
        table.insert(totals, p.s)
    end
end


-- OUTPUT THE RESULT
print("")
print.green(utils.sum(totals))
utils.timestamp()
