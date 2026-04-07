# -----------------------------
# EXEMPLO DE USO
# -----------------------------
if __name__ == "__main__":
    keys = [5, 10, 15, 20, 25, 30, 35]

    # "previsão" do modelo de ML
    predicted_frequencies = {
        20: 100,
        10: 60,
        30: 40,
        5: 10,
        15: 8,
        25: 6,
        35: 4
    }

    tree = LearningAugmentedBST(predicted_frequencies)
    tree.build_from_sorted_keys(keys)

    print("Árvore construída com base nas frequências previstas:\n")
    tree.print_tree()

    print("\nPercurso em ordem:", tree.inorder())

    print("\nBuscas:")
    for value in [20, 10, 35]:
        found, cost = tree.search(value)
        print(f"Buscar {value}: encontrado={found}, comparações={cost}")