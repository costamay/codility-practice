#!/usr/bin/python3
def main(plan):
    wall = []
    floors = []
    for x, row in enumerate(plan):
        for y, char in enumerate(row):
            if char == '#':
                wall.append((x, y))
            elif char in ('*', '.'):
                floors.append((x, y))
    # Create separate sections based on walls
    floor_sections = []
    current_section = set(floors)
    while current_section:
        section = set()
        stack = [current_section.pop()]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in current_section:
                    current_section.remove((nx, ny))
                    stack.append((nx, ny))
            section.add((x, y))
        floor_sections.append(section)
    dirty_floor = []
    for section in floor_sections:
        dirty_section = {coord for coord in section if plan[coord[0]][coord[1]] == '*'}
        if dirty_section:
            dirty_floor.append(dirty_section)
    return len(dirty_floor)
plan = [ "**###**", "*#*#*#*", "##*#*##", "*#***#*", ".#####.", "..*#*.." ]
dirty_floor = main(plan)
print(dirty_floor)