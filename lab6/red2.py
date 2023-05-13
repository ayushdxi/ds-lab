# import sys
# import fileinput

# res = []
# prev_loc = None
# prev_max_loc = None
# prev_max_amount = -1
# for line in fileinput.input():
#     data = line.strip().split('\t')

#     if len(data) != 2:
#         continue

#     location, amount = data

#     if prev_loc is None:
#          prev_loc = location
#          prev_max_amount = amount

#     if prev_loc and prev_loc != location:
#         print('%s\t%s'%(prev_loc, prev_max_amount))
#         prev_max_amount = -1
#         prev_loc = location
#         if float(amount) > float(prev_max_amount):
#             prev_max_amount = amount
         


# if prev_loc != None:
#         print('%s\t%s'%(prev_loc, prev_max_amount))

import fileinput
max_value = 0
old_key = None
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) != 2:
# Something has gone wrong. Skip this line.
        continue
current_key, current_value = data
# Refresh for new keys (i.e. locations in the example context)
if old_key and old_key != current_key:
    print (old_key, "\t", max_value)
    old_key = current_key
    max_value = 0
    old_key = current_key
    if float(current_value) > float(max_value):
        max_value = float(current_value)
if old_key != None:
    print (old_key, "\t", max_value)
