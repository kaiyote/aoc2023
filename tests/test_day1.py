from aoc2023 import day1

data_file = open("data/day1.txt", "r")
real_data = data_file.readlines()
data_file.close()

# data_file = open("data/day1_ex.txt", "r")
# ex_data = data_file.readlines()
# data_file.close()

def test_part1():
  assert day1.part1(real_data) == 54331

def test_part2():
  assert day1.part2(real_data) == 54518
