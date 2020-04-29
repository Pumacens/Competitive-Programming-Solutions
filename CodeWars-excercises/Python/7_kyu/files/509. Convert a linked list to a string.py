def stringify(node):
    if not node:
        return 'None'
    
    lst = [str(node.data)]
    next_node = node.next

    while next_node != None:
        lst.append(str(next_node.data))
        next_node = next_node.next

    return ' -> '.join(lst) + ' -> None'



# def stringify(list):
#     return 'None' if list == None else str(list.data) + ' -> ' + stringify(list.next)