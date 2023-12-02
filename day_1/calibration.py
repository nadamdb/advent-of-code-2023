DIGIT_MAP = {
    "one":      "o1e",
    "two":      "t2o",
	"three":    "t3e",
	"four":     "4",
	"five":     "5e",
	"six":      "6",
	"seven":    "7n",
	"eight":    "e8t",
	"nine":     "n9e"
}


def get_number(line: str) -> int:
    nums = [c for c in line if c.isdigit()]
    return int(nums[0] + nums[-1])

def string_to_number(line: str) -> str:
    for key in DIGIT_MAP.keys():
        line = line.replace(key, DIGIT_MAP[key])
    return line

# def string_to_number(line: str) -> str:
#     i = 0
#     while i < len(line):
#         for key in DIGIT_MAP.keys():
#             if line[i:].startswith(key):
#                 line = line.replace(key, DIGIT_MAP[key], 1)
#                 break
#         i += 1
#     return line


sum = 0
sum2 = 0
with open("input.txt", "r") as file:
    for line in file:
        sum += get_number(line)
        sum2 += get_number(string_to_number(line))

print(sum)
print(sum2)