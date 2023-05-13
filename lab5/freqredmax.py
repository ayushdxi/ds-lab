import sys

curr_max = -1
max_freq = []
for line in sys.stdin:
    word, count = line.strip().split('\t', 1)
    count = int(count)

    if count > curr_max:
        curr_max = count
        max_freq = [word]

    elif count == curr_max:
        max_freq.append(word)

for word in max_freq:
    print('%s\t%s'%(word, curr_max))

