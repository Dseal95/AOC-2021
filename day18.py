import builtins


class Node(object):
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(string:str, left_sym:str='[', right_sym:str=']'):
    """Build a tree from a nested data structure."""
    # print(f'build_tree({string})')
    if string[0] != left_sym:
        return Node(value=int(string))
    depth = 0
    for i in range(len(string)):
        # print(depth)
        if string[i] == left_sym:
            depth+=1
        if string[i] == right_sym:
            depth-=1
        if string[i] == ',' and depth == 1:
            # print(f'lhs={string[1:i]}, rhs={string[i+1:-1]}')
            return Node(value=-1, left=build_tree(string[1:i]), right=build_tree(string[i+1:-1]))
    
    assert False 

def print_tree(node, depth:int=0):
    print(f"{' ' * depth}{node.value if node.value>=0 else '*'}")
    if node.left is not None:
        print_tree(node.left, depth+1)
    if node.right is not None:
        print_tree(node.right, depth+1)

def list_values(node):
    """List left and right values of a tree / node."""
    if node is None:
        return []
    if node.value >= 0:
        return [node.value]
    return list_values(node.left) + list_values(node.right)
 



def find_explode(node, depth=0):
    global index

    if depth == 4 and node.value < 0:
        # found a parent node at depth 4
        return index

    if node.value >= 0:
        index += 1
        return -1 
    
    left = find_explode(node.left, depth+1)

    if left >= 0:
        return left 
    
    return find_explode(node.right, depth+1)



def do_explode(node, explode_index, explode_values):
    global index
    global exploded

    if node.value >= 0:
        if index == explode_index - 1:
            node.value += explode_values[0]
        elif index == explode_index + 2:
            node.value += explode_values[1]
        index += 1
        return 

    do_explode(node.left, explode_index, explode_values)
    do_explode(node.right, explode_index, explode_values)

    if not exploded and index == explode_index + 2:
        node.value = 0
        node.left = node.right = None
        exploded = True

def do_split(node):
    if node is None:
        return False
    if node.value >= 0:
        if node.value >= 10:
            node.left = Node(value=node.value // 2)
            node.right = Node(value=(node.value + 1) // 2)
            node.value = -1
            return True 
        return False
    if do_split(node.left):
        return True 
    return do_split(node.right)


def clean_tree(tree):
    global index 
    global exploded
    while True:
        index = 0
        explode_index = find_explode(tree)
        if explode_index >= 0:
            values = list_values(tree)
            index = 0
            print(f'explode_index: {explode_index}')
            exploded = False
            do_explode(tree, explode_index, (values[explode_index], values[explode_index + 1]))
            print_tree(tree)
            continue
        index = 0
        if do_split(tree):
            print_tree(tree)
            continue
        break


def add(tree0, tree1):
    return Node(value=-1, left=tree0, right=tree1)


def magnitude(tree):
    if tree is None:
        return 0
    if tree.value >= 0:
        return tree.value
    return 3 * magnitude(tree.left) + 2 * magnitude(tree.right)


lines = [line[:-1].strip() for line in open('/Users/danielseal/AOC_2021/data/day18_example.txt').readlines()]

# part 1
index = 0
exploded = False
tree = build_tree(lines[0])

for line in lines[1:]:
    tree = add(tree, build_tree(line))
    clean_tree(tree)

print(magnitude(tree))

# # part 2
# most = 0
# for i in range(len(lines)):
#     for j in range(len(lines)):
#         if i == j:
#             continue
#         combined = add(build_tree(lines[i]), build_tree(lines[j]))
#         clean_tree(combined)
#         most = max(most, magnitude(combined))
# print(most)