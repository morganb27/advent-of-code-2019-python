import fileinput
from itertools import permutations

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = None, None

def program_alarm(data):
    global PART_1, PART_2
    for line in data:
        program = list(map(int, line.split(",")))
        PART_1 = compute_program(program.copy())

        for verb, noun in permutations(range(100), 2):
             tape = program.copy()
             tape[1] = noun
             tape[2] = verb
             result = compute_program(tape)
             if result == 19690720:
                  PART_2 = 100 * noun + verb



def compute_program(program):
    for i in range(0, len(program), 4):
            opcode, x, y, target = program[i], program[i+1], program[i+2], program[i+3]
            if opcode == 1:
                program[target] = program[x] + program[y]
            elif opcode == 2:
                program[target] = program[x] * program[y]
            elif opcode == 99:
                break
    return program[0]

program_alarm(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is : {PART_2}")