import math


def minmax(scores, depth, current_node_index, current_depth, maximizing_player):
    print(current_node_index)
    if depth == current_depth:
        return scores[current_node_index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = minmax(scores, depth, current_node_index * 2 + i, current_depth+1, False)
            max_eval = max(eval, max_eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = minmax(scores, depth, current_node_index * 2 + i, current_depth+1, True)
            min_eval = min(eval, min_eval)
        return min_eval


scores = []
num_leaf_nodes = int(input("Enter the number of leaf nodes : "))
for _ in range(num_leaf_nodes):
    score = int(input(f"Enter the value of leaf node {_+1} : "))
    scores.append(score)

depth = int(math.log2(num_leaf_nodes))
maximizing_player = True
current_node_index = 0
current_depth = 0

best_solution = minmax(scores, depth, current_node_index, current_depth, maximizing_player)

print(f"Best Solution : {best_solution}")