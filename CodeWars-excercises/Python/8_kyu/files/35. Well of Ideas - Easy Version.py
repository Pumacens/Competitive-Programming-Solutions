def well(x):
    num_goods = x.count('good')
    return {num_goods == 0: 'Fail!',
            1 <= num_goods <= 2: 'Publish!',
            num_goods > 2: 'I smell a series!'
    }[True]