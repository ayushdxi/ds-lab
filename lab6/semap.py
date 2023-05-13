import sys
import fileinput

def read_input(file, separator):
    for line in file:
        yield line.strip().split(separator)

def main(separator = '\t'):
    data = read_input(fileinput.input(), separator)
    print(data)
    for words in data:
        print(words)
        for word in words:
            print('%s%s%d'%(word, separator, 1))

if __name__ == "__main__":
    main()

