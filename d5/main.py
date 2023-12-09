# solution here is brute force.
# I solved in a mischievous manner :)

import sys

class Map:
  def __init__(self, nameline):
    self.name = nameline.split()[0]
    self.source = self.name.split('-')[0]
    self.dest = self.name.split('-')[2]
    self.ranges_min = []
    self.ranges_max = []
    self.ranges_dest = []
    self.lines = []
    self.min = sys.maxsize

  def add_line(self, line):
    self.lines.append(line)

  def ok(self):
    for line in self.lines:
      line.strip()
      dest = int(line.split()[0])
      source = int(line.split()[1])
      count = int(line.split()[2])
      self.ranges_min.append(source)
      self.ranges_max.append(source + count - 1)
      self.ranges_dest.append(dest)
    self.lines.clear()

  def get_range_index(self, num):
    index = -1
    for i in range(len(self.ranges_dest)):
      if num >= self.ranges_min[i] and num <= self.ranges_max[i]:
        index = i
        break
    return index


def get_seeds(line):
  arr = []
  line.strip()
  for i in line.split()[1:]:
    arr.append(int(i))
  return arr

def get_maps(lines):
  maps = []
  curr_map: Map = None
  for line in lines:
    if line == "\n":
      curr_map.ok()
      maps.append(curr_map)
      curr_map = None
      continue
    if curr_map is None:
      curr_map = Map(line)
    else:
      curr_map.add_line(line)
  if curr_map is not None:
    curr_map.ok()
    maps.append(curr_map)
    curr_map = None
  return maps

def find_map(maps, src) -> Map:
  for map in maps:
    if map.source == src:
      return map
  return None

def get_num_location(num):
  m = Map("x-x-x")
  src = 'seed'
  while True:
    if src == 'location':
      break
    m = find_map(maps, src)
    range_index = m.get_range_index(num)
    if range_index != -1:
      num = m.ranges_dest[range_index] + num - m.ranges_min[range_index]
    src = m.dest
  return num

def simplify_seeds(seeds):
  i = 0
  j = 0
  seeds_new = []
  while True:
    if i >= len(seeds):
      break
    while True:
      if j >= seeds[i+1]:
        break
      print(f"{j}/{seeds[i+1]}")
      num = seeds[i] + j
      if num not in seeds_new:
        seeds_new.append(num)
      j += 1
    i += 2
  return seeds_new

def get_min_min(maps):
  min = sys.maxsize
  for map in maps:
    for x in map.ranges_min:
      if x < min:
        min = x
  return min

f = open("input.txt", "r")
lines = f.readlines()
seeds = get_seeds(lines[0])
maps = get_maps(lines[2:])
f.close()
num: int = seeds[0]
location = sys.maxsize

# # :)
# min_min = get_min_min(maps) # 201731623 for humidity
# min_min_input = sys.maxsize
# for i in range(len(seeds)):
#   min_min_input = min(min_min_input, seeds[i])
#   i += 2
# print(f"min_min_input: {min_min_input} min_min: {min_min}")
# if min_min_input < min_min:
#     print(f"hmm: {min_min_input}")

sdii = 0
while True:
  if sdii >= len(seeds):
    break
  sd = seeds[sdii]
  sdii += 2
  for sdi in range(seeds[sdii-1]):
    num = sd + sdi
    num = get_num_location(num)
    location = min(location, num)

# print(f"min location: {location}")
