import sys
sys.stdin = open("수 정렬하기 3.txt", "r")
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001
for i in range(N):
    cnt[int(input())] += 1
for j in range(10001):
    if cnt[j]:
        for k in range(cnt[j]):
            print(j)