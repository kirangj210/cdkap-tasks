import sys
sys.tracebacklimit = 0
d = {
    'A':'Hello',
    'B':'World',
    'C':'Buddy',
    'D':'Welcome'
}

taken = input()
length = len(taken)

if length <= 7:
    if taken[2] == 'a':
        print(d[taken[0]]+" "+d[taken[-1]]) #Hello World #Hello Buddy
elif length <= 13:
    if taken[0] == 'A' and taken[6] == 'B' and taken[12] == 'C':
        print(d[taken[0]]+" "+d[taken[6]]+" "+d[taken[12]]) #Hello World Buddy
elif length <= 14:
    if taken[0] == 'A' and (taken[7] == 'B' or taken[12] == 'C'):
        print(d[taken[0]]+" "+d[taken[7]]) #Hello World...
elif length <= 6:
    if taken[0] == 'D' or taken[5] == 'B':
        print(d[taken[5]]) #World.
elif length <= 6:
    if taken[0] == 'A' or taken[5] == 'B':
        print(d[taken[0]]) #Hello.
elif length <= 14:
    if taken[0] == 'A' and taken[7] == 'C' or taken[12] == 'D':
        print(d[taken[0]]+" "+d[taken[7]]) #Hello Buddy.
elif length <= 20:
    if taken[0] == 'A' and (taken[7] == 'B' or taken[12] == 'C') and taken[19] == 'D':
        print(d[taken[0]]+" "+d[taken[12]]+" "+d[taken[19]]) #Hello Buddy Welcome...
    
else:
    print("FAIL")