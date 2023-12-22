import itertools

def part1(data: list[str]):
  part_map = __process_data(data)
  part_numbers = [int(key.split("_", 2)[0]) for key, pos in part_map.items() if key != "part" and __is_adjacent_to_part(pos, part_map["part"]) > 0]

  print(list(part_numbers))

  return sum(part_numbers)

def part2(data: list[str]):
  clean_lines = __process_data(data)

  pass

def __process_data(data: list[str]) -> dict[str, list]:
  final_result = { "part": [] }
  line_maps = [ __process_line(line.strip(), index) for index, line in enumerate(data) ]

  for map in line_maps:
    for key, pos in map.items():
      match key:
        case "part":
          final_result[key] += pos
        case _:
          number_index = len([k for k in list(final_result.keys()) if k.startswith(key)])
          final_result[key + "_" + str(number_index)] = pos

  return final_result

def __process_line(line: str, line_index: int) -> dict[str, list[tuple[int, int]]]:
  result: dict[str, list[tuple[int, int]]] = { "part": [] }
  num_string: str = ""
  num_pos: list[tuple[int, int]] = []

  for index, ch in enumerate(line):
    match ch:
      case ".":
        if num_string != "":
          result.setdefault(num_string, [])
          result[num_string] += num_pos
          num_pos = []
          num_string = ""
        continue
      case x if str.isdigit(x):
        num_string += x
        num_pos.append((index, line_index))
      case x:
        if num_string != "":
          result.setdefault(num_string, [])
          result[num_string] += num_pos
          num_pos = []
          num_string = ""
        result["part"].append((index, line_index))

  return result

def __is_adjacent_to_part(num_pos: list[tuple[int, int]], part_pos: list[tuple[int, int]]) -> int:
  adj_part_count = 0

  for (x, y) in part_pos:
    adj_pos = [(x + x1, y + y1) for (x1, y1) in list(set(itertools.combinations([1,0,-1,1,-1,0], 2)))]
    adj_num_pos = [x for x in num_pos if x in adj_pos]
    if len(adj_num_pos) > 0:
      adj_part_count += 1

  return adj_part_count
