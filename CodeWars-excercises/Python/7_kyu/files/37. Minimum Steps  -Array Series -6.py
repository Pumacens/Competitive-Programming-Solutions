def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    steps = 1
    sum_arr = numbers[0] + numbers[1]
    
    if sum_arr > value:
        return 0
    
    for i in range(2, len(numbers)):
        if sum_arr >= value:
            return steps
            
        sum_arr += numbers[i]
        steps += 1
    
    return steps



# def minimum_steps(arr, n):
#     arr = sorted(arr)
#     s = 0
#     for i,v in enumerate(arr): 
#         s += v
#         if s >= n: return i
    
    