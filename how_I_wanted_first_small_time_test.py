import time
start = time.process_time()

all_fig_list2 = [[[[0, 0, 0], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 1, 1]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 1]], [[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [1, 0, 0], [1, 0, 0]]], [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]], [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 1, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 1]], [[0, 0, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 1]], [[0, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 1, 0]], [[0, 0, 0], [1, 0, 0], [1, 0, 0]], [[0, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[1, 1, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [1, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 1, 0], [0, 1, 1]], [[0, 0, 0], [0, 0, 1], [0, 1, 1]], [[0, 0, 0], [0, 1, 1], [0, 1, 0]], [[0, 0, 0], [1, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 0, 0], [1, 1, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 0]], [[0, 0, 0], [1, 1, 0], [1, 0, 0]], [[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[0, 1, 0], [0, 1, 1], [0, 0, 0]], [[0, 0, 1], [0, 1, 1], [0, 0, 0]], [[0, 1, 1], [0, 1, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 0], [0, 0, 0]], [[1, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 1, 0], [1, 1, 0], [0, 0, 0]], [[1, 1, 0], [1, 0, 0], [0, 0, 0]]]]


# 3. appropriate combinations

l1 = all_fig_list2[0]
l2 = all_fig_list2[1]
l3 = all_fig_list2[2]
l4 = all_fig_list2[3]


def comparison(c_p):  # expected input with rows: row in elm in clss    [clss[elm[row]]]
    lst_check = []                                     # how to rid of creation of list checking items?
    for tr in zip(*c_p):                             # If one el is False break the loop and jump to the next result.
        zip_row = zip(*tr)
        check = [sum(tr) < 2 for tr in zip_row]
        [lst_check.append(tr) for tr in check]
    if all(el is True for el in lst_check):
        return c_p
    else:
        return None


i1 = 0
i2 = 0
i3 = 0
i4 = 0

results = []

while i1 < len(l1):
    if i1 < len(l1) and i2 < len(l2):
        while i2 < len(l2):
            if comparison([l1[i1]] + [l2[i2]]) is not None:
                while i3 < len(l3):
                    if comparison([l1[i1]] + [l2[i2]] + [l3[i3]]) is not None:
                        while i4 < len(l4):
                            if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]]) is not None:
                                results.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                                i4 += 1
                            else:
                                i4 += 1
                        i4 = 0
                        i3 += 1
                    else:
                        i3 += 1
                i3 = 0
                i2 += 1
            else:
                i2 += 1
        i2 = 0
        i1 += 1

print('\nHow many possible solutions are: ')
print(len(results))

elapsed = (time.process_time() - start)
print('\nTaken time: ' + str(elapsed))
