from itertools import groupby
from operator import itemgetter
import sys
import fileinput

def read_mapper_output(file, separator):
    for line in file:
        yield line.strip().split(separator)

def main(separator = '\t'):

    data = read_mapper_output(fileinput.input(), separator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print('%s%s%d'%(current_word, separator, total_count))
        except ValueError:
            pass

if __name__ == "__main__":
    main()


