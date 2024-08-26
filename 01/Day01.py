import fileinput
import math

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0

def rocket_equation(data, part_two = False):
    global PART_1, PART_2
    for line in data:
        required_fuel = calculate_required_fuel(int(line))
        sum = required_fuel
        print("initial", required_fuel)
        if not part_two:
            PART_1 += required_fuel
        while required_fuel > 0:
            required_fuel = calculate_required_fuel(int(required_fuel))
            print(required_fuel)
            sum += required_fuel
        PART_2 += sum


def calculate_required_fuel(module):
    return max(math.floor(module/3) - 2, 0)

rocket_equation(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")