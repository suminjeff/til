import sys

sys.stdin = open("재귀의 귀재.txt", "r")
input = sys.stdin.readline


def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


N = int(input())
for _ in range(N):
    string = input().rstrip()
    cnt = 0
    print(isPalindrome(string), cnt)