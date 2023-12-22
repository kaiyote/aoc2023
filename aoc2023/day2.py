def part1(data: list[str]) -> int:
  allowable = { "red": 12, "green": 13, "blue": 14 }
  games = __process_data(data)

  total = 0
  for (index, game) in enumerate(games):
    if game["red"] <= allowable["red"] and game["green"] <= allowable["green"] and game["blue"] <= allowable["blue"]:
      total += index + 1

  return total

def part2(data: list[str]) -> int:
  games = __process_data(data)

  total = 0
  for game in games:
    total += game["red"] * game["green"] * game["blue"]

  return total

def __process_data(data: list[str]) -> list[dict[str, int]]:
  return [ __line_to_map(line.strip()) for line in data ]

def __line_to_map(line: str) -> dict[str, int]:
  [_, rounds] = line.strip().split(":", 2)
  rounds = rounds.strip().split(";")

  results = { "red": 0, "blue": 0, "green": 0 }

  for round in rounds:
    groups = [g.strip().split(" ", 2) for g in round.strip().split(",")]
    for [num, color] in groups:
      results[color] = max(results[color], int(num))

  return results
