def find_children(santas_list, children):
    return sorted(child for child in children if child in santas_list)


# def find_children(santas_list, children):
#     return sorted(set(santas_list) & set(children))