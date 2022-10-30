# try to run 

# This katamino solver was written for the part of the riddle (8x5). 
# Input is: a field and figures. In the beginning, point 5 and point 6. In case if quantity of figures changes, the function sltns() in point 5 must be changed, too.
# Output is:a picture presenting results
# The field and the figures are made of list and sublists. Sublists show rows. Ones stand for filled places, zeros - empty.
# This code runs faster through PyPy (Python 4000sec vs 3000sec PyPy).
# Some of the restrictions in point 4 are very specific and can be used only for these figures.

# Desired improvements:
# 1. Transfer all inputs at the beginning. Also compress point 5 into the flexible piece of code.
# 2. Some variables changed in point 3 so I had to use strings to keep them stable. Find a better solution.

import time
start = time.process_time()
from matplotlib import pyplot as plt  # for part 4
import math  # for part 4
# ----------------------------------------- input -----------------------------------------
# Field
field = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# Figures
g_curve = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
al_tr = [[1, 1, 1], [1, 1, 0]]
b_curve = [[1, 1, 1, 1], [1, 0, 0, 0]]
line = [[1, 1, 1, 1, 1]]
t_curve = [[1, 1, 1, 1], [0, 1, 0, 0]]
z_line = [[1, 1, 0, 0], [0, 1, 1, 1]]
b_z = [[0, 0, 1], [1, 1, 1], [1, 0, 0]]
c_curve = [[1, 1], [0, 1], [1, 1]]

initial_figures_list = [g_curve, al_tr, b_curve, line, t_curve, z_line, b_z, c_curve]
# -----------------------------------------------------------------------------------------
# 1. check of the square

field_rows = (len(field))
field_columns = (len(field[0]))

area = len(field)*len(field[0])

fig_sum = sum(iii for i in initial_figures_list for ii in i for iii in ii)

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

# 2. creation of all mirrored-rotated positions of each figure


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

# 3. find all positions on a field every figure can take


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

all_fig_list2 = sorted(concatenate(json.loads(second_ufc), fig_list_rows), key=len)

# 4 restrictions
# 4.1 pointless placement


def speed_up_mb():
    all_fig_list3 = []
    for fig_cls in all_fig_list2:
        new_cls = []
        for fig in fig_cls:
            if fig[0][0] == 0 and 1 in fig[0][1:] and (fig[1][0] == 1 or fig[2][0] == 1 or fig[3][0] == 1 or fig[4][0] == 1):
                continue
            elif fig[0][-1] == 0 and 1 in fig[0][:-1] and (fig[1][-1] == 1 or fig[2][-1] == 1 or fig[3][-1] == 1 or fig[4][-1] == 1):
                continue
            elif fig[-1][0] == 0 and 1 in fig[-1][1:] and (fig[0][0] == 1 or fig[1][0] == 1 or fig[2][0] == 1 or fig[3][0] == 1):
                continue
            elif fig[-1][-1] == 0 and 1 in fig[-1][:-1] and (fig[0][-1] == 1 or fig[1][-1] == 1 or fig[2][-1] == 1 or fig[3][-1] == 1):
                continue
            else:
                new_cls.append(fig)
        all_fig_list3.append(new_cls)

    # c_curve special
        # up and down

    all_fig_list4 = []
    for fig_cls in all_fig_list3:
        new_cls = []
        for fig in fig_cls:
            s_first = ''.join(str(i) for i in fig[0])
            s_last = ''.join(str(i) for i in fig[-1])
            if '101' in s_first or '101' in s_last:
                continue
            else:
                new_cls.append(fig)
        all_fig_list4.append(new_cls)

        # left and right
    all_fig_list5 = []
    for fig_cls in all_fig_list4:
        new_cls = []
        for fig in fig_cls:
            zzz = tuple(zip(*fig))
            s_first = ''.join(str(i) for i in zzz[0])
            s_last = ''.join(str(i) for i in zzz[-1])
            if '101' in s_first or '101' in s_last:
                continue
            else:
                new_cls.append(fig)
        all_fig_list5.append(new_cls)

    # line special

    all_fig_list5_5 = []
    for fig_cls in all_fig_list5:
        new_cls = []
        for fig in fig_cls:
            s_first = ''.join(str(i) for i in fig[1])
            s_last = ''.join(str(i) for i in fig[-2])
            zzz = tuple(zip(*fig))
            zzz_s_first = ''.join(str(i) for i in zzz[1])
            zzz_s_last = ''.join(str(i) for i in zzz[-2])

            zzz_s_first2 = ''.join(str(i) for i in zzz[2])
            zzz_s_last2 = ''.join(str(i) for i in zzz[-3])
            if ('11111' in s_first and (s_first[0] == '1' or s_first[-1] == '1')) or ('11111' in s_last and (s_last[0] == '1' or s_last[-1] == '1')):
                continue
            elif '11111' in zzz_s_first or '11111' in zzz_s_last or '11111' in zzz_s_first2 or '11111' in zzz_s_last2:
                continue
            else:
                new_cls.append(fig)
        all_fig_list5_5.append(new_cls)

    # b_curve special

    all_fig_list5_5_1 = []
    for fig_cls in all_fig_list5_5:
        new_cls = []
        for fig in fig_cls:
            s_first = ''.join(str(i) for i in fig[0])
            s_second = ''.join(str(i) for i in fig[1])
            end_s_first = ''.join(str(i) for i in fig[-1])
            end_s_second = ''.join(str(i) for i in fig[-2])
            zzz = tuple(zip(*fig))
            zzz_s_first = ''.join(str(i) for i in zzz[0])
            zzz_s_second = ''.join(str(i) for i in zzz[1])
            zzz_end_s_first = ''.join(str(i) for i in zzz[-1])
            zzz_end_s_second = ''.join(str(i) for i in zzz[-2])
            if (s_first.startswith('00001') and s_second.startswith('01111')) or (s_first.endswith('10000') and s_second.endswith('11110')) or (end_s_first.startswith('00001') and end_s_second.startswith('01111')) or (end_s_first.endswith('10000') and end_s_second.endswith('11110')):
                continue
            elif (zzz_s_first.startswith('00001') and zzz_s_second.startswith('01111')) or (zzz_s_first.endswith('10000') and zzz_s_second.endswith('11110')) or (zzz_end_s_first.startswith('00001') and zzz_end_s_second.startswith('01111')) or (zzz_end_s_first.endswith('10000') and zzz_end_s_second.endswith('11110')):
                continue
            else:
                new_cls.append(fig)
        all_fig_list5_5_1.append(new_cls)

    all_fig_list1_5 = tuple(tuple([tuple([tuple(i) for i in ii]) for ii in iii]) for iii in all_fig_list5_5_1)

    return tuple(sorted(all_fig_list1_5, key=len))


all_fig_list6 = speed_up_mb()

print('\nHow many positions each figure has: ')
[print(len(i)) for i in all_fig_list6]

total_combinations = 1
for i in all_fig_list6:
    total_combinations = total_combinations * len(i)
print('\nThe total number of the combinations: ' + str(total_combinations))

# 4.2 pointless combinations

pattern = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
pattern_bigger = [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0]]
pattern_bigger_h = [[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
pattern_three_row_vert = [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]]
pattern_three_row_horiz = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
pattern_three_NW = [[0, 0, 1, 0],
                    [0, 1, 0, 1],
                    [1, 0, 0, 1],
                    [0, 1, 1, 0]]
pattern_three_NE = [[0, 1, 0, 0],
                    [1, 0, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 1, 0]]
pattern_three_SW = [[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0]]
pattern_three_SE = [[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [1, 0, 1, 0],
                    [0, 1, 0, 0]]
pattern_four_cube = [[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [0, 1, 1, 0]]


def find_pattern_four_cube(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1:3] == pattern[0][1:3] and local[1] == pattern[1] and local[2] == pattern[2] and local[3][
                                                                                                          1:3] == \
                    pattern[3][1:3]:
                return True


def find_pattern_three_SE(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1:3] == pattern[0][1:3] and local[1] == pattern[1] and local[2][0] == pattern[2][0] and \
                    local[2][2] == pattern[2][2] and local[3][1] == pattern[3][1]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_four_cube(grid, pattern_four_cube) is True:
                    return True


def find_pattern_three_SW(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1:3] == pattern[0][1:3] and local[1] == pattern[1] and local[2][1] == pattern[2][1] and \
                    local[2][-1] == pattern[2][-1] and local[3][2] == pattern[3][2]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_SE(grid, pattern_three_SE) is True:
                    return True


def find_pattern_three_NE(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1] == pattern[0][1] and local[1][0] == pattern[1][0] and local[1][2] == pattern[1][2] and local[
                2] == pattern[2] and local[3][1:3] == pattern[3][1:3]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_SW(grid, pattern_three_SW) is True:
                    return True


def find_pattern_three_NW(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][2] == pattern[0][2] and local[1][1] == pattern[1][1] and local[1][-1] == pattern[1][-1] and \
                    local[2] == pattern[2] and local[3][1:3] == pattern[3][1:3]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_NE(grid, pattern_three_NE) is True:
                    return True


def find_pattern_three_row_horizontal(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1:4] == pattern[0][1:4] and local[1] == pattern[1] and local[2][1:4] == pattern[2][1:4]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_NW(grid, pattern_three_NW) is True:
                    return True


def find_pattern_three_row_vertical(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1] == pattern[0][1] and local[1] == pattern[1] and local[2] == pattern[2] and local[3] == \
                    pattern[3] and local[4][1] == pattern[4][1]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_row_horizontal(grid, pattern_three_row_horiz) is True:
                    return True


def find_pattern_bigger_horizontal(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1:3] == pattern[0][1:3] and local[1] == pattern[1] and local[2][1:3] == pattern[2][1:3]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_three_row_vertical(grid, pattern_three_row_vert) is True:
                    return True


def find_pattern_bigger(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1] == pattern[0][1] and local[1] == pattern[1] and local[2] == pattern[2] and local[3][1] == \
                    pattern[3][1]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_bigger_horizontal(grid, pattern_bigger_h) is True:
                    return True


def find_pattern(grid, pattern):
    for x in range(len(grid[0]) - len(pattern[0]) + 1):
        for y in range(len(grid) - len(pattern) + 1):
            local = grid[y:y + len(pattern)]
            local = [e[x:x + len(pattern[0])] for e in local]
            if local[0][1] == pattern[0][1] and local[1] == pattern[1] and local[2][1] == pattern[2][1]:
                return True
            elif (len(grid[0]) - len(pattern[0]) + 1) * (len(grid) - len(pattern) + 1) == ((x + 1) * (y + 1)):
                if find_pattern_bigger(grid, pattern_bigger) is True:
                    return True


# 5 searching for the solutions


def comparison(c_p):
    lst = []
    for tr in zip(*c_p):
      if all([sum(tr) < 2 for tr in zip(*tr)]) is not True:
        return None
      else:
        lst.append([sum(tr) for tr in zip(*tr)])
    if find_pattern(lst, pattern) is not True:
        return c_p


def sltns():
    l1,l2,l3,l4,l5,l6,l7,l8 = (i for i in all_fig_list6)  # input (need to change before the start)
    i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = 0                            # input (need to change before the start)
    results = []
    while i1 < len(l1):
        if i1 < len(l1) and i2 < len(l2):
            while i2 < len(l2):
                if comparison([l1[i1]] + [l2[i2]]) is not None:
                    while i3 < len(l3):
                        if comparison([l1[i1]] + [l2[i2]] + [l3[i3]]) is not None:
                            while i4 < len(l4):
                                if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]]) is not None:
                                    while i5 < len(l5):
                                        if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]] + [l5[i5]]) is not None:
                                            while i6 < len(l6):
                                                if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]] + [l5[i5]] + [l6[i6]]) is not None:
                                                    while i7 < len(l7):
                                                        if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]] + [l5[i5]] + [l6[i6]] + [l7[i7]]) is not None:
                                                            while i8 < len(l8):
                                                                if comparison([l1[i1]] + [l2[i2]] + [l3[i3]] + [l4[i4]] + [l5[i5]] + [l6[i6]] + [l7[i7]] + [l8[i8]]) is not None:
                                                                    results.append([l1[i1], l2[i2], l3[i3], l4[i4], l5[i5], l6[i6], l7[i7], l8[i8]])
                                                                    print('\nTaken time: ' + str(time.process_time() - start))
                                                                    i8 += 1
                                                                else:
                                                                    i8 += 1
                                                            i8 = 0
                                                            i7 += 1
                                                        else:
                                                            i7 += 1
                                                    i7 = 0
                                                    i6 += 1
                                                else:
                                                    i6 += 1
                                            i6 = 0
                                            i5 += 1
                                        else:
                                            i5 += 1
                                    i5 = 0
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

    return(results)


results = sltns()
print('\nHow many solutions are: ' + str(len(results)))

# 6. visual part


def vis():
    visual_results = []
    for result in results:
        f2 = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]  # find the way change this in the beginning
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
    return (visual_results)


visual_results = vis()
d_grid = math.ceil(len(visual_results)**0.5)

rows = columns = d_grid

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


print('\nTaken time: ' + str(time.process_time() - start))
