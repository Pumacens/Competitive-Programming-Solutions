def am_I_afraid(day,num):
    return day=='Monday' and num == 12 or \
       day=='Tuesday' and num > 95 or \
       day=='Wednesday' and num == 34 or \
       day=='Thursday' and num == 0 or \
       day=='Friday' and num % 2==0 or \
       day=='Saturday' and num == 56 or \
       day=='Sunday' and num in (666, -666)

        
# def am_I_afraid(day,num):
#     return {
#         'Monday':  num == 12,
#         'Tuesday': num > 95,
#         'Wednesday': num == 34,
#         'Thursday': num == 0,
#         'Friday': num % 2 == 0,
#         'Saturday': num ==  56,
#         'Sunday': num == 666 or num == -666,
#     }[day]