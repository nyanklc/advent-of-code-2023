# disgusting
from math import pow


box_x = [-1, 0, 1]
box_y = [-1, 0, 1]


class Obj:
    def __init__(self, value, x, y, typ):
        self.value = value
        self.x = x
        self.y = y
        self.type = typ
        self.adjacency_values = []

    def add_adjacent(self, value):
        self.adjacency_values.append(value)

    def is_adjacent_to(self, x, y):
        for ix in box_x:
            for iy in box_y:
                if ix == 0 and iy == 0:
                    continue
                if self.x+ix == x and self.y+iy == y:
                    return True
        return False

    def is_same(self, obj):
        if self.x == obj.x:
            if self.y == obj.y:
                return True
        return False

    def is_after(self, obj):
        if self.y != obj.y:
            return False
        if self.x != obj.x + 1:
            return False
        return True


class Num:
    def __init__(self, value, objects):
        self.value = value
        self.objects = objects

    def is_adjacent_to(self, x, y):
        for obj in self.objects:
            if obj.is_adjacent_to(x, y):
                return True
        return False


def construct_number(num_digits):
    value = 0
    for i in range(len(num_digits)):
        value += num_digits[-i-1].value * pow(10, i)
    return Num(value, num_digits)


def merge_numbers(obj_list):
    nums = []
    num_digits = []
    for i in range(len(obj_list)):
        if obj_list[i].type != 'digit':
            continue
        if len(num_digits) == 0:
            num_digits.append(obj_list[i])
            continue
        if obj_list[i].is_after(num_digits[-1]):
            num_digits.append(obj_list[i])
        else:
            nums.append(construct_number(num_digits))
            num_digits = []
            num_digits.append(obj_list[i])
    if len(num_digits) > 0:
        nums.append(construct_number(num_digits))
    return nums


def create_objects(input):
    obj_list = []
    idx_line = 0
    for line in input.readlines():
        idx = 0
        for ch in line:
            if ch == '\n':
                break
            if ch.isdigit():
                obj_list.append(Obj(int(ch), idx, idx_line, 'digit'))
            elif ch != '.':
                obj_list.append(Obj(-1, idx, idx_line, 'symbol'))
            idx += 1
        idx_line += 1
    return obj_list


f = open("input2.txt", "r")
lst = create_objects(f)
numbers = merge_numbers(lst)
added_nums = []
for obj in lst:
    if obj.type != 'symbol':
        continue
    for num in numbers:
        if num.is_adjacent_to(obj.x, obj.y):
            obj.add_adjacent(num.value)
            if num not in added_nums:
                added_nums.append(num)
numsum = 0
for num in added_nums:
    numsum += num.value
# print(f"sum: {numsum}")

gearsum = 0
for obj in lst:
    if obj.type != 'symbol':
        continue
    if len(obj.adjacency_values) == 2:
        mul = 1
        for gear in obj.adjacency_values:
            mul *= gear
        gearsum += mul
print(f"gearsum: {gearsum}")