Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@guivandm 
guivandm
/
solver
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
solver
/
ccc.py
in
main
 

Spaces

4

No wrap
1
l1 = [1, 2, 3, 4, 5]
2
l2 = [6, 7, 8, 9, 10, 11]
3
l3 = [12, 13, 14, 15, 16, 17, 18]
4
l4 = [19, 30, 21, 22, 23, 24, 25, 26]
5
lsts = [l1, l2, l3, l4]
6
i1 = 0
7
i2 = 0
8
i3 = 0
9
i4 = 0
10
iterables = [i1, i2, i3, i4]
11
max_sum = 51
12
print("Expected quantity: ")
13
print(5 * 6 * 7 * 8)
14
​
15
​
16
def big_thing(result, i1, i2, i3, i4):
17
    if l1[i1] + l2[i2] < max_sum:
18
        if l1[i1] + l2[i2] + l3[i3] < max_sum:
19
            if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
20
                result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
21
                i4 += 1
22
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
23
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
24
​
25
        else:
26
            i3 += 1
27
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
28
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
29
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
30
                    i4 += 1
31
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
32
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
33
​
34
            else:
35
                i4 += 1
36
                if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
37
                    result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
38
                    i4 += 1
39
                    if l1[i1] + l2[i2] + l3[i3] + l4[i4] < max_sum:
40
                        result.append([l1[i1], l2[i2], l3[i3], l4[i4]])
41
​
42
    else:
43
        i2 += 1
44
        if l1[i1] + l2[i2] < max_sum:
45
            if l1[i1] + l2[i2] + l3[i3] < max_sum:
@guivandm
Commit changes
Commit summary
Create ccc.py
Optional extended description
Add an optional extended description…
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications
