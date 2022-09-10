l1 = [1, 2, 3, 4, 5]
l2 = [6,7, 8, 9, 10, 11]
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

result = []
print(len(l1), len(l2), len(l3), len(l4))
while i1 < len(l1):
   if i1 < len(l1) and i2 < len(l2):
      while i2 < len(l2):
        if l1[i1] + l2[i2] < max_sum:
            while i3 < len(l3):
              if l1[i1] + l2[i2] + l3[i3] < max_sum:
                while i4 < len(l4):
                  if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
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
  
print('\n\n\n\n\n')
print(result)                        
                                
