def side_len(x, y):
    result_lst = [i for i in range(abs(x-y)+1, x+y)]
    
    try:
        result_lst.remove((x**2 + y**2)**(1/2))
        return result_lst
        
    except ValueError:
        try: 
            result_lst.remove((max(x,y)**2 - min(x,y)**2)**(1/2))
            return result_lst
        
        except ValueError:
            return result_lst



# def side_len(x, y):
#     return [z for z in range(abs(x-y)+1,x+y) if z*z not in (abs(x*x-y*y), x*x+y*y)]