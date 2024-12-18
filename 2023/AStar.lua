-- https://github.com/Shakadak/lua-astar

local PQ = {}

PQ.new = function()
    local queue = {
        n      = 0,
        pop    = PQ.pop,
        insert = PQ.insert
    }
    return queue
end

PQ.insert = function(self, priority, elem)
    local n = self.n + 1
    self.n = n
    self[n] = { p = priority, v = elem }
    local i = n
    while i >= 2 do
        local j = math.floor(i / 2)
        if self[i].p < self[j].p then
            self[i], self[j] = self[j], self[i]
        end
        i = j
    end
end

PQ.pop = function(self)
    if self.n == 0 then return nil end
    local ret        = self[1]
    local n          = self.n
    self[1], self[n] = self[n], nil
    self.n           = n - 1
    local i          = 1
    while i < self.n do
        local left = 2 * i
        local right = 2 * i + 1
        local current = i
        if left <= self.n then
            if self[left].p < self[i].p then
                i = left
            end
        end
        if right <= self.n then
            if self[right].p < self[i].p then
                i = right
            end
        end
        if current == i then
            break
        else
            self[current], self[i] = self[i], self[current]
        end
    end
    return ret.v
end

local function fromMaybe(default)
    return function(maybeNil)
        if maybeNil == nil
        then
            return default
        else
            return maybeNil
        end
    end
end

local function maybe(default)
    return function(f)
        return function(x)
            if x == nil
            then
                return default
            else
                return f(x)
            end
        end
    end
end

local function inferior(x)
    return function(y)
        return x < y
    end
end

local function backtrack(last, cameFrom)
    local current = last
    local path = {}
    while current ~= nil do
        table.insert(path, 1, current)
        current = cameFrom[current]
    end
    return path
end

-- aStar:
--      - expand:   function that takes a node and return its neighbors as array/table
--                  neighbors must be values, not keys, as they are discarded
--      - cost:     function that take two nodes, `from` and `to`, and return the cost
--                  to go from `from` to `to`
--                  must be curried
--      - heuristic:function that takes a node and return the estimated cost to reach
--                  the goal
--      - goal:     function that takes a node and return whether the goal has been
--                  reached or not
--      - start:    the starting node
--
-- return nil in case of failure
--        the ordered path in case of success, as an array
local function aStar(expand)
    return function(cost)
        return function(heuristic)
            return function(goal)
                return function(start)
                    local open = PQ.new()
                    local closed = {}
                    local cameFrom = {}
                    local tCost = {}

                    open:insert(0, start)
                    cameFrom[start] = nil
                    tCost[start] = 0
                    for current in PQ.pop, open do
                        if goal(current) then
                            return backtrack(current, cameFrom)
                        else
                            closed[current] = true
                            local costFromCurrentTo = cost(current)
                            for _, neighbor in pairs(expand(current)) do
                                if not closed[neighbor] then
                                    local tmpCost = tCost[current] + costFromCurrentTo(neighbor)
                                    if maybe(true)(inferior(tmpCost))(tCost[neighbor]) then
                                        cameFrom[neighbor] = current
                                        tCost[neighbor] = tmpCost
                                        open:insert(tmpCost + heuristic(neighbor), neighbor)
                                    end
                                end
                            end
                        end
                    end
                    return nil
                end
            end
        end
    end
end

return aStar
