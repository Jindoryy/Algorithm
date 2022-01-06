from sys import stdin
input = stdin.readline

score = [ input().split() for _ in range(int(input())) ]

score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in score:
    print(x[0])
