

def valid_game(line):
    red_max = 0
    green_max = 0
    blue_max = 0
    split = line.split(' ')
    id = int(split[1][:-1])
    idx = 2
    while idx < len(split):
        count = int(split[idx])
        print(f"count: {count}")
        color = split[idx+1]
        print(f"color: {color}")
        if 'blue' in color:
            if count > blue_max:
                blue_max = count
        elif 'red' in color:
            if count > red_max:
                red_max = count
        elif 'green' in color:
            if count > green_max:
                green_max = count
        idx += 2
    return red_max, green_max, blue_max


f = open("input.txt", "r")
power_sum = 0
for line in f.readlines():
    red, green, blue = valid_game(line)
    power = red * green * blue
    power_sum += power

print(f"sum of powers: {power_sum}")
