if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     if n < 2:
#         raise Exception("not found")
    
#     import sys
#     max_score = -sys.maxsize
#     result = -sys.maxsize
    
#     for a in arr:
#         if a > max_score:
#             result = max_score
#             max_score = a
#         elif a > result and a < max_score:
#             result = a
    
#     print(result)