import sys
import fileinput

for line in fileinput.input():
    data = line.strip().split('\t')

    if len(data) != 6:
        continue

    date, time, location, item, amount, method = data

    print('%s\t%s' % (location, amount))

