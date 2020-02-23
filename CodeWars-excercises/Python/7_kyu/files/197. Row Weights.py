def row_weights(array):
    return (sum(array[::2]), sum(array[1::2]))



# def row_weights(array):
#     odd = 0
#     even = 0
#     for i in range(len(array)):
#         if i%2 == 0:
#             odd += array[i]
#         else:
#             even += array[i]
#     return odd, even