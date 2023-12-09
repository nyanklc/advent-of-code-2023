# yeah I gave up and just used lcm

from math import lcm

class Node:
    def __init__(self, this, left, right):
        self.this = this
        self.right = right
        self.left = left

def get_node(g, gm, n):
    return g[gm[n]]    

def identify_starts(g, gm):
    starts = []
    for node in g:
        if node.this[2] == 'A':
            starts.append(gm[node.this])
    return starts

def is_end(currs):
    for curr in currs:
        if curr.this[2] != 'Z':
            return False
    return True

def will_end(lengths):
    return all(i == lengths[0] for i in lengths)

def move(node, rli, num, g, gm):
    curr = node
    for i in range(num):
        if rl[rli % len(rl)] == 'L':
            curr = get_node(g, gm, curr.left)
        else:
            curr = get_node(g, gm, curr.right)
        rli += 1
    return curr

# incomplete attempt on a generic algorithm without 'path loops'
def traverse(rl, g, gm, starts):
    currs = starts
    count = 0
    while not is_end(currs):
        curr_lengths = [identify_traversal_length(rl, g, gm, curr, count) for curr in currs]
        print(f"steps until end: {curr_lengths}")
        print(f"currents: {[curr.this for curr in currs]}")
        if -1 in curr_lengths:
            print("what")
            quit()
        if will_end(curr_lengths):
            count += max(curr_lengths)
            return count
        # index of current one which will reach end the earliest
        idx = curr_lengths.index(min([c[0] for c in curr_lengths]))
        currs[idx] = move(currs[idx], count, curr_lengths[idx], g, gm)
        # ...
        count += min([c[0] for c in curr_lengths])
        for i in range(len(currs)):
            currs[i] = g[gm[curr_lengths[i][1]]]
        print(f"after update currents: {[curr.this for curr in currs]}")
        # for curr in currs:
        #     if rl[count % len(rl)] == 'L':
        #         currs[currs.index(curr)] = get_node(g, gm, curr.left)
        #     else:
        #         currs[currs.index(curr)] = get_node(g, gm, curr.right)
        # count += 1
    return count

# can precompute all possible versions of this also
def identify_traversal_length(rl, g, gm, start, c):
    curr = start
    curr_initial = curr
    count = c
    while count == 0 or not curr.this[2] == 'Z':
        if curr.this == curr.left and curr.this == curr.right: return -1
        if rl[count % len(rl)] == 'L':
            curr = get_node(g, gm, curr.left)
        else:
            curr = get_node(g, gm, curr.right)
        count += 1
    return count - c, curr.this


f=open("input.txt", "r")
lines = f.readlines()
rl = lines[0].strip()
g = [] # graph
gm = {} # map name->index in graph
i = 0
for line in lines[2:]:
    this = line.split()[0]
    left = line.split()[2][1:-1]
    right = line.split()[3][:-1]
    g.append(Node(this, left, right))
    gm[this] = i
    i += 1
starts = [g[x] for x in identify_starts(g, gm)]
start_traversal_lengths = [identify_traversal_length(rl, g, gm, start, 0) for start in starts]
r = lcm(*[s[0] for s in start_traversal_lengths])
print(f"result: {r}")
