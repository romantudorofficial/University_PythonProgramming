def eval (node):

    if isinstance (node.value, int):
        return node

    elif isinstance (node, float):
        return eval(node.value, (int, float))



def print_ast (node, level = 0):

    indent = ' ' * (level * 2)

    if node:
        print(f"{indent}{node.value}")



# AST - expresie: 13 * 2 - 11 + 5 + 21 / 7

root = Node("+", Node())



print(eval(root))