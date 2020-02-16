def isValid(formula):
    formula = set(formula)
    
    if {1, 2} <= formula or {3,4} <= formula:
        return False
        
        
    if 5 in formula:
        if 6 in formula:
            return 7 in formula or 8 in formula
        
        return False
        
    
    if 6 in formula:
        if 5 in formula:
            return 7 in formula or 8 in formula
        
        return False
        
    
    return 7 in formula or 8 in formula