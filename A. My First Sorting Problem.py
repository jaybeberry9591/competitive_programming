n = int(input())

for i in range(n):
    scores = list(map(int, input().split(' ')))
    scores.sort()
    print (scores[0],scores[-1])
