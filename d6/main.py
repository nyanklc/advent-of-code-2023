def get_record_count_min_max(race):
    mn = race[0]
    mx = 0
    for i in range(race[0]):
        if i*(race[0]-i) > race[1]:
            mn = i
            break
    for i in reversed(range(race[0])):
        if i*(race[0]-i) > race[1]:
            mx=i
            break
    return mx-mn+1

# # naive approach
# def get_distances(race):
#     d=[]
#     for i in range(race[0]):
#         d.append(i*(race[0]-i))
#     return d
# def get_record_counts(race_distances, race):
#     count=0
#     record=race[1]
#     for r in range(race_distances):
#         if race_distances[r] > record:
#             count+=1
#     return count


f=open("input.txt", "r")
lines=f.readlines()
race=int(lines[0].strip().split()[1]), int(lines[1].strip().split()[1])
print(f"race: {race}")
print(f"result: {get_record_count_min_max(race)}")