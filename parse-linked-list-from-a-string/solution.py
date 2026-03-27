from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    parts = list_repr.split(" -> ")
    current = None
    for i in reversed(parts[:-1]):
        current = Node(int(i), current)

    return current
