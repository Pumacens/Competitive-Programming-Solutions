def top3(products, amounts, prices):
    products_dict = {products[i]:(amounts[i], prices[i]) for i in range(len(products))}
    return sorted(products_dict, key= lambda x: products_dict[x][0] * products_dict[x][1], reverse=True)[:3]



# def top3(*args):
#     return [item[0] for item in sorted(zip(*args), key=lambda x: x[1]*x[2], reverse=True)[:3]]