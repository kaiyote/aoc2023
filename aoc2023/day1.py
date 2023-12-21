import re
import functools

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
    line = re.sub(r'(oneight|threeight|fiveight|sevenine|nineight|eightwo|eighthree|twone|one|two|three|four|five|six|seven|eight|nine)', __string_to_int, line)
    numbers = [x for x in line if x.isdigit()]
    total += int(numbers[0] + numbers[-1])

  return total

def __process_data(data: list[str]):
  return [ line.strip() for line in data ]

def __string_to_int(number_word: re.Match[str]):
  match number_word.group(0):
    case "one":
      return "1"
    case "two":
      return "2"
    case "three":
      return "3"
    case "four":
      return "4"
    case "five":
      return "5"
    case "six":
      return "6"
    case "seven":
      return "7"
    case "eight":
      return "8"
    case "nine":
      return "9"
    case "oneight":
      return "18"
    case "threeight":
      return "38"
    case "fiveight":
      return "58"
    case "sevenine":
      return "79"
    case "nineight":
      return "98"
    case "eightwo":
      return "82"
    case "eighthree":
      return "83"
    case "twone":
      return "21"
