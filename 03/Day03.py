import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = None, float("inf")
COORD = defaultdict(int)
SEEN = set()
STEPS = defaultdict(int)

def crossed_wires(data):
    global COORD, SEEN, PART_1, PART_2
    for i, line in enumerate(data):
        wire = line.split(',')
        temp = set()
        X, Y, steps = 0, 0, 0
        for item in wire:
            direction, distance = parse_line(item)
            for _ in range(distance):
                steps += 1
                if direction == 'U':
                    Y += 1
                elif direction == 'R':
                    X += 1
                elif direction == 'D':
                    Y -= 1
                elif direction == 'L':
                    X -= 1
                
                if (X, Y) in temp:
                    continue

                if (X, Y) in COORD and (X, Y) not in temp:
                    SEEN.add((X, Y))
                    STEPS[(X, Y)] += steps + COORD[(X, Y)]
                COORD[(X, Y)] = steps
                temp.add((X, Y))

    PART_1 = min((manhattan_distance(x, y) for x, y in SEEN), default=None)
    PART_2 = min(STEPS.values())

            
    
def parse_line(line):
    direction, distance = line[0], line[1:]
    return direction, int(distance)


def manhattan_distance(x, y):
    return abs(x) + abs(y)

crossed_wires(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")