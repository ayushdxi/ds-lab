import sys
import fileinput

prev_country = None
count = 0
prev_cases = 0

print('=================================')
for line in fileinput.input():
    # print(line)
    data = line.strip().split(',')

    if len(data) != 2:
        print("error")
        continue
    
    # print(data)
    country, cases = data
    cases = int(cases)
    if country == prev_country:
        prev_cases += cases
    else :
        if prev_country:
            print('%s\t%s'%(prev_country, prev_cases))
        prev_country = country
        prev_cases = cases

# if prev_country is not None:
#     print('%s\t%s'%(prev_country, prev_cases))

