def get_min(fringe, key):
    index_min = 0
    for i in range(len(fringe)):
        if fringe[i][key] < fringe[index_min][key]:
            index_min = i
    return index_min


def compute_cost(state, action):
    return 1

def h1(state):
    cost = 0
    for i in range(len(state)):
        cost += state[i] != i
    return cost


def h2(state):
    cost = 0
    for i in range(len(state)):
        j = state[i]
        actual_row_j = j // 3
        actual_col_j = j % 3

        current_row_i = i // 3
        current_col_i = i % 3

        cost += abs(actual_row_j - current_row_i) + abs(actual_col_j - current_col_i)

    return cost
