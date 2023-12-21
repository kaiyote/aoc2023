import re

def part1(data: list[str]):
  clean_lines = __process_data(data)

  total = 0
  for line in clean_lines:
    numbers = [x for x in line if x.isdigit()]
    total += int(numbers[0] + numbers[-1])

  return total

def part2(data: list[str]):
  clean_lines = __process_data(data)

  total = 0
  for line in clean_lines:
    while re.sub(r'(one|two|three|four|five|six|seven|eight|nine)', __string_to_int, line) != line:
      line = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)', __string_to_int, line)

    numbers = [x for x in line if x.isdigit()]
    total += int(numbers[0] + numbers[-1])

  return total

def __process_data(data: list[str]):
  return [ line.strip() for line in data ]

def __string_to_int(number_word: re.Match[str]):
  match number_word.group(0):
    case "one":
      return "1e" # the trailing last letter is important so the next replace can work if you run into a "smushed double letter"
    case "two":
      return "2o"
    case "three":
      return "3e"
    case "four":
      return "4r"
    case "five":
      return "5e"
    case "six":
      return "6x"
    case "seven":
      return "7n"
    case "eight":
      return "8t"
    case "nine":
      return "9e"
