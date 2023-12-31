def solution(dartResult):
    stack = []
    point = {'S': 1, 'D': 2, 'T': 3}
    # for i in dartResult:
    i = 0
    while i < len(dartResult):
        if dartResult[i].isnumeric():
            num = ""
            while dartResult[i].isnumeric():
                num += dartResult[i]
                i += 1
            stack.append(int(num))
        elif dartResult[i] in point:
            stack.append(stack.pop() ** point[dartResult[i]])
            i += 1
        else:
            if dartResult[i] == "*":
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * 2)
                    stack.append(a * 2)
                else:
                    stack.append(stack.pop() * 2)
            else:
                stack.append(stack.pop() * (-1))
            i += 1
    answer = sum(stack)
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))

stack = []
point = {'S': 1, 'D': 2, 'T': 3}
# for i in dartResult:
# i = 0
# while i < len(dartResult):
#     if dartResult[i].isnumeric():
#         num = ""
#         while dartResult[i].isnumeric():
#             num += dartResult[i]
#             i += 1
#         stack.append(int(num))
#     elif dartResult[i] in point:
#         stack.append(stack.pop() ** point[dartResult[i]])
#         i += 1
#     else:
#         if dartResult[i] == "*":
#             if len(stack) > 1:
#                 a = stack.pop()
#                 b = stack.pop()
#                 stack.append(b * 2)
#                 stack.append(a * 2)
#             else:
#                 stack.append(stack.pop() * 2)
#         else:
#             stack.append(stack.pop() * (-1))
#         i += 1
# answer = sum(stack)
# print(answer)