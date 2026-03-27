def stringify(node):
    if node == None:
        return 'None'
    answ = ''
    current = node
    while current is not None:
        answ += f'{current.data}'
        answ += " -> "
        current = current.next
    answ += 'None'
    return answ
