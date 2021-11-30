import itertools

a = [0,1,2,3,4]

combinations = list(itertools.permutations(a, 5))
print(combinations)
print()
print(combinations[0])
print()
print(combinations.pop())
print()
print(combinations.pop())
print()
print(combinations.pop())
print()
print(combinations.pop(0))

print(combinations.pop(0))

print(combinations.pop(0))
