class TrieNode:
    def __init__(self, children=None, is_last_char=False):
        self.children = children
        self.is_last_char = is_last_char


def insert(root, word):
    _insert_node(root, word, 0)


def _insert_node(root, word, count):
    if len(word) == count:
        return
    else:
        if word[count] in root.children:
            return _insert_node(root.children[word[count]], word, count + 1)
        else:
            new_node = TrieNode()
            if len(word) == count - 1:
                new_node.is_last_char = True
            else:
                new_node.is_last_char = False
            root.children[word[count]] = new_node
            return _insert_node(root.children[word[count]], word, count)


def search_prefix(root, word):
    return search(root, word, 0, prefix=True)


def search(root, pattern, count, prefix=True):
    if len(pattern) == count:
        if prefix:
            return True
        else:
            return root.is_last_char
    else:
        if pattern[count] in root.children:
            return search(
                root.children[pattern[count]], pattern, count + 1, prefix
            )
        else:
            return False
