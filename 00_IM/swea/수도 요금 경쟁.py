import sys

sys.stdin = open("수도 요금 경쟁.txt", "r")

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P*W
    B = Q
    if W > R:
        B += S*(W-R)
    ans = min(A, B)
    print(f"#{tc} {ans}")