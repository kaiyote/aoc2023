from aoc2023 import day2

data_file = open("data/day2.txt", "r")
real_data = data_file.readlines()
data_file.close()

# data_file = open("data/example.txt", "r")
# ex_data = data_file.readlines()
# data_file.close()

def test_part1():
  assert day2.part1(real_data) == 2239

def test_part2():
  assert day2.part2(real_data) == 83435
