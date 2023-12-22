def part1(data: list[str]) -> int:
  games = __process_data(data)
  win_count = [ len([ n for n in mine if n in winner ]) for [winner, mine] in games ]

  return sum([ pow(2, w - 1) for w in win_count if w > 0 ])

def part2(data: list[str]) -> int:
  games = __process_data(data)
  game_counts = [1] * len(games)

  for index, [winner, mine] in enumerate(games):
    win_count = len([ n for n in mine if n in winner ])
    for i in range(win_count):
      game_counts[index + i + 1] += game_counts[index]

  return sum(game_counts)

def __process_data(data: list[str]) -> list[list[list[str]]]:
  cards = [ line.strip().split(": ", 2)[1].split(" | ", 2) for line in data ]
  return [ [winner.split(), mine.split()] for [winner, mine] in cards ]
