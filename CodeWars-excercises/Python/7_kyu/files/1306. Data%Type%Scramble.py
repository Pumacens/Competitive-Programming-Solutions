def make_model_year(lst):
    make = next(filter(lambda x: isinstance(x, str), lst))
    new = next(filter(lambda x: isinstance(x, bool), lst))
    model = ' '.join(next(filter(lambda x: isinstance(x, tuple), lst)))
    year = next(filter(lambda x: isinstance(x, int) and x not in (False, True), lst))
    
    return {'make': make,
            'model': model,
            'year':year,
            'new':new}
    
    

# id_=lambda k: lambda v: (k,v)

# CONFIG = {
#     bool:  id_('new'),
#     int:   id_('year'),
#     tuple: lambda t:('model',' '.join(t)),
#     str:   id_('make'),
# }

# def make_model_year(lst):
#     return dict( CONFIG[type(data)](data) for data in lst)