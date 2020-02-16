def _if(b, func1, func2):
  (func1() if b else func2())


# def _if(bool, func1, func2):
#     return func1() if bool else func2()