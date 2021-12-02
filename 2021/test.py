with open("day02.txt") as text:
    lines = text.readlines()

commands = []
aim = 0
horizontal = 0
depth = 0

for i in lines:
    command = str(i)
    commands.append(command[:-3])

for i in range(len(commands)):
    if commands[i] == "down":
        depth += int(lines[i][-2:])
    if commands[i] == "up":
        depth -= int(lines[i][-2:])
    if commands[i] == "forward":
        horizontal += int(lines[i][-2:])

# it didnt include the last line, so manually:
horizontal += 2
result = horizontal * depth
print(result)
