# About
This is a script for building a dictionary with a tree structure.
<br>
Script requires list of nodes. Nodes are typles with structure `(parent_id, id)`.

# Limitations:
- Nodes must be valid.
- The nodes in the list should be sorted by the depth in the tree.

# Example

## Signature
```
to_tree(source)
```

## Input
```
[
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]
```

## Output
```
{
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}
```
