l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11]
l3 = [12, 13, 14, 15, 16, 17, 18]
l4 = [19, 30, 21, 22, 23, 24, 25, 26]
lsts = [l1, l2, l3, l4]
i1 = 0
i2 = 0
i3 = 0
i4 = 0
iterables = [i1, i2, i3, i4]
max_sum = 51
print("Expected quantity: ")
print(5 * 6 * 7 * 8)


def big_thing(result, i1, i2, i3, i4):
    if l1[i1] + l2[i2] < max_sum:
        if l1[i1] + l2[i2] + l3[i3] < max_sum:
            if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                i4 += 1
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

        else:
            i3 += 1
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

            else:
                i4 += 1
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

    else:
        i2 += 1
        if l1[i1] + l2[i2] < max_sum:
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

            else:
                i3 += 1
                if l1[i1] + l2[i2] + l3[i3] < max_sum:
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                        i4 += 1
                        if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                            result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

                else:
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                        i4 += 1
                        if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                            result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                            i4 += 1
                            if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                                result.append([l1[i1], l2[i2], l3[i3], l4[i4]])


result = []
print(len(l1), len(l2), len(l3), len(l4))
while i1 < len(l1) or i2 < len(l2) or i3 < len(l3) or i4 < len(l4):
    print(result)
    if l1[i1] + l2[i2] < max_sum:
        if l1[i1] + l2[i2] + l3[i3] < max_sum:
            if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                i4 += 1
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    big_thing(result, i1, i2, i3, i4)

        else:
            i3 += 1
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

            else:
                i4 += 1
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

    else:
        i2 += 1
        if l1[i1] + l2[i2] < max_sum:
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

            else:
                i3 += 1
                if l1[i1] + l2[i2] + l3[i3] < max_sum:
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                        i4 += 1
                        if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                            result.append([l1[i1], l2[i2], l3[i3], l4[i4]])

                else:
                    i4 += 1
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                        i4 += 1
                        if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                            result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
                            i4 += 1
                            if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                                result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
