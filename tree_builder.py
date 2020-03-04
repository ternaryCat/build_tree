def to_tree(source):
    tree = {}
    for node in source:
        if node[0] == None:
            tree[node[1]] = {}
            continue

        path = find_path_to_parent(tree, node[0])
        if (not path):
            continue

        parent = tree
        for key in path:
            parent = parent[key]
        parent[node[1]] = {}
        
    return tree

def find_path_to_parent(tree, target_id):
    path = [target_id]
    if target_id in tree:
        return path

    for nested_tree_key in tree:
        nested_path = find_path_to_parent(tree[nested_tree_key], target_id)
        if (nested_path):
            path = [nested_tree_key]
            return path + nested_path