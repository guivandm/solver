import time
start = time.process_time()

all_fig_list2 = [[[[0, 0, 0], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 1, 1]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 1]], [[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [1, 0, 0], [1, 0, 0]]], [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]], [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 1, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 1]], [[0, 0, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 1]], [[0, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 1, 0]], [[0, 0, 0], [1, 0, 0], [1, 0, 0]], [[0, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[1, 1, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [1, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 1, 0], [0, 1, 1]], [[0, 0, 0], [0, 0, 1], [0, 1, 1]], [[0, 0, 0], [0, 1, 1], [0, 1, 0]], [[0, 0, 0], [1, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 0, 0], [1, 1, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 0]], [[0, 0, 0], [1, 1, 0], [1, 0, 0]], [[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[0, 1, 0], [0, 1, 1], [0, 0, 0]], [[0, 0, 1], [0, 1, 1], [0, 0, 0]], [[0, 1, 1], [0, 1, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 0], [0, 0, 0]], [[1, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 1, 0], [1, 1, 0], [0, 0, 0]], [[1, 1, 0], [1, 0, 0], [0, 0, 0]]]]


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


results_first_two = []
for clss in range(1, len(all_fig_list2[:2])):
    for elm in all_fig_list2[clss-1]:
        for elm2 in all_fig_list2[clss]:
            if comparison([elm] + [elm2]) is not None:
                results_first_two.append([elm] + [elm2])

results = results_first_two
print('\nHow many possible solutions are: ')
print(len(results))

tmp = []
for i in range(2, len(all_fig_list2)):
    if i == 2:
        for nm, elmr in enumerate(results):
            for nm2, elmr2 in enumerate(all_fig_list2[2]):
                if comparison(elmr + [elmr2]) is not None:
                    tmp.append(elmr + [elmr2])
        print(len(tmp))
    else:
        tmp2 = []
        for nm, elmr in enumerate(tmp):
            for nm2, elmr2 in enumerate(all_fig_list2[i]):
                if comparison(elmr + [elmr2]) is not None:
                    tmp2.append(elmr + [elmr2])
        tmp *= 0
        tmp = [i for i in tmp2]
        print(len(tmp))
        tmp2 *= 0

print('\nHow many possible solutions are: ')
print(len(tmp))

elapsed = (time.process_time() - start)
print('\nTaken time: ' + str(elapsed))
