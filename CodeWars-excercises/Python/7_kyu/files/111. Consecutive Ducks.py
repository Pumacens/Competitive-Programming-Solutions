from math import log10

def consecutive_ducks(n):
    return not (log10(n) / log10(2)).is_integer()



# from math import log10

# def consecutive_ducks(n):
#     return not (log10(n) / log10(2)).is_integer()




# def consecutive_ducks(n):
#     for i in range(n - n//2, 2, -1):
#         j = i-2
#         suma = (i + j + 1)*(i - j) // 2
        
#         if suma == n:
#             return True
            
#         while suma < n and j > 0:
#             j -= 1
#             suma = (i + j + 1)*(i - j) // 2

# #             if j == 0:
# #                 break

#         if suma == n:
#             return True
            
#     return False

