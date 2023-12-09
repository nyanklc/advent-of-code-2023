def predict_next(seq):
    if all(i == seq[0] for i in seq):
        return seq[0]
    diffs = []
    for i in range(len(seq)-1):
        diffs.append(seq[i+1]-seq[i])
    return seq[len(seq)-1] + predict_next(diffs)


f=open("input.txt", "r")
seqs = []
for line in f.readlines():
    seqs.append([int(x) for x in line.strip().split()])
predictions = [predict_next(list(reversed(seq))) for seq in seqs]
print(f"predictions: {predictions}")
print(f"sum: {sum(predictions)}")

