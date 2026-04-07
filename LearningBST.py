class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class LearningAugmentedBST:
    def __init__(self, predicted_frequencies):
        """
        predicted_frequencies: dicionário {elemento: frequência prevista}
        Exemplo: {10: 50, 5: 10, 20: 5}
        """
        self.predicted_frequencies = predicted_frequencies
        self.root = None

    def build_from_sorted_keys(self, keys):
        """
        Constrói a árvore priorizando elementos com maior frequência prevista.
        A ideia é tentar colocar elementos mais acessados mais próximos da raiz.
        """
        self.root = self._build(keys)

    def _build(self, keys):
        if not keys:
            return None

        # escolhe como raiz o elemento com maior frequência prevista
        best_key = max(keys, key=lambda k: self.predicted_frequencies.get(k, 0))
        node = Node(best_key)

        left_keys = [k for k in keys if k < best_key]
        right_keys = [k for k in keys if k > best_key]

        node.left = self._build(left_keys)
        node.right = self._build(right_keys)

        return node

    def search(self, key):
        """
        Busca um elemento e retorna:
        (encontrou, número de comparações)
        """
        current = self.root
        comparisons = 0

        while current:
            comparisons += 1

            if key == current.key:
                return True, comparisons
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False, comparisons

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def print_tree(self, node=None, level=0, prefix="Raiz: "):
        if node is None and level == 0:
            node = self.root

        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")