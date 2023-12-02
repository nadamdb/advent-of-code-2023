import math

LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_game(line: str) -> dict:
    game = {}
    two_parts = line.strip().split(":")
    game["id"] = int(two_parts[0].split(" ")[1])
    pulls = []
    for pull in two_parts[1].split(";"):
        cubes_in_pull = {"red": 0, "green": 0, "blue": 0}
        for cube in pull.split(","):
            n_c = cube.strip().split(" ")
            cubes_in_pull[n_c[1]] = int(n_c[0])
        pulls.append(cubes_in_pull)
    game["pulls"] = pulls
    return game
            

def id_if_possible(game: dict) -> int:
    for pull in game["pulls"]:
        for cube, cnt in pull.items():
            if cnt > LIMITS[cube]:
                return 0
    return game["id"]

def get_min_power(game: dict) -> int:
    maxs = {"red": 0, "green": 0, "blue": 0}
    for pull in game["pulls"]:
        for cube, cnt in pull.items():
            if cnt > maxs[cube]:
                maxs[cube] = cnt
    return math.prod(maxs.values())
    

possibles = 0
prods = 0
with open("input.txt", 'r') as file:
    for line in file:
        possibles += id_if_possible(parse_game(line))
        prods += get_min_power(parse_game(line))

print(possibles)
print(prods)