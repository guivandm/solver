import time
start = time.process_time()

# Field

field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

field_rows = (len(field))
field_columns = (len(field[0]))

# 1. create all mirrored-rotated positions of a figure

cube = [[1]]
s_line = [[1, 1]]
b_line = [[1, 1, 1]]
curve = [[1, 1], [0, 1]]

initial_figures_list = [cube, s_line, b_line, curve]

area = 0
for i in field:
    for ii in i:
        area += 1

fig_sum = 0
for i in initial_figures_list:
    for ii in i:
        for iii in ii:
            fig_sum = fig_sum + iii

if abs(area - fig_sum) == 1:
    sq_or_sqs = ' square'
else:
    sq_or_sqs = ' squares'

if fig_sum == area:
    print("OK. Areas of the field and figures are equal.")
elif area > fig_sum:
    print("There aren't enough figures to fill the area completely. Need " + str(area - fig_sum) + sq_or_sqs + " more.")
    exit()
elif fig_sum > area:
    print("You can't fit so many figures. Need " + str(fig_sum - area) + sq_or_sqs + " less.")
    exit()


def t_pose(fig):
    return [[fig[j][ii] for j in range(len(fig))] for ii in range(len(fig[0]))]


def rotation(fig):
    return [list(a) for a in list(zip(*fig[::-1]))]


fig_classes = []
for in_fig in initial_figures_list:
    fig_class = []
    fig_class.append(in_fig)
    if t_pose(in_fig) not in fig_class:
        fig_class.append(t_pose(in_fig))
    if rotation(in_fig) not in fig_class:
        fig_class.append(rotation(in_fig))
    if rotation(rotation(in_fig)) not in fig_class:
        fig_class.append(rotation(rotation(in_fig)))
    if rotation(rotation(rotation(in_fig))) not in fig_class:
        fig_class.append(rotation(rotation(rotation(in_fig))))
    if rotation(t_pose(in_fig)) not in fig_class:
        fig_class.append(rotation(t_pose(in_fig)))
    if rotation(rotation(t_pose(in_fig))) not in fig_class:
        fig_class.append(rotation(rotation(t_pose(in_fig))))
    if rotation(rotation(rotation(t_pose(in_fig)))) not in fig_class:
        fig_class.append(rotation(rotation(rotation(t_pose(in_fig)))))
    fig_classes.append(fig_class)


def separate_print(not_sep_list):
    counter = 0
    print('Classes: ' + str(len(not_sep_list)))
    for i in not_sep_list:
        print('Items in class: ' + str(len(i)))
        for ii in i:
            print(ii)
            counter += 1
    print('All items: ' + str(counter))


# 2. find all positions on a field every figure can take


def adding_zeros(fig):
    fig_rows = (len(fig))
    fig_columns = (len(fig[0]))
    difference_rows = field_rows - fig_rows
    difference_columns = field_columns - fig_columns
    for zero in range(difference_columns):
        for row in fig:
            row.append(0)
    for zero in range(difference_rows):
        fig.append([0]*field_columns)
    return fig


figures_list_zeros = []
for f_class in fig_classes:
    class_zeros = [adding_zeros(i) for i in f_class]
    figures_list_zeros.append(class_zeros)

safe = str(figures_list_zeros)
fig_columns = []
for i in figures_list_zeros:
    fig_list_columns = []
    for fig_z in i:
        while all(row[-1] == 0 for row in fig_z):
            lst = []
            for row in fig_z:
                row.pop()
                row.insert(0, 0)
                lst.append(row.copy())
            fig_list_columns.append(lst)
    fig_columns.append(fig_list_columns)

import json
unsafe = json.loads(safe)


def concatenate(first, second):
    for i in first:
        for ii in i:
            second[first.index(i)].append(ii)
    return second


unsafe_fig_columns = concatenate(unsafe, fig_columns)

second_ufc = str(unsafe_fig_columns)

fig_list_rows = []

for i in unsafe_fig_columns:
    fig_co = []
    for fig_c in i:
        while all(element == 0 for element in fig_c[-1]):
            fig_c.pop()
            fig_c.insert(0, [0]*field_columns)
            fig_co.append(fig_c.copy())
    fig_list_rows.append(fig_co)

second_unsafe = json.loads(second_ufc)

all_fig_list = concatenate(second_unsafe, fig_list_rows)

all_fig_list1_5 = tuple(tuple([tuple([tuple(i) for i in ii]) for ii in iii]) for iii in all_fig_list)

all_fig_list2 = tuple(sorted(all_fig_list1_5, key=len))

print('\nHow many positions each figure has: ')
for i in all_fig_list2:
    print(len(i))
total_combinations = 1
for i in all_fig_list2:
    total_combinations = total_combinations * len(i)
print('\nThe total number of the combinations: ' + str(total_combinations))

# 3. appropriate combinations


def comparison(c_p):
    lst_check = []
    for tr in zip(*c_p):
        zip_row = zip(*tr)
        if all([sum(tr) < 2 for tr in zip_row]) is True:
            [lst_check.append(tr) for tr in [sum(tr) < 2 for tr in zip_row]]
        else:
            return None
    if all(el is True for el in lst_check):
        return c_p
    else:
        return None


l1 = all_fig_list2[0]
l2 = all_fig_list2[1]
l3 = all_fig_list2[2]
l4 = all_fig_list2[3]

i1 = i2 = i3 = i4 = 0

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

print('\nHow many solutions are: ')
print(len(results))

# 4. visual part

from matplotlib import pyplot as plt
import math

visual_results = []
for result in results:
    f2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # find the way change this in the beginning
    for fgr in result:
        row_counter = 0
        for rw in fgr:
            el_counter = 0
            for nmbr in rw:
                if nmbr == 1:
                    f2[row_counter][el_counter] = result.index(fgr)
                el_counter += 1
            row_counter += 1

    visual_results.append(f2)

d_grid = math.ceil(len(visual_results)**0.5)

rows = d_grid
columns = d_grid

fig = plt.figure(figsize=(10, 7))

counter = 1
for i in visual_results:
    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, counter)
    counter += 1
    # showing image
    plt.imshow(i)
    plt.axis('off')
plt.show()

elapsed = (time.process_time() - start)
print('\nTaken time: ' + str(elapsed))
