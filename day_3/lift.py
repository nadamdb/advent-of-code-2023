def is_symbol(lines, i, j):
    return not lines[i][j].isdigit() and lines[i][j] != "."


def sum_parts(lines: list) -> int:
    parts_sum = 0
    for i in range(len(lines)):
        new_num = True
        to_add = False
        num = ""
        line = lines[i]
        for j in range(len(line)):
            c = line[j]
            if c.isdigit():
                num = num + c
                new_num = False
                if j > 0:
                    to_add = True if is_symbol(lines, i, j-1) else to_add
                    if i > 0:
                        to_add = True if is_symbol(lines, i-1, j-1) else to_add
                        to_add = True if is_symbol(lines, i-1, j) else to_add
                    if  i < len(lines)-1:
                        to_add = True if is_symbol(lines, i+1, j-1) else to_add
                        to_add = True if is_symbol(lines, i+1, j) else to_add

                if j < len(line)-1:
                    to_add = True if is_symbol(lines, i, j+1) else to_add
                    if i > 0:
                        to_add = True if is_symbol(lines, i-1, j+1) else to_add
                        to_add = True if is_symbol(lines, i-1, j) else to_add
                    if  i < len(lines)-1:
                        to_add = True if is_symbol(lines, i+1, j+1) else to_add
                        to_add = True if is_symbol(lines, i+1, j) else to_add
                if j == len(line)-1:
                    if to_add:
                        parts_sum += int(num)
                    num = ""
                    to_add = False
                    new_num = True
            elif not new_num:
                if to_add:
                    parts_sum += int(num)
                num = ""
                to_add = False
                new_num = True
    return parts_sum


with open("input.txt", 'r') as file:
    lines = [line.rstrip() for line in file]
    print(sum_parts(lines))
