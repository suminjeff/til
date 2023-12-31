import sys
sys.stdin = open("13241_최소공배수.txt", "r")
input = sys.stdin.readline

A, B = map(int, input().split())
if A % B == 0 or B % A == 0:
    print(max(A, B))
else:
    pA, pB = A, B
    while A != B:
        if A < B:
            A += pA
        elif B < A:
            B += pB
    print(A)