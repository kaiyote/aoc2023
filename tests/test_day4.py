from aoc2023 import day4

data_file = open("data/day4.txt", "r")
real_data = data_file.readlines()
data_file.close()

# data_file = open("data/example.txt", "r")
# ex_data = data_file.readlines()
# data_file.close()

def test_part1():
  # assert day4.part1(ex_data) == 13
  assert day4.part1(real_data) == 32001

def test_part2():
  # assert day4.part2(ex_data) == 30
  assert day4.part2(real_data) == 5037841
