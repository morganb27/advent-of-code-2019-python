START = 136760
END = 595730
PART_1, PART_2 = 0, 0

def valid_passwords():
    global PART_1, PART_2
    for num in range(START, END):
        if has_two_adjacent_digits(str(num)) and has_increasing_characters(str(num)):
            PART_1 += 1
        if has_valid_pair(str(num)) and has_increasing_characters(str(num)):
            PART_2 += 1


def has_two_adjacent_digits(num):
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            return True
    return False

def has_increasing_characters(num):
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            return False
    return True

def has_valid_pair(num):
    i = 1
    while i < len(num):
        pair = num[i-1]
        while i <= len(num) - 1 and num[i] == num[i-1]:
            pair += num[i]
            i += 1
        if len(pair) == 2:
            return True
        i += 1
    return False
    
valid_passwords()
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")