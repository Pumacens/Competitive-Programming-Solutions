def row_sum_odd_numbers(n):
    start_odd = 2*sum(range(n)) + 1
    end_odd = 2*(sum(range(n)) + n - 1) + 1
    return sum(range(start_odd, end_odd+1, 2))


# def row_sum_odd_numbers(n):
#     #your code here
#     return n ** 3